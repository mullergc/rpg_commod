

def introScene():
    difficulty = ["easy", "normal", "hard"]
    print(
        "Choose your difficulty for the game")
    userInput = ""
    while userInput not in difficulty:
        print("Options: easy/normal/hard")
        userInput = input()
        if userInput == "easy":
            res = 400
            choices_gov(res)
        elif userInput == "normal":
            res = 200
            choices_gov(res)
        elif userInput == "hard":
            res = 100
            choices_gov(res)
        else:
            print("Please enter a valid option.")

def choices_gov(res):
    print("You have this amount to manage:" + str(res) + ".")
    print("How much you will give to primary care? (0-100%)")
        userInput = ""
    print("How much you will give to Hospital? (0-100%)")
        userInput2 = ""
    print("How much you will give to Hospital? (0-100%)")
    print("How much you will give to Hospital? (0-100%)")
        userInput3 = ""

primcare = res * userInput
        hospital = res * userInput2

if __name__ == "__main__":
    while True:
        print("Welcome to the ComMod RPG Game!")
        print("You are choose to play this game about managing an pandemic scenario")
        print("Let's start with the name of your country: ")
        name = input()
        print("Welcome to, " + name + ".")
        introScene()
