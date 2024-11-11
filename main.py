from __future__ import annotations
import pyautogui

from common.application_manager import ApplicationManager
from config import APPLICATION_PATH
from common.utils import click_icon_on_screen, click_text_on_screen


def main():
    with ApplicationManager(APPLICATION_PATH):
        pyautogui.sleep(2)


if __name__ == "__main__":
    main()
