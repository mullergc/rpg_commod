class start:
    def __init__(self):
        self.name = 0
        self.pop = 0
        self.res = 0
        self.difficulty = "easy"
    def choose_pop(self,name_input,pop_input):
        val = int(pop_input)
        if val > 1000:
          print("Invalid input, please choose less than 1000 people")
        elif val == 0:
           print("Invalid input, please choose greater than 0 people")
        else:
           print(f'Welcome to country of {name_input},with a pop of {val}')

    def choose_level(self,level):
        if level.lower() == 'easy':
            self.res = 200
        elif level.lower() == 'normal':
            self.res = 100
        elif level.lower() == 'hard':
            self.res = 50
        else:
            print("Invalid input, please choose [EASY/NORMAL/HARD]")
            self.choose_level()
