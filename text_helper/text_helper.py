from PIL import Image
from pytesseract import image_to_data, Output

from text_helper.text_element import TextElement
from text_helper.text_element_group import TextElementGroup


def locate_word_center_on_image(image: Image, text: str) -> tuple[int, int] | None:
    data = image_to_data(image, output_type=Output.DICT)
    text_elements = sorted(
        get_text_elements(data, text), key=lambda t: (-t.top, -t.bottom, t.height)
    )

    if not text_elements:
        raise Exception(f"`{text}` could not be found on the screen.")

    return text_elements[-1].get_center()


def locate_text_center_on_image(image: Image, text: str) -> tuple[int, int]:
    text_sections = text.split()

    if not text_sections:
        raise Exception(f"No valid text was provided: {text}")

    data = image_to_data(image, output_type=Output.DICT)

    largest_text_element_groups = get_largest_text_element_groups(text_sections, data)

    if not largest_text_element_groups:
        raise Exception(f"`{text}` could not be found on the screen.")

    return largest_text_element_groups[0].get_center()


def get_largest_text_element_groups(text_sections, data):

    text_elements = sorted(
        get_text_elements(data, text_sections[0]), key=lambda t: t.height, reverse=True
    )
    text_element_groups = [
        TextElementGroup(text_element) for text_element in text_elements
    ]

    if len(text_sections) == 1:
        return text_element_groups

    for text_section in text_sections[1:]:
        text_elements = get_text_elements(data, text_section)
        text_element_groups = get_updated_text_element_groups(
            text_element_groups, text_elements
        )

    return text_element_groups


def get_updated_text_element_groups(
    text_element_groups: list[TextElementGroup], text_elements: list[TextElement]
):
    return [
        text_element_group.add(text_element)
        for text_element_group in text_element_groups
        for text_element in sorted(
            text_elements, key=lambda t: abs(text_element_group.top - t.top)
        )
        if text_element_group.is_before(text_element)
    ]


def get_text_elements(data: dict, target: str) -> list[TextElement]:
    return [
        TextElement(
            data["level"][index],
            data["page_num"][index],
            data["block_num"][index],
            data["par_num"][index],
            data["line_num"][index],
            data["word_num"][index],
            data["left"][index],
            data["top"][index],
            data["width"][index],
            data["height"][index],
            data["conf"][index],
            data["text"][index],
        )
        for index, text in enumerate(data["text"])
        if text.strip().lower() in target.strip().lower().split()
    ]
