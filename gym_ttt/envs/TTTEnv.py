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

  def step(self, action):
    reward = 0
    done = False

    a = self.observation

    self.observation[action] = 1

    # horizontal
    if (np.array_equal(a[0:3], WIN) or
       np.array_equal(a[3:6], WIN) or
       np.array_equal(a[6:9], WIN) or
    # vertical
       np.array_equal([a[0],a[3],a[6]], WIN) or
       np.array_equal([a[1],a[4],a[7]], WIN) or
       np.array_equal([a[2],a[5],a[8]], WIN) or
    # cross
       np.array_equal([a[0],a[4],a[8]], WIN) or
       np.array_equal([a[2],a[4],a[6]], WIN)
       ):
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
