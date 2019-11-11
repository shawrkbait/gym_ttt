import random

class Agent():
  def __init__(self, token):
    self.token = token

  def act(self, observation):
    playerTurn, board = observation
    action = random.randint(0,8)
    while board[action] != 0:
      action = random.randint(0,8)
    return action
