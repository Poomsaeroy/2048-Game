import os
os.environ["KIVY_NO_ARGS"] = "1"
from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import random

class MenuScreen(Screen):
    pass

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        # self._keyboard.bind(on_key_down = self._on_key_down)
        self._keyboard.bind(on_key_up = self._on_key_up)
        self.left_d = True 
        self.right_d = True 
        self.up_d = True
        self.down_d = True
        self.process = True
        self.totalscore = str(0)
        self.num = ['-','2','4','8','16','32','64','128','256','512','1024','2048','4096']  ## num[0] = default for this meaning
        self.numstate = [0, 0, 0, 0,     # 0  1  2  3
                         0, 0, 0, 0,     # 4  5  6  7
                         0, 0, 0, 0,     # 8  9  10 11
                         0, 0, 0, 0]     # 12 13 14 15
        self.touch_down = None

        self.randompos(None)    # สุ่มตำแหน่งเลข

    def _on_keyboard_closed(self):
        # self._keyboard.unbind(on_key_down = self._on_key_down)
        self._keyboard.unbind(on_key_up = self._on_key_up)
        self._keyboard = None

    # def _on_key_down(self, keyboard, keycode, text, modifiers):
    #     print('down',keycode)

    def on_touch_down(self, touch):
        if touch.y <= self.height*5/6:
            self.touch_down = touch.pos
        # print('down',touch.y, self.height)
        super(MainScreen, self).on_touch_down(touch)


    def on_touch_up(self, touch):
        if not self.process: # stop move if process = False
            return
        if self.touch_down != None:
            x1, y1 = self.touch_down
            x2, y2 = touch.pos
            x_vector, y_vector = x2-x1, y2-y1
            # print('vector', x_vector, y_vector)
            if abs(x_vector) > abs(y_vector) :
                if x_vector > 0:
                    self.plus('right')
                else:
                    self.plus('left')

            elif abs(x_vector) < abs(y_vector) :
                if y_vector > 0:
                    self.plus('up')
                else:
                    self.plus('down')
        self.touch_down = None
        super(MainScreen, self).on_touch_down(touch)

    def _on_key_up(self, keyboard, keycode):
        keyinput = keycode[1]
        if not self.process: # stop bind keyboard input if process = False
            return

        if keyinput == 'left':
            # print('left')
            self.plus(keyinput)
            
        if keyinput == 'right':
            # print('right')
            self.plus(keyinput)

        if keyinput == 'up':
            # print('up')
            self.plus(keyinput)

        if keyinput == 'down':
            # print('down')
            self.plus(keyinput)

    def randompos(self, direction):
        lstempty = []
        # position check if value = 0 
        for position_value in range(len(self.numstate)):
            if self.numstate[position_value] == 0:
                # print(self.numstate[position_value],position_value)
                lstempty.append(position_value)
        # print(lstempty)

        try :
            i = random.choice(lstempty)     # random position
            j = random.randint(1, 2)        # random value(2, 4)
            self.numstate[i] = j # change value following position in GameApp list
            self.board_randompos(i, j)
        except:
            self.losscheck(direction)

    def board_randompos(self, i, j):
        self.ids[str(i)].text = self.num[j] # change value following position in GameApp output

    def merge(self, i, j ):
        if self.numstate[i] > 0:
            if self.numstate[j] > 0 and self.numstate[i] != self.numstate[j]:
                return True
            else:
                if self.numstate[i] == self.numstate[j]:
                    self.numstate[j] = 0 # move to merge
                    self.numstate[i] += 1 # plus 1 state
                    self.board_merge(i, j)
                    self.plusscore(self.num[self.numstate[i]])
                    self.left_d = True; self.right_d = True; self.up_d = True; self.down_d = True   # If game can merge ,so the "game over" status will be reset.
                    self.wincheck()
                    return True
        else:
            return False

    def board_merge(self, i, j):
        self.ids[str(i)].text = self.num[self.numstate[i]]  # make pos1 output *2
        self.ids[str(j)].text = self.num[self.numstate[j]]  # make pos2 output to default

    def move(self, direction):
        # print("Direction is", direction)
        if direction == 'left':
            for r in range(4):
                self.move_logic([0, 4, 8, 12], [4, 8, 12, 16], 1, r)

        if direction == 'right':
            for r in range(4):
                self.move_logic([3, 7, 11, 15], [-1, 3, 7, 11], -1, r)

        if direction == 'up':
            for r in range(4):
                self.move_logic([0, 1, 2, 3], [13, 14, 15, 16], 4, r)

        if direction == 'down':
            for r in range(4):
                self.move_logic([12, 13, 14, 15], [-1, 0, 1, 2], -4, r)
    
    def move_logic(self, lst_start, lst_stop, step, r):
        t = 0
        for i in range(lst_start[r], lst_stop[r], step):
            if self.numstate[i] > 0 and t == 0:
                continue
            if self.numstate[i] == 0:
                t += step
            else: 
                self.board_move(i, t)
                self.numstate[i-t] = self.numstate[i]
                self.numstate[i] = 0

    def board_move(self, i, t):
        self.ids[str(i-t)].text = self.num[self.numstate[i]]
        self.ids[str(i)].text = self.num[0]
    # ----------
    
    def plus(self, direction):
        if direction == 'left':
            # plus process --> 0+1, 1+2, 2+3 (4, 8, 12)
            for r in range(4):
                self.plus_logic([0, 4, 8, 12], [4, 8, 12, 16], 1, r)
            self.move(direction)
            self.randompos(direction)

        if direction == 'right':
            # plus process --> 3+2, 2+1, 1+0 (7, 11, 15)
            for r in range(4):
                self.plus_logic([3, 7, 11, 15], [-1, 3, 7, 11], -1, r)
            self.move(direction)
            self.randompos(direction)

        if direction == 'up':
            # plus process --> 0+4, 4+8, 8+12 (1, 2, 3)
            for r in range(4):
                self.plus_logic([0, 1, 2, 3], [13, 14, 15, 16], 4, r)
            self.move(direction)
            self.randompos(direction)

        if direction == 'down':
            # plus process --> 12+8, 8+4, 4+0 (13, 14, 15)
            for r in range(4):
                self.plus_logic([12, 13, 14, 15], [-1, 0, 1, 2], -4, r)
            self.move(direction)
            self.randompos(direction)

    def plus_logic(self, lst_start, lst_stop, step, r):
        for i in range(lst_start[r], lst_stop[r], step):
            for j in range(i+step, lst_stop[r], step):
                process = self.merge(i, j)
                if process:
                    break
            
    def plusscore(self, scorepoint):
        self.totalscore = int(self.totalscore) + int(scorepoint)
        self.board_scoreupdate('plus')

    def board_scoreupdate(self, a):
        if a == 'reset':
            self.ids['score'].text = 'Score : 0'
        if a == 'plus':
            self.ids['score'].text = 'Score : '+str(self.totalscore)

    def reset(self):
        for i in range(16):
            self.numstate[i] = 0
            self.board_reset(i)
        self.board_scoreupdate('reset')
        self.board_process('reset')
        self.process = True
        self.randompos(None)
        self.totalscore = str(0)
    
    def board_reset(self, i):
        self.ids[str(i)].text = self.num[0]

    def wincheck(self):
        for i in range(16):
            if self.numstate[i] >= 11: # num >= 2048 is win
                self.board_process('Win')
                self.process = False
                break

    def losscheck(self, direction):
        if direction == 'left':
            self.left_d = False
            # print('left fail')
        elif direction == 'right':
            self.right_d = False
            # print('right fail')
        elif direction == 'up':
            self.up_d = False
            # print('up fail')
        elif direction == 'down':
            self.down_d = False
            # print('down fail')
        # print(self.left_d, self.right_d, self.up_d, self.down_d)
        if self.left_d == False and self.right_d == False and self.up_d == False and self.down_d == False:
            self.process = False
            self.board_process('Loss')
            
    def board_process(self, winorloss):
        if winorloss == "Win":
            self.ids['gaming'].text = "Win"
        if winorloss == "Loss":
            self.ids['gaming'].text = "Game over"
        if winorloss == "reset":
            self.ids['gaming'].text = ''

class GameApp(App):
    def build(self):
        s = ScreenManager()
        s.add_widget(MenuScreen(name='menu'))
        s.add_widget(MainScreen(name='main'))
        return s

if __name__ == '__main__':
    GameApp().run()