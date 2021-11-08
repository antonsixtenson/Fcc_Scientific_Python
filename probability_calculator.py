import random
import copy as cp

class Hat:
    def __init__(self, **values):
        self.contents = []
        for key, value in values.items():
            for i in range(value):
                self.contents.append(key)

    def draw_balls(self, n):
        if n >=len(self.contents):
            return self.contents
        else:
            drawn = []
            for i in range(n):
                drawn.append(self.contents.pop(random.randint(0, len(self.contents)-1)))
            return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_matches = 0
    for i in range(num_experiments):
        match = True
        temphat = cp.deepcopy(hat)
        drawn = temphat.draw_balls(num_balls_drawn)
        for key, value in expected_balls.items():
            if drawn.count(key) < value:
                match = False
                break
        if match:
            num_matches += 1
    return num_matches/num_experiments
