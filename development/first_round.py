import players as pl
import pandemics as pnd

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


def round_1():
    st = start()
    gov = pl.Government()
    media = pl.Media()
    hospital = pl.Hospital()
    pand = pnd.pandemics_dinamics()

    #start info
    name = input("Name your country: ")
    pop = input("Enter your total population (max=1000): ")
    level = input("What level you would like to play? [EASY/NORMAL/HARD]")
    st.choose_pop(name,pop)
    st.choose_level(level)
    resources = st.res
    pop2 = int(pop)

    # distribute resources
    print(f"Governor, you have {resources} to distribute for Media, Hospital and Primary Care")
    media_pct = int(input("Enter percentage of resources for Media: "))
    hospital_pct = int(input("Enter percentage of resources for Hospital: "))
    primarycare_pct = int(input("Enter percentage of resources for Primary Care: "))
    social_isol = input("Define your social distancing level [0-100]: ")
    gov.gov_decisions()
    gov.distribute_resources(resources, media_pct, hospital_pct, primarycare_pct)
    hospital.resources = gov.hospital_resources
    primcare_resources = gov.primarycare_resources
    media.resources = gov.media_resources
    box = resources - (media.resources + hospital.resources + primcare_resources)
    print(f'Governor, you have {box}$ to next round')

    # choose talk
    media.choose_talk()

    # buy resources
    hospital.resources = gov.hospital_resources
    hospital.buy_resources()

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
    print(f"Number of cases needing hospital care of {tot_cases} and total deaths was {total_deaths}")
    print(f"The number of death excess was {deaths_excess}")
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
            'lockdown': gov.lockdown
            }