import random
import string

class Robot:
    def __init__(self):
        self.name = generate_robot_name()

    def reset(self):
        self.__init__()

def generate_robot_name():
    random.seed()
    return ''.join([i + j + k + l + m
        for i in random.choice(string.ascii_uppercase)
        for j in random.choice(string.ascii_uppercase)
        for k in random.choice(string.digits)
        for l in random.choice(string.digits)
        for m in random.choice(string.digits)
        ])
        

            

