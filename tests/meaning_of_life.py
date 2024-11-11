import pyautogui

from common.application_manager import ApplicationManager
from config import APPLICATION_PATH
from common.utils import click_icon_on_screen


def find_meaning():
    with ApplicationManager(APPLICATION_PATH):
        pyautogui.sleep(1.5)

        click_icon_on_screen("new_tab")
        pyautogui.sleep(1)

        pyautogui.write("Wikipedia")
        pyautogui.press("enter")
        pyautogui.sleep(2.5)

        click_icon_on_screen("wikipedia")
        pyautogui.sleep(2.5)

        pyautogui.write("The answer to life, the universe and everything")
        pyautogui.press("enter")
        pyautogui.sleep(1.5)
