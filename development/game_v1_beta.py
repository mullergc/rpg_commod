import first_round_beta as frst
import rounds_beta as rd

def play_game():
    game = "ongoing"
    num_rounds = 12
    round_num = 3

    print("Round 1 of 12")
    round_res = frst.round_1()
    pop = round_res['res_pop']
    init_res = round_res['init_res']
    box = round_res['box']
    media_talk = round_res['media_talk']
    pct_pop = round_res['pct_pop']
    name_media = round_res['name_media']
    name_gov = round_res['name_gov']
    name_hosp = round_res['name_hosp']
    print("Round 2 of 12")
    res = rd.rounds(pop, pct_pop, init_res, box, media_talk, name_media, name_hosp, name_gov)
    pop2 = res['res_pop']
    init_res2 = res['init_res']
    box2 = res['box']
    media_talk2 = res['media_talk']
    pct_pop2 = res['pct_pop']


    while game != "over" and round_num <= num_rounds:
        print(f"Round {round_num} of {num_rounds}")

        name_media = round_res['name_media']
        name_gov = round_res['name_gov']
        name_hosp = round_res['name_hosp']

        if pop2 <= 0:
            print("Game over! Your population has been wiped out.")
            game = "over"
        elif round_num == num_rounds:
            print("Congratulations! You have successfully completed the game.")
            game = "over"
        else:
            round_num += 1
            print(f"Your population is {pop2}. Proceeding to next round...\n")

        # Call rounds function here passing the results of round_1
        res = rd.rounds(pop2, pct_pop2, init_res2, box2, media_talk2, name_media, name_hosp, name_gov)
        pop2 = res['res_pop']
        init_res2 = res['init_res']
        box2 = res['box']
        media_talk2 = res['media_talk']
        pct_pop2 = res['pct_pop']

    return