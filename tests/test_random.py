from Game.main import MainScreen, GameApp
import unittest
from unittest.mock import Mock, patch

class RandomModuleTest(unittest.TestCase):
    @patch('Game.main.MainScreen.board_process')
    def test_rand_fulltable_keyleft_isFalse(self, board_process):
        game = MainScreen()
        for i in range(16):
            game.numstate[i] = 1 # all id not 0
        game.randompos('right')
        self.assertTrue(game.left_d)
        self.assertFalse(game.right_d)
        self.assertTrue(game.up_d)
        self.assertTrue(game.down_d)
    
    @patch('Game.main.MainScreen.board_process')
    def test_rand_fulltable_keyright_isFalse(self, board_process):
        game = MainScreen()
        for i in range(16):
            game.numstate[i] = 1 # all id not 0
        game.randompos('left')
        self.assertFalse(game.left_d)
        self.assertTrue(game.right_d)
        self.assertTrue(game.up_d)
        self.assertTrue(game.down_d)

    @patch('Game.main.MainScreen.board_process')
    def test_rand_fulltable_keyup_isFalse(self, board_process):
        game = MainScreen()
        for i in range(16):
            game.numstate[i] = 1 # all id not 0
        game.randompos('up')
        self.assertTrue(game.left_d)
        self.assertTrue(game.right_d)
        self.assertFalse(game.up_d)
        self.assertTrue(game.down_d)

    @patch('Game.main.MainScreen.board_process')
    def test_rand_fulltable_keydown_isFalse(self, board_process):
        game = MainScreen()
        for i in range(16):
            game.numstate[i] = 1 # all id not 0
        game.randompos('down')
        self.assertTrue(game.left_d)
        self.assertTrue(game.right_d)
        self.assertTrue(game.up_d)
        self.assertFalse(game.down_d)

    @patch('random.choice', return_value = 13)
    @patch('random.randint', return_value = 2)
    @patch('Game.main.MainScreen.board_randompos', return_value = True)
    def test_rand_give_2_atpos13(self, randchoice, randint, board_rand):
        numstate = [0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 2, 0, 0]
        mock = Mock()
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0]
        game.board_randompos = mock()
        game.randompos(None)
        self.assertEqual(game.numstate, numstate)

    @patch('random.choice', return_value = 1)
    @patch('random.randint', return_value = 1)
    @patch('Game.main.MainScreen.board_randompos', return_value = True)
    def test_rand_give_1_atpos1(self, randchoice, randint, board_rand):
        numstate = [0, 1, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0]
        mock = Mock()
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0]
        game.board_randompos = mock()
        game.randompos('left')
        self.assertTrue(game.left_d)
        self.assertEqual(game.numstate, numstate)

    @patch('random.choice', return_value = 5)
    @patch('random.randint', return_value = 2)
    @patch('Game.main.MainScreen.board_randompos', return_value = True)
    def test_rand_give_2_atpos5(self, randchoice, randint, board_rand):
        numstate = [0, 0, 0, 0,
                    0, 2, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0]
        mock = Mock()
        game = MainScreen()
        game.numstate = [0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0,
                         0, 0, 0, 0]
        game.board_randompos = mock()
        game.randompos('up')
        self.assertTrue(game.up_d)
        self.assertEqual(game.numstate, numstate)

