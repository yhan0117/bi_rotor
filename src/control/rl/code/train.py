import gym
from stable_baselines3 import A2C, PPO
from customEnv.bi_rotor import dualrotorEnv
import os

#------------------------------------------------------------------------------#

# model directory on local computer
models_dir = "models/DualRotor/Integral"

# log directory on Tensorboard
logdir = "logs/drotor/int"

# log name to be plotted on Tensorboard
log_name = "PPO"

# starting point from where we keep training (0 if its a new train)
end_step = 100000  

# parameters 
steps = 10000
episodes = 60
m = 5       # added mass in kg, could be the battery
x = 0.2     # m from the center, right is positive
c = 1       # friction coefficient

#------------------------------------------------------------------------------#

# load past training data
# or create new directories if they do not exist (new train)
if os.path.exists(models_dir):
    models_path = f"{models_dir}/{end_step}.zip"
else:
    models_path = None
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

#------------------------------------------------------------------------------#

# initialize environment
'''
To use gym enviroments
call gym.make("name_of_env")
'''
env = dualrotorEnv(m, x, c)  
env.reset()

#------------------------------------------------------------------------------#

# Rl algo
'''
To switch to anothe algorithm 
keep the arguments and call, for example, A2C(same_arguments)
'''
if models_path != None:
    model = PPO.load(models_path, env = env, tensorboard_log = logdir)
else:
    model = PPO("MlpPolicy", env, verbose = 1, tensorboard_log = logdir)

#------------------------------------------------------------------------------#

# train and save
for i in range(episodes):
    # reset enviroment at the start of each episode
    obs = env.reset()

    # train for specified number of timesteps
    model.learn(total_timesteps = steps, reset_num_timesteps = False, tb_log_name = log_name)

    # save training data
    model.save(f"{models_dir}/{end_step+steps*(i+1)}")
    
env.close()