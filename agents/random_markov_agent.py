#!/usr/bin/env python
import gym
import universe  # register the universe environments
from universe import wrappers
from random import randint

env = gym.make('internet.SlitherIO-v0')
env.configure(remotes='vnc://localhost:5900+15900')
env = wrappers.experimental.SafeActionSpace(env)
observation_n = env.reset()

actions = [
    [('KeyEvent', 'left', True), ('KeyEvent', 'right', False)],
    [('KeyEvent', 'left', False), ('KeyEvent', 'right', True)],
    [('KeyEvent', 'left', False), ('KeyEvent', 'right', False)]
]

action = 0
r = 0

while True:
    r += 1
    if r % 500 == 0:
        if randint(0, 1) == 0:
            action = (action + 1) % 3
        else:
            action = (action - 1) % 3

    action_n = [actions[action] for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()
