import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from os import path


class dualrotorEnv(gym.Env):
    metadata = {"render.modes": ["human", "rgb_array"], "video.frames_per_second": 30}

    def __init__(self):
        '''
        Parameters:
        min_PWM
        max_PWM
        O
        km
        J
        '''

        '''
        Inputs:
        kp
        ki
        kd
        '''

        '''
        Observation:
        x, u
        '''

        self.min_PWM = 1100
        self.max_PWM= 1400
        self.dt = 0.05
        self.O = 1300
        self.J = 0.022
        self.viewer = None

        high = np.array([1.0, 1.0, self.max_speed], dtype=np.float32)
        self.action_space = spaces.Box(
            low=-self.max_dT, high=self.max_dT, shape=(1,), dtype=np.float32
        )
        self.observation_space = spaces.Box(low=-high, high=high, dtype=np.float32)

        self.seed()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, u):
        th, thdot = self.state  # th := theta

        g = self.g
        j = self.j
        l = self.l
        dt = self.dt

        # saturation
        u = np.clip(u, -self.max_dT, self.max_dT)[0]

        # state space
        newthdot = thdot + u/j * dt
        newthdot = np.clip(newthdot, -self.max_speed, self.max_speed)
        newth = th + newthdot * dt
        
        self.state = np.array([newth, newthdot])

        # cost function
        cost = self.state[0]**2 + (self.state[1]**2)/8
        self.reward = -cost + 1

        if  self.state[0] > np.pi/3 or  self.state[0] < -np.pi/3:
            self.done = True
            self.reward -= 2

        return self._get_obs(), self.reward, self.done, {}

    def reset(self):
        self.done = False
        self.reward = -9999
        high = np.array([np.pi, 1])
        self.state = self.np_random.uniform(low=-high, high=high)
        return self._get_obs()

    def _get_obs(self):
        theta, thetadot = self.state
        return np.array([theta, thetadot], dtype=np.float32)

    def render(self, mode="human"):
        if self.viewer is None:
            from gym.envs.classic_control import rendering

            l, r, t, b = 0, 2, 0.1, -0.1

            self.viewer = rendering.Viewer(500, 500)
            self.viewer.set_bounds(-2.2, 2.2, -2.2, 2.2)
            rod1 = rendering.make_polygon([(l, b), (l, t), (r, t), (r, b)])
            rod1.set_color(0.4, 0.4, 0.8)
            self.rod1_transform = rendering.Transform()
            rod1.add_attr(self.rod1_transform)
            self.viewer.add_geom(rod1)

            l = -r
            r = 0
            
            rod2 = rendering.make_polygon([(l, b), (l, t), (r, t), (r, b)])
            rod2.set_color(0.4, 0.4, 0.8)
            self.rod2_transform = rendering.Transform()
            rod2.add_attr(self.rod2_transform)
            self.viewer.add_geom(rod2)

            axle = rendering.make_circle(0.05)
            axle.set_color(0, 0, 0)
            self.viewer.add_geom(axle)

        self.rod1_transform.set_rotation(self.state[0])
        self.rod2_transform.set_rotation(self.state[0])

        return self.viewer.render(return_rgb_array=mode == "rgb_array")

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None
