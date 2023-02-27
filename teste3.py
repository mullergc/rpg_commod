if __name__ == "__main__":
    while True:
        print("Welcome to the Adventure Game!")
        print("As an avid traveler, you have decided to visit the Catacombs of Paris.")
        print("However, during your exploration, you find yourself lost.")
        print("You can choose to walk in multiple directions to find a way out.")
        print("Let's start with your name: ")
        name = input()
        print("Good luck, " +name+ ".")
        introScene()

def introScene():
    directions = ["left","right","forward"]
    print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/backward/forward")
        userInput = input()
        if userInput == "left":
        showShadowFigure()
    elif userInput == "right":
      showSkeletons()
    elif userInput == "forward":
      hauntedRoom()
                elif userInput == "backward":
      print("You find that this door opens into a wall.")
    else:
      print("Please enter a valid option.")