import gym
import gym_ttt

from agent import Agent

env = gym.make('Connect4-v0')

player1 = Agent()
player2 = Agent()

for i_episode in range(1):
  observation = env.reset()
  players = [{
              "agent": player1,
              "name": "player1",
              "token": 1
            },
            {
              "agent": player2,
              "name": "player2",
              "token": 2
            }
          ]

  for t in range(100):
      env.render()
      playerTurn, valid_actions, board = observation
      action = players[playerTurn]['agent'].act(observation)
      observation, reward, done, info = env.step(action, players[playerTurn]['token'])
      if done:
          env.render()
          print("Episode finished after {} timesteps".format(t+1))
          if reward[0] == 1:
            print("Winner = player1")
          else:
            print("Winner = player2")
          break
env.close()


