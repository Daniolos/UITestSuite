from text_helper.text_element import TextElement


class TextElementGroup:
    @property
    def first(self):
        return self.text_elements[0] if self.text_elements else None

    @property
    def last(self):
        return self.text_elements[-1] if self.text_elements else None

    @property
    def height(self):
        return max(text_element.height for text_element in self.text_elements)

    @property
    def left(self):
        return min(text_element.left for text_element in self.text_elements)

    @property
    def right(self):
        return max(text_element.right for text_element in self.text_elements)

    @property
    def top(self):
        return min(text_element.top for text_element in self.text_elements)

    @property
    def bottom(self):
        return max(text_element.bottom for text_element in self.text_elements)

    def __init__(self, text_element: TextElement) -> None:
        self.text_elements: list[TextElement] = list()
        self.add(text_element)

    def add(self, text_element: TextElement):
        self.text_elements.append(text_element)
        return self

    def is_before(self, text_element: TextElement, margin: float = None):
        if margin is None:
            margin = self.height
        return self.is_left(text_element, margin) or self.is_above(text_element, margin)

    def is_left(self, text_element: TextElement, margin: float = None):
        if margin is None:
            margin = self.height
        return self.last.is_left(text_element, margin)

    def is_above(self, text_element: TextElement, margin: float = None):
        if margin is None:
            margin = self.height
        return self.first.is_above(text_element, margin)

    def get_center(self):
        horizontal_center = (self.left + self.right) / 2
        vertical_center = (self.top + self.bottom) / 2
        return (horizontal_center, vertical_center)
