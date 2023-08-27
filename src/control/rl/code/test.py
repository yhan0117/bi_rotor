import gym
from stable_baselines3 import A2C, PPO
from customEnv.bi_rotor import dualrotorEnv
import os

#------------------------------------------------------------------------------#

models_dir = "models/DualRotor/Integral"
end_step = 600000
episodes = 4
m = 5     # added mass in kg, could be the battery
x = 0.2 # m from the center, right is positive
c = 1     # friction coefficient

#------------------------------------------------------------------------------#

# initialize environment
env = dualrotorEnv(m, x, c)  
env.reset()

#------------------------------------------------------------------------------#

# load model
models_path= f"{models_dir}/{end_step}.zip"
model = PPO.load(models_path, env = env)

#------------------------------------------------------------------------------#

# train and save
for i in range(episodes):
    obs = env.reset()
    done = False
    time = 0
    while not done and time < 1000:
        env.render()
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)
        time += 1

env.close()