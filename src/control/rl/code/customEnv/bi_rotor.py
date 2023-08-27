import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from os import path


class dualrotorEnv(gym.Env):
    metadata = {"render.modes": ["human", "rgb_array"], "video.frames_per_second": 30}

    # extra mass, location of extra mass, friction coefficient
    def __init__(self, m, x, c):
        self.max_speed = 8
        self.max_dT= 4.0
        self.dt = 0.01
        self.j = 0.022 + m*(x**2)
        self.c = c
        self.m = m
        self.x = x
        self.viewer = None

        high = np.array([1.0, self.max_speed], dtype=np.float32)
        self.action_space = spaces.Box(
            low=-self.max_dT, high=self.max_dT, shape=(1,), dtype=np.float32
        )
        self.observation_space = spaces.Box(low=-high, high=high, dtype=np.float32)

        self.seed()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, u):
        self.state = self.obs(u, self.state[0], self.state[1])
        
        # cost function
        # self.cost = 0.9*self.cost + (self.state[0]**2)*self.dt
        self.cost += 0.05*(self.state[0]**2)*self.dt

        self.reward = -self.cost - self.state[1]**2 + 10

        if  self.state[0] > np.pi/3 or self.state[0] < -np.pi/3:
            self.cost = 0
            self.done = True
            self.reward -= 50

        return self.state, self.reward, self.done, {}

    def reset(self):
        self.done = False
        self.reward = -9999
        self.cost = 0
        high = np.array([np.pi/4, 1])
        self.state = self.np_random.uniform(low=-high, high=high)
        return self.state

    def obs(self, u, th, thdot):        
        c = self.c
        j = self.j
        dt = self.dt

        # saturation
        u = np.clip(u, -self.max_dT, self.max_dT)[0]

        # state space
        newthdot = thdot + (u - 0.05*c*thdot - self.m*self.x)/j * dt
        newthdot = np.clip(newthdot, -self.max_speed, self.max_speed)
        newth = th + newthdot * dt
        
        return np.array([newth, newthdot], dtype=np.float32)

    def render(self, mode="human"):
        if self.viewer is None:
            from gym.envs.classic_control import rendering

            l, r, t, b = 0, 2, 0.1, -0.1

            self.viewer = rendering.Viewer(500, 500)
            self.viewer.set_bounds(-2.2, 2.2, -2.2, 2.2)
            rod1 = rendering.make_polygon([(l, b), (l, t), (r, t), (r, b)])
            rod1.set_color(0.4, 0.4, 0.8)
            self.transform = rendering.Transform()
            rod1.add_attr(self.transform)
            self.viewer.add_geom(rod1)

            l = -r
            r = 0
            
            rod2 = rendering.make_polygon([(l, b), (l, t), (r, t), (r, b)])
            rod2.set_color(0.4, 0.4, 0.8)
            rod2.add_attr(self.transform)
            self.viewer.add_geom(rod2)

            l, r, t, b = 2*self.x/0.25 + 0.15, 2*self.x/0.25 - 0.15, 0.1, 0.3

            box = rendering.make_polygon([(l, b), (l, t), (r, t), (r, b)])
            box.set_color(0.9, 0.3, 0.3)
            box.add_attr(self.transform)
            self.viewer.add_geom(box)

            axle = rendering.make_circle(0.05)
            axle.set_color(0, 0, 0)
            self.viewer.add_geom(axle)

        self.transform.set_rotation(self.state[0])

        return self.viewer.render(return_rgb_array=mode == "rgb_array")

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None
