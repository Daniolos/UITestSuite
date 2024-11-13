from __future__ import annotations
import pyautogui

from common.application_manager import ApplicationManager
from config import APPLICATION_PATH


def main():
    with ApplicationManager(APPLICATION_PATH):
        pyautogui.sleep(2)


if __name__ == "__main__":
    main()
