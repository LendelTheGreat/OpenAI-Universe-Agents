#!/usr/bin/env python
import gym
import universe  # register the universe environments
from universe import wrappers

env = gym.make('internet.SlitherIO-v0')
env.configure(remotes='vnc://localhost:5900+15900')
env = wrappers.experimental.SafeActionSpace(env)
observation_n = env.reset()

while True:
  action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
  observation_n, reward_n, done_n, info = env.step(action_n)
  env.render()
