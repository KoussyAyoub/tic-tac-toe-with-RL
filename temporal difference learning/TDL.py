import re
import random
import ast
class Agent:
    def __init__(self, name ,  path_policy , epsilon = 0.1):
        self.epsilon = epsilon
        self.name = name
        self.positions = []
        self.reward = 0
        self.policy = {}
        self.filename = path_policy
        # read the dic from the filepath into the variable policy 
        with open(self.filename) as fp:
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
        #self.policy = {tuple(reversed(key)): value for key, value in self.policy.items()}



    def chose_action(self, env):
        key = list(self.policy.keys())[0]
        if self.policy[env.status] != None :
            if random.random() <= 1 - self.epsilon:
                action = self.policy[env.status]
            else:
                j = int(env.status[0], 2) | int(env.status[1], 2)
                global_status = bin(j)[2:].zfill(9)
                allowed_place = [ 8-i for i in range(9) if global_status[i] == '0']
                # chose radnom place 
                action = random.choice(allowed_place)
        else : 
            j = int(env.status[0], 2) | int(env.status[1], 2)
            global_status = bin(j)[2:].zfill(9)
            allowed_place = [ 8-i for i in range(9) if global_status[i] == '0']
            # chose radnom place 
            action = random.choice(allowed_place)

        i = int(env.status[0], 2) | (1 << action)
        env.status = ( bin(i)[2:].zfill(9), env.status[1])
        return action



class Env:
    def __init__(self, Agent):
        self.status = (bin(0)[2:].zfill(9) , bin(0)[2:].zfill(9))        
        self.current_winner = None # keep track of winner!
        self.Agent = Agent
        
    
        
    def check_winner(self , status):
        # check rows
        s = [int(status[0], 2) , int(status[1], 2)]
        for row in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            if all((1 << i) & s[0] for i in row):
                return "Agent"
            if all((1 << i) & s[1] for i in row):
                return "Human"
        
        # check columns
        for col in [[0, 3, 6], [1, 4, 7], [2, 5, 8]]:
            if all((1 << i) & s[0] for i in col):
                return "Agent"
            if all((1 << i) & s[1] for i in col):
                return "Human"
        
        # check diagonals
        for dig in [[0, 4, 8], [2, 4, 6]]:
            if all((1 << i) & s[0] for i in dig):
                return "Agent"
            if all((1 << i) & s[1] for i in dig):
                return "Human"
    
        # no winner
        return None
    
    def reward(self, status):
        if self.check_winner(status) == "Agent":
            return -2
        elif self.check_winner(status) == "Human":
            return 4
        else :
            return -0.1

class TDL :
    def __init__(self , path_policy) :
        self.path_policy = path_policy
        self.policy = Agent("Agent" ,path_policy = self.path_policy , epsilon = 0.1).policy
        self.states = list(self.policy.keys())
    
    def Sarsa(self, nb_episodes ,alpha = 0.1 , gamma = 0.9) :
        Q = {state: {action: 0 for action in [ 8-i for i in range(9) if bin(int(state[0], 2) | int(state[1], 2))[2:].zfill(9)[i] == '0']} for state in self.states}
        for state in Q:
            if not Q[state]:
                Q[state][None] = 0

        policy = self.policy

        for k in range(nb_episodes) :
            env = Env(Agent("Agent" , epsilon = 0.1 , path_policy = self.path_policy))
            nb_allowed_place = 9
            while env.check_winner(env.status) == None and nb_allowed_place > 0:
                state = env.status
                action = env.Agent.chose_action(env)
                reward = env.reward(env.status)
                
                j = int(env.status[0], 2) | int(env.status[1], 2)
                global_status = bin(j)[2:].zfill(9)
                allowed_place = [ 8-i for i in range(9) if global_status[i] == '0']
                if len(allowed_place)-1 > 0 :
                    action = random.choice(allowed_place)
                    env.status = ( env.status[0] ,bin(int(env.status[1], 2) | (1 << action))[2:].zfill(9))

                    
                    next_state = env.status
                    next_action = env.Agent.chose_action(env)

                    Q[state][action] = Q[state][action] + alpha * (reward + gamma * Q[next_state][next_action] - Q[state][action])
                    policy[state] = max(Q[state], key=Q[state].get)
                    env.status = next_state


                nb_allowed_place -=2

        return policy
    
    def generate_n_step(self, env , n):
        Status = []
        Rewards = []
        Actions = []
        nb_allowed_place = 9
        i = 0
        while env.check_winner(env.status) == None and nb_allowed_place != 0 and i < n:
            Status.append(env.status)
            action = env.Agent.chose_action(env)
            Actions.append(action)
            Rewards.append(env.reward(env.status))

            j = int(env.status[0], 2) | int(env.status[1], 2)
            global_status = bin(j)[2:].zfill(9)
            allowed_place = [ 8-i for i in range(9) if global_status[i] == '0']
            if len(allowed_place) != 0 :
                action = random.choice(allowed_place)
                env.status = ( env.status[0] ,bin(int(env.status[1], 2) | (1 << action))[2:].zfill(9))
                
            
            s =  int(env.status[0], 2) | int(env.status[1], 2)
            nb_allowed_place = bin(s)[2:].zfill(9).count('0')
            i += 1

        if env.check_winner(env.status) != None  or nb_allowed_place == 0 :
            game_over = True
        else :
            game_over = False
        return Status , Rewards , Actions , game_over


    def Sarsa_n(self , nb_episodes ,alpha = 0.1 , gamma = 0.9 , n = 1) :
        Q = {state: {action: 0 for action in [ 8-i for i in range(9) if bin(int(state[0], 2) | int(state[1], 2))[2:].zfill(9)[i] == '0']} for state in self.states}
        for state in Q:
            if not Q[state]:
                Q[state][None] = 0

        policy = self.policy
        for k in range(nb_episodes) :
            game_over = False
            env = Env(Agent("Agent" , epsilon = 0.1 , path_policy = self.path_policy))
            while not game_over :
                Status , Rewards , Actions , game_over = self.generate_n_step(env , n)
                G = 0
                for t in range(len(Status)-1 , -1 , -1) :
                    G = gamma * G + Rewards[t]
                    Q[Status[t]][Actions[t]] = Q[Status[t]][Actions[t]] + alpha * (G - Q[Status[t]][Actions[t]])
                    policy[Status[t]] = max(Q[Status[t]], key=Q[Status[t]].get)

        return policy

        
        
                    
                    

    



class Main : 
    path = r"C:\Users\DELL\Desktop\naoum\tp2\policy_MCP_Exploring_Starts.txt"
    TDL = TDL(path)
    policy = TDL.Sarsa_n(1000 , n = 3)
    ancien_policy = Agent("Agent" , path_policy = path).policy

    # check if the new policy is modified or not
    for key in policy :
        if policy[key] != ancien_policy[key] :
            print("policy changed")
            break

    # write the new policy in the file
    with open("policy_TDL_Sarsa_n.txt", "w") as file:
        for key, value in policy.items():
            file.write(f"{key}: {value}\n")

    print('done')

                
                
                

