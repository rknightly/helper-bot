import unittest.main
from unittest import TestCase

import sys
sys.path.append('../')

from onlineActions import *

class TestWebAction(TestCase):
    def test_open_website(self):
        WebAction.open_website("google.com")

class TestGmail(TestCase):
    def test_pandora(self):
        self.assertEqual(Pandora.aliases, ["pandora"])
        Pandora.do_action()

if __name__ == '__main__':
    unittest.main()
