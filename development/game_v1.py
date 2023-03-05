import first_round as frst
import rounds as rd

def play_game():
    game = "ongoing"
    num_rounds = 12
    round_num = 2

    print("Round 1 of 12")
    round_res = frst.round_1()
    pop = round_res['res_pop']
    init_res = round_res['init_res']
    box = round_res['box']
    media_talk = round_res['media_talk']
    pct_pop = round_res['pct_pop']
    print("Round 2 of 12")
    res = rd.rounds(pop, pct_pop, init_res, box, media_talk)

    while game != "over" and round_num <= num_rounds:
        print(f"Round {round_num} of {num_rounds}")

        pop2 = res['res_pop']
        init_res2 = res['init_res']
        box2 = res['box']
        media_talk2 = res['media_talk']
        pct_pop2 = res['pct_pop']

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
        res = rd.rounds(pop2, pct_pop2, init_res2, box2, media_talk2)

    return