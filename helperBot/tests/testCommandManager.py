import unittest.main
from unittest import TestCase

import sys
sys.path.append('../')

from commandManager import CommandManager

class TestManageCommand(TestCase):
    def test_pandora(self):
        manager = CommandManager()
        manager.manageCommand("pandora")

if __name__ == '__main__':
    unittest.main()
