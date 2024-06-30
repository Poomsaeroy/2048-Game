from Game.main import MainScreen, GameApp
import unittest
from unittest.mock import patch

class GamecheckAndResetTest(unittest.TestCase):
    @patch('Game.main.MainScreen.board_reset')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.board_process')
    @patch('Game.main.MainScreen.randompos')
    def test_reset_return_pos13_not_0(self, board_reset, board_scoreupdate, board_process, rand):
        numstate = [0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 3, 0, 0]
        game = MainScreen()
        game.reset() # all num = 0
        game.numstate[13] = 3
        board_reset.assert_called()
        board_scoreupdate.assert_called()
        board_process.assert_called()
        rand.assert_called()
        self.assertEqual(game.numstate, numstate)
        self.assertTrue(game.process)
    
    @patch('Game.main.MainScreen.board_reset')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.board_process')
    @patch('Game.main.MainScreen.randompos')
    def test_reset_return_pos5_not_0(self, board_reset, board_scoreupdate, board_process, rand):
        numstate = [0, 0, 0, 0,
                    2, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0]
        game = MainScreen()
        game.reset() # all num = 0
        game.numstate[4] = 2
        board_reset.assert_called()
        board_scoreupdate.assert_called()
        board_process.assert_called()
        rand.assert_called()
        self.assertEqual(game.numstate, numstate)
        self.assertTrue(game.process)

    @patch('Game.main.MainScreen.board_reset')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.board_process')
    @patch('Game.main.MainScreen.randompos')
    def test_reset_return_all0(self, board_reset, board_scoreupdate, board_process, rand):
        numstate = [0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0]
        game = MainScreen()
        game.reset() # all num = 0
        board_reset.assert_called()
        board_scoreupdate.assert_called()
        board_process.assert_called()
        rand.assert_called()
        self.assertEqual(game.numstate, numstate)
        self.assertTrue(game.process)
    
    # False = gamestop
    @patch('Game.main.MainScreen.board_process', return_value = None)
    def test_Gameprocess_win_return_false(self, board_process):
        game = MainScreen()
        game.numstate[5] = 11 # point = 2048
        gameprocess = game.wincheck()
        self.assertFalse(gameprocess)

    @patch('Game.main.MainScreen.board_process', return_value = None)
    def test_Gameprocess_Gameover_return_false(self, board_process):
        game = MainScreen()
        game.left_d = False
        game.right_d = False
        game.up_d = False
        game.down_d = False
        gameprocess = game.losscheck('right')
        self.assertFalse(gameprocess)