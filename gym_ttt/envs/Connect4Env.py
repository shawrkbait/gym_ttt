import numpy as np
import gym
from gym import spaces

COLUMNS = 7
MAX_PLAYERS = 2

class Connect4Env(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    super(Connect4Env, self).__init__()
    self.action_space = spaces.Discrete(7*6) # Place to put
    self.valid_actions = np.array([35,36,37,38,39,40,41],dtype=np.uint8)
    # 3x3 grid, 0=none, 1=O, 2=X
    self.board_space = spaces.Box(low=0, high=2, shape=[7,6,1], dtype=np.uint8) # 3x3 grid
    self.board = np.zeros(7*6,dtype=np.uint8)
    self.winners = [
    # horizontal
      [0,1,2,3],
      [1,2,3,4],
      [2,3,4,5],
      [3,4,5,6],
      [7,8,9,10],
      [8,9,10,11],
      [9,10,11,12],
      [10,11,12,13],
      [14,15,16,17],
      [15,16,17,18],
      [16,17,18,19],
      [17,18,19,20],
      [21,22,23,24],
      [22,23,24,25],
      [23,24,25,26],
      [24,25,26,27],
      [28,29,30,31],
      [29,30,31,32],
      [30,31,32,33],
      [31,32,33,34],
      [35,36,37,38],
      [36,37,38,39],
      [37,38,39,40],
      [38,39,40,41],

    # vertical
      [0,7,14,21],
      [7,14,21,28],
      [14,21,28,35],
      [1,8,15,22],
      [8,15,22,29],
      [15,22,29,36],
      [2,9,16,23],
      [9,16,23,30],
      [16,23,30,37],
      [3,10,17,24],
      [10,17,24,31],
      [17,24,31,38],
      [4,11,18,25],
      [11,18,25,32],
      [18,25,32,39],
      [5,12,19,26],
      [12,19,26,33],
      [19,26,33,40],
      [6,13,20,27],
      [13,20,27,34],
      [20,27,34,41],

    # cross
      [3,9,15,21],
      [4,10,16,22],
      [10,16,22,28],
      [5,11,17,23],
      [11,17,23,29],
      [17,23,29,35],
      [6,12,18,24],
      [12,18,24,30],
      [18,24,30,36],
      [13,19,25,31],
      [19,25,31,37],
      [20,26,32,38],
  
      [3,11,19,27],
      [2,10,18,26],
      [10,18,26,34],
      [1,9,17,25],
      [9,17,25,33],
      [17,25,33,41],
      [0,8,16,24],
      [8,16,24,32],
      [16,24,32,40],
      [7,15,23,31],
      [15,23,31,39],
      [14,22,30,38],
    ]
    self.playerTurn = 0

  def step(self, action, token):
    if action not in self.valid_actions:
      return self._get_obs(), 0, False, {}
    
    reward = [0,0]
    done = False

    self.board[action] = token

    # Update valid actions
    if action < 7:
      np.delete(self.valid_actions, action)
    else:
      self.valid_actions[action % 7] -= 7

    nextPlayer = 0 if self.playerTurn + 1 == MAX_PLAYERS else self.playerTurn + 1

    for x,y,z,a in self.winners:
      if(self.board[x] != 0 and
         self.board[x] == self.board[y] == self.board[z] == self.board[a]):
        done = True
        reward[self.playerTurn] = 1
        reward[nextPlayer] = -1
        return self._get_obs(), reward, done, {}

    self.playerTurn = nextPlayer

    return self._get_obs(), reward, done, {}

  def _get_obs(self):
    return (self.playerTurn, self.valid_actions, self.board)

  def reset(self):
    self.__init__()
    return self._get_obs()

  def render(self, mode='human', close=False):
    for i in range(len(self.board)):
      print('%d ' % (self.board[i]), end = "")
      if i % COLUMNS == (COLUMNS - 1):
        print()
    print()
