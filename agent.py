import random

class Agent():
  #def __init__(self):

  def act(self, observation):
    playerTurn, valid_actions, board = observation
    action = random.choice(valid_actions)
    return action
