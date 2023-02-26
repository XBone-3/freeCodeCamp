import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)
    
    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        balls = []
        for _ in range(number):
            choice = random.randrange(len(self.contents))
            balls.append(self.contents.pop(choice))
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    no_of_expected_balls = []
    for key in expected_balls:
        no_of_expected_balls.append(expected_balls[key])

    positive_experiments = 0
    for _ in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        balls = copy_hat.draw(num_balls_drawn)
        no_of_balls = []

        for key in expected_balls:
            no_of_balls.append(balls.count(key))

        if no_of_balls >= no_of_expected_balls:
            positive_experiments += 1
    return positive_experiments/num_experiments
