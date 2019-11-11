import numpy as np
import gym
from gym import spaces

MAX_PLAYERS = 2

class TTTEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    super(TTTEnv, self).__init__()
    self.action_space = spaces.Discrete(9) # Place to put
    # 3x3 grid, 0=none, 1=O, 2=X
    self.board_space = spaces.Box(low=0, high=2, shape=[3,3,1], dtype=np.uint8) # 3x3 grid
    self.board = np.array([0,0,0,0,0,0,0,0,0],dtype=np.uint8)
    self.winners = [
    # horizontal
      [0,1,2],
      [3,4,5],
      [6,7,8],
    # vertical
      [0,3,6],
      [1,4,7],
      [2,5,8],
    # cross
      [0,4,8],
      [2,4,6]
    ]
    self.playerTurn = 1

  def step(self, action, token):
    reward = 0
    done = False

    a = self.board

    self.board[action] = token

    for x,y,z in self.winners:
      if(self.board[x] != 0 and
         self.board[x] == self.board[y] == self.board[z]):
        done = True
        reward = 1

    pt = 0 if self.playerTurn + 1 == MAX_PLAYERS else self.playerTurn + 1
    self.playerTurn = pt

    return self._get_obs(), reward, done, {}

  def _get_obs(self):
    return (self.playerTurn, self.board)

  def reset(self):
    self.__init__()
    return self._get_obs()

  def render(self, mode='human', close=False):
    for i in range(len(self.board)):
      print('%d, ' % (self.board[i]), end = "")
      if i % 3 == 2:
        print()
    print()
