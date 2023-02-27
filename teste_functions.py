
# ***Clear the screen function***
def clear_screen():
    """
    This function will clear the screen
    """
    sleep(2)
    os.system('cls')

# function for making the illusion of typing on every print
def typing(message):
    print("")
    #print(message) # Eliminate this after testing...
    for word in message:
        time.sleep(random.choice([0.3, 0.11, 0.08, 0.07,   0.07, 0.07, 0.06, 0.06, 0.05, 0.01]))
        sys.stdout.write(word)
        sys.stdout.flush()
    time.sleep(.1)
    return ""

def choose_dif():
    global res
    typing('Type "1" for first option, and "2" for the second option')
    a = int(input(typing("Difficulty (1) Easy, (2) Normal and (3) Hard: ")))
    while a != 1 and a != 2:
        typing(f"{a} is not either '1' or '2' or '3'... invalid option\n")
        m1 = typing("Difficulty (1) Easy, (2) Normal and (3) Hard:  \n")
        a = int(input(m1))

    if a == 1:
        # Strategic path
        res = 400
    elif a == 2:
        # Normal
        res = 200
    elif a == 3:
        #Hard
        res=100
    return(res)