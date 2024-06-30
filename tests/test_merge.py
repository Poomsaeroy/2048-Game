from Game.main import MainScreen, GameApp
import unittest
from unittest.mock import Mock, patch


class MergeModuleTest(unittest.TestCase):
    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    def test_pos1_4_pos2_4_return_pos1_score8(self, board_merge, board_plus, win):
        game = MainScreen()
        game.numstate = [0, 2, 2, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0]
        game.merge(1, 2)
        self.assertEqual(game.numstate, [0, 3, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0])
        self.assertEqual(game.totalscore, 8)


    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    def test_pos3_4_pos2_4_return_pos3_score16(self, board_merge, board_plus, win):
        game = MainScreen()
        game.numstate = [0, 0, 3, 3,
                         0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0]
        game.merge(2, 3)
        self.assertEqual(game.numstate, [0, 0, 4, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0])
        self.assertEqual(game.totalscore, 16)


    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    def test_pos5_16_pos7_16_return_pos7_score32(self, board_merge, board_plus, win):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 4, 0, 4,
                         0, 0, 0, 0,
                         0, 0, 0, 0]
        game.merge(7, 5)
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         0, 0, 0, 5,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0])
        self.assertEqual(game.totalscore, 32)


    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    def test_pos5_16_pos7_16_return_pos7_score32_butpos6issame(self, board_merge, board_plus, win):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 4, 2, 4,
                         0, 0, 0, 0,
                         0, 0, 0, 0]
        game.merge(7, 5)
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         0, 0, 2, 5,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0])
        self.assertEqual(game.totalscore, 32)