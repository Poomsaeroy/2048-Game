from Game.main import MainScreen, GameApp
import unittest
from unittest.mock import Mock, patch

class MoveModuleTest(unittest.TestCase):
    # left
    @patch('Game.main.MainScreen.board_move')
    def test_left_pos2_pos3_return_pos0_pos1(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 2, 1,
                         0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0]
        game.move('left')
        self.assertEqual(game.numstate, [2, 1, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0])

    @patch('Game.main.MainScreen.board_move')
    def test_left_pos5_pos15_return_pos4_pos12(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 2, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 2]
        game.move('left')
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         2, 0, 0, 0,
                                         0, 0, 0, 0,
                                         2, 0, 0, 0])

    @patch('Game.main.MainScreen.board_move')
    def test_left_pos9_pos12_return_pos8_pos12(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 3, 0, 0,
                         2, 0, 0, 0]
        game.move('left')
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         3, 0, 0, 0,
                                         2, 0, 0, 0])

    @patch('Game.main.MainScreen.board_move')
    def test_left_5pos(self, board_move):
        game = MainScreen()
        game.numstate = [0, 1, 0, 0,
                         0, 1, 3, 0,
                         0, 0, 4, 0,
                         0, 0, 3, 0]
        game.move('left')
        self.assertEqual(game.numstate, [1, 0, 0, 0,
                                         1, 3, 0, 0,
                                         4, 0, 0, 0,
                                         3, 0, 0, 0])

    @patch('Game.main.MainScreen.board_move')
    def test_left_allpos_notnull_return_same(self, board_move):
        game = MainScreen()
        game.numstate = [1, 2, 1, 2,
                         2, 1, 2, 1,
                         1, 2, 1, 2,
                         2, 2, 1, 1]
        game.move('left')
        self.assertEqual(game.numstate, [1, 2, 1, 2,
                                         2, 1, 2, 1,
                                         1, 2, 1, 2,
                                         2, 2, 1, 1])

    # right
    @patch('Game.main.MainScreen.board_move')
    def test_right_pos1_pos2_return_pos2_pos3(self, board_move):
        game = MainScreen()
        game.numstate = [0, 3, 2, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0]
        game.move('right')
        self.assertEqual(game.numstate, [0, 0, 3, 2,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0])

    @patch('Game.main.MainScreen.board_move')
    def test_right_pos5_pos15_return_pos7_pos15(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 2, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 3]
        game.move('right')
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         0, 0, 0, 2,
                                         0, 0, 0, 0,
                                         0, 0, 0, 3])

    @patch('Game.main.MainScreen.board_move')
    def test_right_pos9_pos12_return_pos11_pos15(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 1, 0, 0,
                         3, 0, 0, 0]
        game.move('right')
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 1,
                                         0, 0, 0, 3])

    @patch('Game.main.MainScreen.board_move')
    def test_right_5pos(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 0, 1,
                         0, 0, 3, 0,
                         0, 2, 1, 0,
                         0, 0, 4, 0]
        game.move('right')
        self.assertEqual(game.numstate, [0, 0, 0, 1,
                                         0, 0, 0, 3,
                                         0, 0, 2, 1,
                                         0, 0, 0, 4])

    @patch('Game.main.MainScreen.board_move')
    def test_right_allpos_notnull_return_same(self, board_move):
        game = MainScreen()
        game.numstate = [1, 2, 1, 3,
                         2, 1, 1, 4,
                         1, 3, 2, 2,
                         2, 1, 3, 2]
        game.move('right')
        self.assertEqual(game.numstate, [1, 2, 1, 3,
                                         2, 1, 1, 4,
                                         1, 3, 2, 2,
                                         2, 1, 3, 2])

    # up
    @patch('Game.main.MainScreen.board_move')
    def test_up_pos6_pos7_return_pos2_pos3(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 0, 3, 1,
                         0, 0, 0, 0,
                         0, 0, 0, 0]
        game.move('up')
        self.assertEqual(game.numstate, [0, 0, 3, 1,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0])

    @patch('Game.main.MainScreen.board_move')
    def test_up_pos5_pos15_return_pos1_pos3(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 2, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 3]
        game.move('up')
        self.assertEqual(game.numstate, [0, 2, 0, 3,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0])

    @patch('Game.main.MainScreen.board_move')
    def test_up_pos9_pos12_return_pos1_pos0(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 3, 0, 0,
                         1, 0, 0, 0]
        game.move('up')
        self.assertEqual(game.numstate, [1, 3, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0])

    @patch('Game.main.MainScreen.board_move')
    def test_up_5pos(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         1, 2, 3, 0,
                         0, 0, 1, 2,
                         0, 0, 0, 0]
        game.move('up')
        self.assertEqual(game.numstate, [1, 2, 3, 2,
                                         0, 0, 1, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0])

    @patch('Game.main.MainScreen.board_move')
    def test_up_allpos_notnull_return_same(self, board_move):
        game = MainScreen()
        game.numstate = [1, 2, 1, 3,
                         2, 1, 1, 4,
                         1, 3, 2, 2,
                         2, 1, 3, 2]
        game.move('up')
        self.assertEqual(game.numstate, [1, 2, 1, 3,
                                         2, 1, 1, 4,
                                         1, 3, 2, 2,
                                         2, 1, 3, 2])
    # down
    @patch('Game.main.MainScreen.board_move')
    def test_down_pos2_pos3_return_pos14_pos15(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 1, 3,
                         0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0]
        game.move('down') 
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 1, 3])               
    
    @patch('Game.main.MainScreen.board_move')
    def test_down_pos5_pos15_return_pos13_pos15(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 3, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 1]
        game.move('down')
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 3, 0, 1])

    @patch('Game.main.MainScreen.board_move')
    def test_down_pos9_pos12_return_pos13_pos12(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 2, 0, 0,
                         1, 0, 0, 0]
        game.move('down')
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         1, 2, 0, 0])

    @patch('Game.main.MainScreen.board_move')
    def test_down_5pos(self, board_move):
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         2, 1, 3, 0,
                         0, 4, 1, 0,
                         0, 0, 0, 0]
        game.move('down')
        self.assertEqual(game.numstate, [0, 0, 0, 0,
                                         0, 0, 0, 0,
                                         0, 1, 3, 0,
                                         2, 4, 1, 0])

    @patch('Game.main.MainScreen.board_move')
    def test_down_allpos_notnull_return_same(self, board_move):
        game = MainScreen()
        game.numstate = [1, 2, 1, 3,
                         2, 1, 1, 4,
                         1, 3, 2, 2,
                         2, 1, 3, 2]
        game.move('down')
        self.assertEqual(game.numstate, [1, 2, 1, 3,
                                         2, 1, 1, 4,
                                         1, 3, 2, 2,
                                         2, 1, 3, 2])