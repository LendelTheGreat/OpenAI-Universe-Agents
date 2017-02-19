#!/usr/bin/env python
from random import randint

class RandomAgent(object):

    def __init__(self, actions):
        self.actions = actions
        self.n_actions = len(actions)

    def __call__(self, observation, reward, done):
        return self.actions[randint(0, self.n_actions-1)]
