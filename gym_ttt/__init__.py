from gym.envs.registration import register
 
register(id='TicTacToe-v0', 
    entry_point='gym_ttt.envs:TTTEnv', 
)

register(id='Connect4-v0', 
    entry_point='gym_ttt.envs:Connect4Env', 
)
