import gym
import gym_ttt

from agent import Agent

env = gym.make('TicTacToe-v0')

player1 = Agent(1)
player2 = Agent(2)

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
      playerTurn, board = observation
      print(observation)
      action = players[playerTurn]['agent'].act(observation)
      observation, reward, done, info = env.step(action, players[playerTurn]['token'])
      if done:
          env.render()
          print("Episode finished after {} timesteps".format(t+1))
          break
env.close()


