

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
    print("How much you will give to Primary care (first) Hospital (second) and Media ? (0-100%)")
        x, y, z = input("Enter three values: ").split()

        userInput = int(x)
        userInput2 = int(y)
        userInput3 = int(z)

    if (userInput + userInput2 + userInput3) > 100:
         print("Please enter a valid option.")
    else:
        primcare = int(res) * userInput
        hospital = int(res) * userInput2
        icu = int(res) * userInput3

if __name__ == "__main__":
    while True:
        print("Welcome to the ComMod RPG Game!")
        print("You are choose to play this game about managing an pandemic scenario")
        print("Let's start with the name of your country: ")
        name = input()
        print("Welcome to, " + name + ".")
        introScene()
