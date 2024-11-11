import pyautogui

from common.application_manager import ApplicationManager
from config import APPLICATION_PATH
from common.utils import (
    click_icon_on_screen,
    click_text_on_screen,
    click_word_on_screen,
)


def run_rick_roll():
    with ApplicationManager(APPLICATION_PATH):
        pyautogui.sleep(1.5)

        click_icon_on_screen("new_tab")
        pyautogui.sleep(1)

        pyautogui.write("youtube")
        pyautogui.press("enter")
        pyautogui.sleep(2.5)

        click_word_on_screen("Suchen")
        pyautogui.write("never gonna give you up")
        pyautogui.press("enter")
        pyautogui.sleep(1.5)

        click_text_on_screen(
            "Rick Astley - Never Gonna Give You Up (Official Music Video)"
        )
        pyautogui.sleep(1)

        pyautogui.press("f")
