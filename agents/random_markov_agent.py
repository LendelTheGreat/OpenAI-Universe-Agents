#!/usr/bin/env python
import gym
import numpy as np
import math
from PIL import Image
import json
import universe
from universe.spaces import vnc_event
from universe import wrappers
from random import randint

def create_mouse_circle_actions(n_actions, offset=(0, 0), action_range=100):
    step = 2 * math.pi / n_actions
    xy_points = [(lambda i: (offset[0]+round(action_range*math.sin(step*i)), offset[1]+round(action_range*math.cos(step*i))))(i) for i in xrange(n_actions)]
    return [(lambda (x, y): [vnc_event.PointerEvent(x, y, 0)])((x, y)) for (x, y) in xy_points]


env = gym.make('internet.SlitherIO-v0')
env.configure(remotes='vnc://localhost:5900+15900')
observation_n = env.reset()

reg = universe.runtime_spec('flashgames').server_registry
off_h = 86
off_w = 20
h = reg['internet.SlitherIO-v0']['height']
w = reg['internet.SlitherIO-v0']['width']

n_actions = 16
actions = create_mouse_circle_actions(n_actions=16, offset=(270, 239))
action = 0

obs = np.asarray([0])
r = 0
vis = True

while True:
    r = randint(1, 100)
    if r >= 80 and r <= 90:
        action = (action + 1) % n_actions
    elif r >= 91:
        action = (action - 1) % n_actions

    action_n = [actions[action] for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)

    if len(observation_n) >= 1 and observation_n[0]:
        obs = np.asarray(observation_n[0]["vision"])
        obs = obs[off_h:off_h+h, off_w:off_w+w, :]
        r = reward_n[0]
        if vis:
            img = Image.fromarray(obs, 'RGB')
            img.save('my.png')
            img.show()
            vis = False


    print '######################################################'
    #print 'Observation: '+str(obs)
    print 'Reward: '+str(r)
    print 'Done: '+str(done_n)
    #print 'Info: '+str(info)

    env.render()
