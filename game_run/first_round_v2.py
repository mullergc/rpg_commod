import players_v2 as pl
import pandemics_v2 as pnd

class start:
    def __init__(self):
        self.name = 0
        self.pop = 0
        self.res = 0
        self.difficulty = "easy"

    # Determinando que o valor da população precisa estar entre 0 e 1000
    # name_input = nome do país
    # val = número de pessoas
    #MUDANDO ALGUMA COISA
    def choose_pop(self,name_input,pop_input):
        val = int(pop_input)
        if val > 1000:
          print("Invalid input, please choose less than 1000 people")
        elif val == 0:
           print("Invalid input, please choose greater than 0 people")
        else:
           print(f'Welcome to country of {name_input},with a pop of {val}')

    # Definindo o nível de dificuldade - quantidade de recursos ofertados no início do round
    # level.lower = nível de dificuldade do jogo
    # self.res = quantidade de $
    #---Se o jogador inserir valores inválidos, apresenta mensagem e retorna
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

# Início do jogo | Definindo quando é pl (player) e pnd (pandemic dynamics)
def round_1():
    st = start()
    gov = pl.Government()
    media = pl.Media()
    hospital = pl.Hospital()
    pand = pnd.pandemics_dinamics()

    # Entrada do nome dos 3 jogadores
    # player_gov = nome do governante
    # player_media = nome do representante da mídia
    # player_hosp = nome do administrador do hospital
    player_gov = input("Name of the player government: ")
    player_media = input("Name of the player media: ")
    player_hosp = input("Name of the player hospital: ")

    # Entrada do nome do país, número de pessoas e nível de dificuldade
    # name = nome do país
    # pop = número de pessoas
    # level = nível de dificuldade
    name = input("Name your country: ")
    while True:
        pop = input("Enter your total population (max=1000): ")
        if pop.isdigit():
            break
        else:
            print("Invalid value, please choose an integer.")
            continue
    while True:
        level = input("What level you would like to play? [EASY/NORMAL/HARD] ")
        if (level.lower() == 'easy') or (level.lower() == 'normal') or (level.lower() == 'hard'):
            break
        else:
            print("Please, choose a level.")
            continue

            # Aqui dá um loop infinito no nivel
    # >>>>>>>O que isso faz mesmo?<<<<<<<<
    st.choose_pop(name,pop)
    st.choose_level(level)
    resources = st.res
    pop2 = int(pop)

    # Distribuição de recursos pelo governante
    # media_pct = porcentagem de recursos para a mídia
    # hospital_pct = porcentagem de recursos para o hospital
    # primarycare_pct = porcentagem de recursos para a UBS
    # Definição do nível de isolamento social
    # social_isol = nível de isolamento social (0-100)
    print(f"Governor {player_gov}, you have {resources} to distribute for Media, Hospital and Primary Care")
    media_pct = int(input("Enter percentage of resources for Media: "))
    hospital_pct = int(input("Enter percentage of resources for Hospital: "))
    primarycare_pct = int(input("Enter percentage of resources for Primary Care: "))
    social_isol = input("Define your social distancing level [0-100]: ")
    # Chamando a função da dinâmica de decisões do governante
    gov.gov_decisions()
    gov.distribute_resources(resources, media_pct, hospital_pct, primarycare_pct)
    hospital.resources = gov.hospital_resources
    primcare_resources = gov.primarycare_resources
    media.resources = gov.media_resources

    box = resources - (media.resources + hospital.resources + primcare_resources)
    print(f'Governor {player_gov}, you have {box}$ to next round')

    # choose talk
    media.choose_talk(player_media)

    # buy resources
    hospital.resources = gov.hospital_resources
    hospital.buy_resources(player_hosp)

    # Cases dinamics
    pand.dynamics_pandemics(pop2,primcare_resources)
    tot_cases = pand.total_cases
    deaths = pand.total_death
    er_excess = pand.er_cases - hospital.er
    icu_excess = pand.icu_cases - hospital.icu
    enf_excess = pand.enf_cases - hospital.beds


    if er_excess < 0:
        er_excess = 0
    else:
        pass

    if icu_excess < 0:
        icu_excess = 0
    else:
        pass

    if enf_excess < 0:
        enf_excess = 0
    else:
        pass

    deaths_excess = er_excess + icu_excess + enf_excess
    total_deaths = deaths + deaths_excess
    res_pop = pop2 - total_deaths
    pct_pop = res_pop/pop2

    # game results
    if media.positive_talk:
        print("The media talked positively about the government.")
    else:
        print("The media talked negatively about the government.")
    print(f"The hospital has {hospital.beds} beds, {hospital.icu} icu units and {hospital.er} units")
    print(f"Number of cases needing hospital care of {tot_cases} and in-hospital deaths was {deaths}")
    print(f"The number of death excess was {deaths_excess}, and total number of deaths was {total_deaths}")
    print(f" {icu_excess} died waiting for ICU,{er_excess} waiting for ER and {enf_excess} for Infirmary ")
    print(f'You actual population is {res_pop}')
    print("Good Job, you survived to first round")

# Agora incluidos o output para o próximo round
    return {
            "init_res": resources,
            "res_pop": res_pop,
            "pct_pop": pct_pop,
            "box": box,
            "media_talk": media.positive_talk,
            "social_isol": social_isol,
            'lockdown': gov.lockdown,
            'name_media': player_media,
            'name_hosp': player_hosp,
            'name_gov': player_gov
            }