import numpy as np
import gym
from gym import spaces

WIN = [1,1,1]

class TTTEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    super(TTTEnv, self).__init__()
    self.action_space = spaces.Discrete(9) # Place to put
    # 3x3 grid, 0=none, 1=O, 2=X
    self.observation_space = spaces.Box(low=0, high=2, shape=[3,3,1], dtype=np.uint8) # 3x3 grid
    self.observation = [0,0,0,0,0,0,0,0,0]
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

  def step(self, action):
    reward = 0
    done = False

    a = self.observation

    self.observation[action] = 1

    for x,y,z in self.winners:
      if(self.observation[x] != 0 and
         self.observation[x] == self.observation[y] == self.observation[z]):
        done = True
        reward = 1
    return self.observation, reward, done, {}

  def _get_obs(self):
    return self.observation

  def reset(self):
    self.__init__()
    return self._get_obs()

  def render(self, mode='human', close=False):
    for i in range(len(self.observation)):
      print('%d, ' % (self.observation[i]), end = "")
      if i % 3 == 2:
        print()
    print()
