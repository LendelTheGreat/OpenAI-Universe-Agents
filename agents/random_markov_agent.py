#!/usr/bin/env python
from random import randint

class MarkovAgent(object):

    def __init__(self, actions, randomness=40):
        self.actions = actions
        self.last_action = 0
        self.n_actions = len(actions)

        self.randomness = randomness

    def __call__(self, observation, reward, done):
        r = randint(1, 100)
        if r >= (100-self.randomness) and r <= (100-self.randomness/2):
            action = (self.last_action + 1) % self.n_actions
        elif r >= self.randomness/2:
            action = (self.last_action - 1) % self.n_actions
        else:
            action = self.last_action

        self.last_action = action
        return actions[action]
