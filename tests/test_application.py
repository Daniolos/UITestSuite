from pathlib import Path
import unittest
import pyautogui

from common.application_manager import ApplicationManager
from tests.meaning_of_life import find_meaning
from tests.rick_roll import run_rick_roll
from config import APPLICATION_PATH, ICONS_PATH, SCREENSHOTS_PATH


class TestApplication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Path(SCREENSHOTS_PATH).mkdir(exist_ok=True)
        Path(ICONS_PATH).mkdir(exist_ok=True)

    def test_open_application(self):
        with ApplicationManager(APPLICATION_PATH):
            pass

    def test_rick_roll(self):
        try:
            run_rick_roll()
        except Exception as e:
            pyautogui.screenshot(f"{SCREENSHOTS_PATH}/test.png")
            raise e

    def test_find_meaning(self):
        try:
            find_meaning()
        except Exception as e:
            pyautogui.screenshot(f"{SCREENSHOTS_PATH}/test.png")
            raise e
