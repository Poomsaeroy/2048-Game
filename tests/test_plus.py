from Game.main import MainScreen, GameApp
import unittest
from unittest.mock import Mock, patch

class PlusModuleTest(unittest.TestCase):
    # specail case
    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    # @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_process')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_leftget11_and_plusagain_return_same(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [10, 10, 10, 10,
                         0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0]
        game.plus('left') # set limit >= 11 to win
        game.plus('left') # can't access this in func if you'r in game @main.py_line41
        self.assertEqual(game.numstate, [12, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0])
        self.assertFalse(game.process)
        
    # left test
    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_leftplus2_pos1_pos2_return_pos0_is3(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [0, 1, 1, 0,
                         0, 1, 2, 0,
                         0, 3, 1, 0,
                         0, 2, 1, 0]
        game.plus('left')
        self.assertEqual(game.numstate, [2, 0, 0, 0,
                                         1, 2, 0, 0,
                                         3, 1, 0, 0,
                                         2, 1, 0, 0])

    
    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_leftplus4_pos8_pos12_return_same(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [0, 3, 3, 0,
                         0, 2, 1, 1,
                         3, 0, 0, 0,
                         2, 0, 0, 0]
        game.plus('left')
        self.assertEqual(game.numstate, [4, 0, 0, 0,
                                         2, 2, 0, 0,
                                         3, 0, 0, 0,
                                         2, 0, 0, 0])

    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_leftplus2and3_pos5_pos7_return_pos4_pos5(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 2, 0, 3,
                         3, 2, 1, 0,
                         0, 2, 1, 0]
        game.plus('left')
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         2, 3, 0, 0,
                                         3, 2, 1, 0,
                                         2, 1, 0, 0])

    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_leftplus2and3_pos5_pos7_buthaspos6_return_pos4_pos6(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [1, 1, 1, 1,
                         0, 2, 3, 2,
                         0, 3, 1, 1,
                         0, 1, 0, 0]
        game.plus('left')
        self.assertEqual(game.numstate, [2, 2, 0, 0,
                                         2, 3, 2, 0,
                                         3, 2, 0, 0,
                                         1, 0, 0, 0])

    # right test
    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_rifgtplus2_pos1_pos2_return_pos3_is3(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [1, 1, 1, 0,
                         3, 0, 0, 2,
                         0, 2, 1, 0,
                         0, 1, 0, 0]
        game.plus('right')
        self.assertEqual(game.numstate, [0, 0, 1, 2,
                                         0, 0, 3, 2,
                                         0, 0, 2, 1,
                                         0, 0, 0, 1])
    
    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_rightplus4_pos8_pos12_return_pos11_pos15_is4(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [2, 0, 1, 3,
                         1, 3, 3, 2,
                         2, 0, 0, 0,
                         2, 0, 0, 0]
        game.plus('right')
        self.assertEqual(game.numstate, [0, 2, 1, 3,
                                         0, 1, 4, 2,
                                         0, 0, 0, 2,
                                         0, 0, 0, 2])

    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_rightplus2and3_pos5_pos7_return_pos6_pos7(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [1, 0, 0, 1,
                         0, 2, 0, 2,
                         1, 1, 0, 0,
                         3, 0, 2, 0]
        game.plus('right')
        self.assertEqual(game.numstate, [0, 0, 0, 2,
                                         0, 0, 0, 3,
                                         0, 0, 0, 2,
                                         0, 0, 3, 2])

    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_rightplus2and3_pos5_pos7_buthaspos6_return_pos5_pos7(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [1, 0, 0, 1,
                         0, 2, 1, 2,
                         1, 1, 0, 0,
                         3, 0, 2, 0]
        game.plus('right')
        self.assertEqual(game.numstate, [0, 0, 0, 2,
                                         0, 2, 1, 2,
                                         0, 0, 0, 2,
                                         0, 0, 3, 2])
                                         
    # up test
    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_upplus2_pos5_pos9_return_pos1_is3(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [1, 1, 2, 0,
                         0, 2, 0, 0,
                         0, 2, 1, 0,
                         3, 0, 3, 0]
        game.plus('up')
        self.assertEqual(game.numstate, [1, 1, 2, 0,
                                         3, 3, 1, 0,
                                         0, 0, 3, 0,
                                         0, 0, 0, 0])
    
    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_upplus4_pos8_pos10_return_pos0_pos2_is4(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [1, 1, 1, 0,
                         0, 2, 0, 0,
                         2, 2, 2, 0,
                         3, 0, 3, 0]
        game.plus('up')
        self.assertEqual(game.numstate, [1, 1, 1, 0,
                                         2, 3, 2, 0,
                                         3, 0, 3, 0,
                                         0, 0, 0, 0])
    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_upplus2and3_pos2_pos10_return_pos2_pos6(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [1, 1, 1, 0,
                         0, 1, 0, 3,
                         2, 2, 1, 3,
                         3, 0, 3, 0]
        game.plus('up')
        self.assertEqual(game.numstate, [1, 2, 2, 4,
                                         2, 2, 3, 0,
                                         3, 0, 0, 0,
                                         0, 0, 0, 0])

    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_upplus2and3_pos2_pos10_buthaspos6_return_pos2_pos10(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [1, 1, 1, 0,
                         0, 1, 2, 3,
                         2, 2, 1, 3,
                         3, 0, 3, 0]
        game.plus('up')
        self.assertEqual(game.numstate, [1, 2, 1, 4,
                                         2, 2, 2, 0,
                                         3, 0, 1, 0,
                                         0, 0, 3, 0])

    # down test
    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_downplus2_pos5_pos9_return_pos13_is3(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [1, 1, 1, 0,
                         0, 2, 0, 0,
                         2, 2, 2, 0,
                         3, 0, 3, 0]
        game.plus('down')
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         1, 0, 1, 0,
                                         2, 1, 2, 0,
                                         3, 3, 3, 0])
    
    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_downplus4_pos8_pos10_return_pos12_pos14_is4(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [1, 1, 1, 0,
                         0, 2, 0, 0,
                         2, 2, 2, 0,
                         3, 0, 3, 0]
        game.plus('down')
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         1, 0, 1, 0,
                                         2, 1, 2, 0,
                                         3, 3, 3, 0])

    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_downplus2and3_pos2_pos10_return_pos10_pos14(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [1, 1, 1, 1,
                         0, 2, 0, 1,
                         2, 2, 1, 1,
                         3, 0, 3, 1]
        game.plus('down')
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         1, 0, 0, 0,
                                         2, 1, 2, 2,
                                         3, 3, 3, 2])

    @patch('Game.main.MainScreen.board_merge')
    @patch('Game.main.MainScreen.board_scoreupdate')
    @patch('Game.main.MainScreen.wincheck')
    @patch('Game.main.MainScreen.board_move')
    @patch('Game.main.MainScreen.randompos')
    def test_downplus2and3_pos2_pos10_buthaspos6_return_pos6_pos14(self, b_merge, b_score, win, b_move, rand):
        game = MainScreen()
        game.numstate = [1, 1, 1, 0,
                         0, 2, 5, 0,
                         2, 2, 2, 0,
                         3, 0, 3, 0]
        game.plus('down')
        self.assertEqual(game.numstate, [0, 0, 1, 0,
                                         1, 0, 5, 0,
                                         2, 1, 2, 0,
                                         3, 3, 3, 0])