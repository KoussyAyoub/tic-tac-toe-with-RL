import time
import math
class MDP:
    def __init__(self):
        self.states = []
        for i in range(512):
            for j in range(512):
                binary_i = bin(i)[2:].zfill(9)
                binary_j = bin(j)[2:].zfill(9)
                state = (binary_i, binary_j)

                # Vérifier si au moins un 1 occupe la même position dans les deux chaînes
                if not any(bit_i == '1' and bit_j == '1' for bit_i, bit_j in zip(binary_i, binary_j)):
                    # Vérifier si la différence d'occurrence de 1 est égale à 1
                    count_1_i = binary_i.count('1')
                    count_1_j = binary_j.count('1')
                    if (count_1_i - count_1_j == 0 ) :
                        self.states.append(state)
        
        
    def get_transition_probabilities(self ,state, new_state, action):
        # s is the current state
        # a is the action
        # s_ is the next state
        # return the probability of going from state s to state s_ when taking action a
        # if s_ is not allowed return 0
        # if s_ is allowed return 1/len(self.Env.allowed_place)
        # check if taking action a from state s results in state s_
        s =  int(state[0], 2) | int(state[1], 2)
        s_ = int(new_state[0], 2) | int(new_state[1], 2)
        # nb_allowed_place = nb de 0 dans bin(s)[2:].zfill(9) avec s = int(state[0], 2) | int(state[1], 2)
        new_state = bin(s_)[2:].zfill(9)
        state = bin(s)[2:].zfill(9)
        if s & (1 << action) == 0 and s_ & (1 << action) != 0 and new_state.count('1') == state.count('1') + 2 :
            nb_allowed_place = 9 - (state[0].count('1') + state[1].count('1'))
            return 1/nb_allowed_place
        else:
            return 0
        


    def check_winner(self , state):
        # check rows
        s = int(state, 2)
        for row in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            if all((1 << i) & s for i in row):
                return True
            
            
        # check columns
        for col in [[0, 3, 6], [1, 4, 7], [2, 5, 8]]:
            if all((1 << i) & s for i in col):
                return True
            
        # check diagonals
        for dig in [[0, 4, 8], [2, 4, 6]]:
            if all((1 << i) & s for i in dig):
                return True
        
        # no winner
        return False
        
    def get_reward(self ,state, new_state, action):
        # s is the current state
        # a is the action
        # s_ is the next state
        # return the reward of going from state s to state s_ when taking action a
        # if s_ is not allowed return -1
        # if s_ is allowed return 0
        # check if taking action a from state s results in state s_
        if self.get_transition_probabilities(state, new_state, action) == 0 :
            return 0
        else :
            if self.check_winner(new_state[0]):
                return 2
            elif self.check_winner(new_state[1]):
                return -1
            else :
                return -0.001
            
            
            
    
    def value_iteration(self, discount_factor=0.2, epsilon=1e-4, max_iterations=10):
        # Initialize the value function and policy for all states
        V = {state: 0 for state in self.states}
        policy = {state: None for state in self.states}
        
        for i in range(max_iterations):
            delta = 0
            # Update the value function and policy for each state
            for state in self.states:
                old_value = V[state]
                new_value = 0 #float('-inf')
                best_action = None

                # Calculate the maximum expected value for each action
                for action in range(9):
                    if (int(state[0], 2) & (1 << action) == 0) and (int(state[1], 2) & (1 << action) == 0):
                        action_value = 0
                        for new_state in self.states:
                            transition_prob = self.get_transition_probabilities(state, new_state, action)
                            reward = self.get_reward(state, new_state, action)
                            action_value += transition_prob * (reward + discount_factor * V[new_state])
                                        
                        if action_value > new_value:
                            #print(f"action value : {action_value} old_value : {old_value} best_action : {best_action} action : {action}")
                            new_value = action_value
                            best_action = action


                # Update the value function and policy for the current state
                V[state] = new_value
                policy[state] = best_action
                delta = max(delta, abs(old_value - new_value))

            # Print the progress of the algorithm
            print(f"Iteration {i+1}: delta = {delta:.6f}")

            # Check for convergence
            if delta < epsilon:
                break

        return V, policy
    

            
class Main():
    # create the environment
    MDP = MDP()
    V , policy = MDP.value_iteration()
    #save the policy in format to read it as dic in python
    with open('tp1/policy.txt', 'w') as f:
        for key, value in policy.items():
            f.write('%s:%s\n' % (key, value))
    #save the V in format to read it as dic in python
    with open('tp1/V.txt', 'w') as f:
        for key, value in V.items():
            f.write('%s:%s\n' % (key, value))

    print("policy and V saved in files")