import pyautogui

from image_helper.image_helper import locate_icon_center_on_image
from text_helper.text_helper import (
    locate_text_center_on_image,
    locate_word_center_on_image,
)


def check_loading_indicator(icon_key: str):
    for _ in range(100):
        screenshot_path = f"screenshots/{icon_key}.png"
        pyautogui.screenshot(screenshot_path)
        pyautogui.sleep(0.2)
        if not locate_icon_center_on_image(screenshot_path, f"icons/{icon_key}.png"):
            return

    raise Exception("Loading time was exceeded!")


def click_icon_on_screen(icon_key: str):
    screenshot_path = f"screenshots/{icon_key}.png"
    pyautogui.screenshot(screenshot_path)
    x, y = locate_icon_center_on_image(screenshot_path, f"icons/{icon_key}.png")
    pyautogui.click(x, y)


def click_text_on_screen(text: str):
    image = pyautogui.screenshot(f"screenshots/{text}.png")
    x, y = locate_text_center_on_image(image, text)
    pyautogui.click(x, y)


def click_word_on_screen(text: str):
    image = pyautogui.screenshot(f"screenshots/{text}.png")
    x, y = locate_word_center_on_image(image, text)
    pyautogui.click(x, y)
