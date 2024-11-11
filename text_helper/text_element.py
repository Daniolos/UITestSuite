from __future__ import annotations
from dataclasses import dataclass


@dataclass
class TextElement:
    level: int
    page_num: int
    block_num: int
    par_num: int
    line_num: int
    word_num: int
    left: int
    top: int
    width: int
    height: int
    conf: int
    text: str

    @property
    def bottom(self) -> int:
        return self.top - self.height

    @property
    def right(self) -> int:
        return self.left + self.width

    def is_near(self, other: TextElement, margin: float = None):
        if margin is None:
            margin = self.height
        return (
            other.left <= self.right + margin
            and self.left <= other.right + margin
            and other.top <= self.bottom + margin
            and self.top <= other.bottom + margin
        )

    def is_before(self, other: TextElement, margin: float = None):
        if margin is None:
            margin = self.height
        return self.is_left(other, margin) or self.is_above(other, margin)

    def is_left(self, other: TextElement, margin: float = None):
        if margin is None:
            margin = self.height
        return (
            self.left < other.left + margin
            and self.right < other.right + margin
            and other.left <= self.right + margin
            and self.top - margin <= other.top <= self.top + margin
        )

    def is_above(self, other: TextElement, margin: float = None):
        if margin is None:
            margin = self.height
        return (
            self.top < other.top + margin
            and self.bottom < other.bottom + margin
            and other.top <= self.bottom + margin
            and self.left - margin <= other.left <= self.left + margin
        )

    def get_center(self) -> tuple[float, float]:
        horizontal_center = (self.left + self.right) / 2
        vertical_center = (self.top + self.bottom) / 2
        return (horizontal_center, vertical_center)
