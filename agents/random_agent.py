#!/usr/bin/env python
import gym
import universe  # register the universe environments
from universe import wrappers
from random import randint

env = gym.make('internet.SlitherIO-v0')
env.configure(remotes='vnc://localhost:5900+15900')
env = wrappers.experimental.SafeActionSpace(env)
observation_n = env.reset()

actions = [('KeyEvent', 'left', True), ('KeyEvent', 'right', True), ('KeyEvent', 'up', True)]

while True:
    action_n = [[sample_action()] for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()

def sample_action():
    return actions[randint(0, len(actions)-1)]
