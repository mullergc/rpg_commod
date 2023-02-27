import game_functions

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
        return

def choices_gov(res):
    print('GOVERNMENT PLAYER TURN')
    print("You have this amount to manage:" + str(res) + ".")
    print("How much you will give to Primary care (first) Hospital (second) and Media (Third)? (0-100%)")
    x, y, z = input("Enter three values: ").split()

    userInput = int(x)
    userInput2 = int(y)
    userInput3 = int(z)

    if (userInput + userInput2 + userInput3) > 100:
         print("Please enter a valid option.")
    else:
       primcare = userInput
       hospital = userInput2
       media = userInput3
       # primcare = (int(res) * userInput)/2
       # hospital = (int(res) * userInput2)/1
       # icu = (int(res) * userInput3)/4
       choices_hosp(hospital,100)


def choices_hosp(hospital,cases):
    print('HOSPITAL MANAGER TURN')
    print("You have this amount to manage:" + str(hospital) + ".")
    print("How much you will give to ER (first) Infirmary (second) and ICU (Third)? (0-100% - each)")
    a, b, c = input("Enter three values: ").split()
    userInput4 = int(a)
    userInput5 = int(b)
    userInput6 = int(c)

    if (userInput4 + userInput5 + userInput6) > 100 :
        print("Please enter a valid option.")
    else :
        ER = (int(hospital) * userInput4)/2
        Infirmary = (int(hospital) * userInput5)/1
        ICU = (int(hospital) * userInput6)/4
        pandemics = game_functions.dynamics_pandemics(cases)
        result = game_functions.hosp_dynamics(pandemics,ER,Infirmary,ICU)
        return result


if __name__ == "__main__":
    while True:
        print("Welcome to the ComMod RPG Game!")
        print("You are choose to play this game about managing an pandemic scenario")
        print("Let's start with the name of your country: ")
        name = input()
        print("Welcome to, " + name + ".")
        introScene()
       # dataf = game_functions.hosp_dynamics(primcare,hospital,icu)