class Human:
    def __init__(self, name):
        self.name = name

    def chose_action(self, env):
        # chose a random number from the allowed places
        while True:
            action = int(input("take a place from the allowed places: "))
            i = int(env.status[0], 2) | int(env.status[1], 2)
            global_status = bin(i)[2:].zfill(9)
            allowed_place = [ 8-i for i in range(9) if global_status[i] == '0']
            if action in allowed_place:
                break
            else:
                print("this place is not allowed, try again")
        i = int(env.status[1], 2) | (1 << action)
        env.status = (env.status[0] , bin(i)[2:].zfill(9) )







    
