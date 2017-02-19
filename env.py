#!/usr/bin/env python
import gym
import numpy as np
import math
import universe
from universe.spaces import vnc_event
from universe import wrappers

from agents.random_agent import RandomAgent
from agents.random_markov_agent import MarkovAgent

def create_mouse_circle_actions(n_actions, offset=(0, 0), action_range=100):
    step = 2 * math.pi / n_actions
    xy_points = [(lambda i: (offset[0]+round(action_range*math.sin(step*i)), offset[1]+round(action_range*math.cos(step*i))))(i) for i in xrange(n_actions)]
    return [(lambda (x, y): [vnc_event.PointerEvent(x, y, 0)])((x, y)) for (x, y) in xy_points]

# Setup the environment
env = gym.make('internet.SlitherIO-v0')
env.configure(remotes='vnc://localhost:5900+15900')
observation_n = env.reset()
reward_n = [0] * env.n
done_n = [False] * env.n

# Get input dimensions
reg = universe.runtime_spec('flashgames').server_registry
off_h = 86
off_w = 20
h = reg['internet.SlitherIO-v0']['height']
w = reg['internet.SlitherIO-v0']['width']

# All possible actions
actions = create_mouse_circle_actions(n_actions=16, offset=(270, 239))
action_n = [actions[0]] * env.n

# Get agent
agent = RandomAgent(actions)

# Monitoring
acc_reward = [0] * env.n
episode_length = [0] * env.n

# Main env loop
while True:
    for i in xrange(env.n):
        obs = observation_n[i]
        r = reward_n[i]
        done = done_n[i]

        # Get game pixels from the whole screen
        obs = np.asarray(obs["vision"])
        obs = obs[off_h:off_h+h, off_w:off_w+w, :]

        # Get the action from agent
        action_n[i] = agent(obs, r, done)

        # Reporting
        if not done:
            acc_reward[i] += r
            episode_length[i] += 1
        else:
            print '######################################################'
            print 'Accumulated reward: '+str(acc_reward[i])
            print 'Episode length: '+str(episode_length[i])
            acc_reward[i] = 0
            episode_length[i] = 0

    # Perform the actions, get new observations, render
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()
