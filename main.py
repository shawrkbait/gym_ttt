import gym
import gym_ttt

env = gym.make('TicTacToe-v0')
for i_episode in range(1):
    observation = env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        # Avoid invalid action
        while observation[action] == 1:
          action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            env.render()
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()


