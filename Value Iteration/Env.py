import Human
import Agent
class Env:
    def __init__(self, Human, Agent):
        self.status = (bin(0)[2:].zfill(9) , bin(0)[2:].zfill(9))        
        self.current_winner = None # keep track of winner!
        self.Human = Human
        self.Agent = Agent
        

    @staticmethod
    def print_board_nums(self):
        # 0 | 1 | 2 etc (tells us what number corresponds to what box) use self.status (00000000,00000000)
        for row in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            print("|", end = "")
            for col in row:
                if (1 << col) & int(self.status[0], 2) != 0:
                    print("X", end = "")
                elif (1 << col) & int(self.status[1], 2) != 0:
                    print("O", end = "")
                else:
                    print(col, end = "")
                print("|", end = "")
            print()
        
        
        
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
        
        

    def play_game(self):
        # loop until someone wins or its a tie
        s =  int(self.status[0], 2) | int(self.status[1], 2)
        allowed_place = bin(s)[2:].zfill(9).count('0')
        while allowed_place > 0 and self.current_winner == None :
            self.Agent.chose_action(self)
            self.current_winner = self.check_winner(self.status)
            s =  int(self.status[0], 2) | int(self.status[1], 2)
            allowed_place = bin(s)[2:].zfill(9).count('0')
            self.print_board_nums(self)
            if allowed_place != 0 and self.current_winner == None :
                self.Human.chose_action(self)
                self.current_winner = self.check_winner(self.status)
                s =  int(self.status[0], 2) | int(self.status[1], 2)
                allowed_place = bin(s)[2:].zfill(9).count('0')
            else :
                break

        if self.current_winner != None:
            print(self.current_winner + " wins")
        else :
            print("tie")
        print("game over")


class Main :
    Env = Env(Human.Human("Human"), Agent.Agent("Agent"))
    Env.play_game()
