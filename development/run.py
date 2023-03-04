import game_v1 as game
#game.round_1()

#pct_pop, media, res_pop, box = game.round_1()

def new_function(res_pop):
    # do something with the passed arguments
    print(f"The hospital has {res_pop}")
        #beds, {box} icu units and {media_talk} units")
    #print(f"The population is {res_pop}")

# call round_1() and store the return values into variables
result = game.round_1()
pop = result['res_pop']
# call the new function and pass in the stored variables from round_1()
new_function(pop)
