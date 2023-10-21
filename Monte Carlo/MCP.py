import re
import random
import ast
class Agent:
    def __init__(self, name , policy_file):
        self.name = name
        self.positions = []
        self.reward = 0
        self.policy = {}
        # read the dic from the filepath into the variable policy 
        with open(policy_file) as fp:
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
            action = self.policy[env.status]
        else : 
            j = int(env.status[0], 2) | int(env.status[1], 2)
            global_status = bin(j)[2:].zfill(9)
            allowed_place = [ 8-i for i in range(9) if global_status[i] == '0']
            # chose radnom place 
            action = random.choice(allowed_place)

        i = int(env.status[0], 2) | (1 << action)
        env.status = (bin(i)[2:].zfill(9) , env.status[1])
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
        

    




    
class MCP :
    def __init__(self , policy) :
        self.policy = policy
        self.states = Agent("Agent" , self.policy).policy.keys()
    
    def generate_episode(self, env):
        Status = []
        Rewards = []
        Actions = []
        nb_allowed_place = 9
        while env.check_winner(env.status) == None and nb_allowed_place != 0:
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

        return Status , Rewards , Actions

        
        
    def First_visit_Monte_Carlo_prediction(self, n_episodes):
        N = {state: 0 for state in self.states}
        Returns = {state: 0 for state in self.states}
        V = {state: None for state in self.states}

        for i in range(n_episodes) :
            env = Env(Agent("Agent" , self.policy))
            Status , Rewards , Actions = self.generate_episode(env)
            G = 0
            for t in range(len(Status)-1 , -1 , -1) :
                G = Rewards[t] + G
                if Status[t] not in Status[:t] :
                    N[Status[t]] += 1
                    Returns[Status[t]] += G

        V = {state: Returns[state]/N[state] if N[state] != 0 else 0 for state in self.states}
            
            

    def On_policy_first_visit_Monte_Carlo_Exploring_Starts(self, n_episodes , gamma = 0.9) :
        policy = Agent("Agent" , self.policy).policy
        Q = {state: {action: 0 for action in [ 8-i for i in range(9) if bin(int(state[0], 2) | int(state[1], 2))[2:].zfill(9)[i] == '0']} for state in self.states}
        for state in Q:
            if not Q[state]:
                Q[state][None] = 0
        
        Returns = {state: {action: [] for action in Q[state].keys()} for state in self.states}
        for episode in range(n_episodes) :
            env = Env(Agent("Agent" , self.policy))
            Status , Rewards , Actions = self.generate_episode(env)
            G = 0
            for t in range(len(Status)-1 , -1 , -1) :
                G = gamma * Rewards[t] + G
                if Status[t] not in Status[:t] :
                    Returns[Status[t]][Actions[t]].append(G)
                    Q[Status[t]][Actions[t]] = sum(Returns[Status[t]][Actions[t]]) / len(Returns[Status[t]][Actions[t]])
                    policy[Status[t]] = max(Q[Status[t]], key=Q[Status[t]].get)

        policy = {tuple(reversed(key)): value for key, value in policy.items()}
        return policy
    
    def On_policy_first_visit_Monte_Carlo_control_epsilon_greedy(self, n_episodes , gamma = 0.9 , epsilon = 0.1) :
        policy = Agent("Agent" , self.policy).policy
        Q = {state: {action: 0 for action in [ 8-i for i in range(9) if bin(int(state[0], 2) | int(state[1], 2))[2:].zfill(9)[i] == '0']} for state in self.states}
        for state in Q:
            if not Q[state]:
                Q[state][None] = 0
        
        Returns = {state: {action: [] for action in Q[state].keys()} for state in self.states}
        for episode in range(n_episodes) :
            env = Env(Agent("Agent" , self.policy))
            Status , Rewards , Actions = self.generate_episode(env)
            G = 0
            for t in range(len(Status)-1 , -1 , -1) :
                G = gamma * Rewards[t] + G
                if Status[t] not in Status[:t] :
                    Returns[Status[t]][Actions[t]].append(G)
                    Q[Status[t]][Actions[t]] = sum(Returns[Status[t]][Actions[t]]) / len(Returns[Status[t]][Actions[t]])
                    policy[Status[t]] = max(Q[Status[t]], key=Q[Status[t]].get) if random.random() > 1-epsilon else random.choice(list(Q[Status[t]].keys()))

        policy = {tuple(reversed(key)): value for key, value in policy.items()}
        return policy
    
    

                    
        




            

            



class Main :
    MCP = MCP("policy.txt")
    Policy = MCP.On_policy_first_visit_Monte_Carlo_Exploring_Starts(5000)
    # chek if there is any change in the value of the policy and Agent.policy and print true if there is change and false if not
    for key, value in Policy.items():
        if value != Agent("Agent" , "policy.txt").policy[key]:
            print("true")
            break
    else:
        print("false")


    
    # save the policy in format to read it as dictionary
    with open("policy_MCP.txt", "w") as file:
        for key, value in Policy.items():
            file.write(f"{key}: {value}\n")

    
    
    print("policy saved in policy_MCP.txt")
    
        
        
        