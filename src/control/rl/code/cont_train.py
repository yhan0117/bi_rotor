import gym
from stable_baselines3 import A2C, PPO
from customEnv.bi_rotor import dualrotorEnv
import os

# initialize environment
env = dualrotorEnv()
env.reset()

# load model
models_dir = "models/PPO-drotor"
logdir = "logs/drotor"

# training parameters 
steps = 10000
episodes = 50

# Rl algo
model = PPO.load(models_path, env = env, tensorboard_log = logdir)

# train and saveCartPole-v1
for i in range(1,episodes):
    obs = env.reset()
    terminated = False
    model.learn(total_timesteps = steps, reset_num_timesteps = False, tb_log_name = "PPO")
    model.save(f"{models_dir}/{end_step+steps*i}")

env.close()