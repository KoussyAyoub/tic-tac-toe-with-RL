# create agent to play the x and o game
import re
import random
import ast
class Agent:
    def __init__(self, name):
        self.name = name
        self.positions = []
        self.reward = 0
        self.policy = {}
        filename = r"C:\Users\DELL\Desktop\naoum\tp1\policy.txt"
        # read the dic from the filepath into the variable policy 
        with open(filename) as fp:
            line = fp.readline()
            while line:
                line = line.strip()
                key = line.split(":")[0]
                value = line.split(":")[1]
                if value.strip() == "None":
                    value = None
                else:
                    value = int(value)
                self.policy[key] = value
                line = fp.readline()
        self.policy = {ast.literal_eval(key): value for key, value in self.policy.items()}
        self.policy = {tuple(reversed(key)): value for key, value in self.policy.items()}



    def chose_action(self, env):
        key = list(self.policy.keys())[0]
        if self.policy[env.status] != None :
            action = self.policy[env.status]
        else : 
            j = int(env.status[0], 2) | int(env.status[1], 2)
            global_status = bin(j)[2:].zfill(9)
            allowed_place = [ 8-i for i in range(9) if global_status[i] == '0']
            # chose radnom place 
            action = random.choice(allowed_place)

        i = int(env.status[0], 2) | (1 << action)
        env.status = ( bin(i)[2:].zfill(9), env.status[1])



