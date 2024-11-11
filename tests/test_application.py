import unittest

import pyautogui

from common.application_manager import ApplicationManager
from tests.rick_roll import run_rick_roll
from config import APPLICATION_PATH


class TestApplication(unittest.TestCase):

    def test_open_application(self):
        with ApplicationManager(APPLICATION_PATH):
            pass

    def test_rick_roll(self):
        try:
            run_rick_roll()
        except Exception as e:
            pyautogui.screenshot("screenshots/test.png")
            raise e
