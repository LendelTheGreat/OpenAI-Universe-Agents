#!/usr/bin/env python
from random import randint

class RandomAgent(object):

    def __init__(self, actions):
        self.actions = actions

    def __call__(self, observation, reward, done):
        return actions[randint(0, len(actions)-1)]
