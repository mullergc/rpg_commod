import random
import pandas as pd

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

class Government:
    def __init__(self):
       # self.resources = 200
        self.media_resources = 0
        self.hospital_resources = 0
        self.primarycare_resources = 0
        self.rem_resources = 0

    def distribute_resources(self,resources, media_pct, hospital_pct, primarycare_pct):
        self.media_resources = int(resources * (media_pct / 100))
        self.hospital_resources = int(resources * (hospital_pct / 100))
        self.primarycare_resources = int(resources * (primarycare_pct / 100))


class Media:
    def __init__(self):
        self.resources = 0
        self.positive_talk = True

    def choose_talk(self):
        print(f'You have {self.resources} to pay your workers and to manage')
        talk = input("Do you want to talk positively or negatively about the government? (P/N) ")
        if talk.lower() == 'p':
            self.positive_talk = True
        elif talk.lower() == 'n':
            self.positive_talk = False
        else:
            print("Invalid input, please choose P or N")
            self.choose_talk()


class Hospital:
    def __init__(self):
        self.resources = 0
        self.beds = 0
        self.icu = 0
        self.er = 0

    def buy_resources(self):
        bed_price = 2
        icu_price = 4
        er_price = 2
        max_beds = int(self.resources / bed_price)
        max_icu = int(self.resources / icu_price)
        max_er = int(self.resources / er_price)
        print(f"You can buy with {self.resources} a maximum of {max_beds} beds, {max_icu} icu units and {max_er} er units.")
        beds = int(input("How many beds do you want to buy? "))
        icu = int(input("How many icu units do you want to buy? "))
        er = int(input("How many er units do you want to buy? "))
        total_cost = beds * bed_price + icu * icu_price + er * er_price
        if total_cost > self.resources:
            print("Not enough resources to buy all the items.")
            self.buy_resources()
        else:
            self.beds += beds
            self.icu += icu
            self.er += er
            self.resources -= total_cost

class pandemics_dinamics:
    def __init__(self):
        self.cases= 0
        self.icu_cases = 0
        self.er_cases = 0
        self.enf_cases = 0
        self.icu_deaths = 0
        self.er_deaths = 0
        self.enf_deaths = 0
        self.total_death = 0

    def dynamics_pandemics(self,pop,primcare_resources):
        percent = int(random.randrange(1,10))
        cases = int((pop*(percent/100)) - primcare_resources/5)
        icu_cases = int(cases * 0.2)
        enf_cases = int(cases * 0.2)
        er_cases = int(cases * 0.6)
        icu_deaths = int(cases * 0.2 * 0.8)
        er_deaths = int(cases * 0.6 * 0.8)
        enf_deaths = int(cases * 0.2 * 0.6)

        self.icu_cases += icu_cases
        self.enf_cases += enf_cases
        self.er_cases += er_cases
        self.icu_deaths += icu_deaths
        self.enf_deaths += enf_deaths
        self.er_deaths += er_deaths
        self.total_cases = self.icu_cases + self.enf_cases + self.er_cases
        self.total_death = self.er_deaths + self.enf_deaths + self.icu_deaths


def play_game():
    st = start()
    gov = Government()
    media = Media()
    hospital = Hospital()
    pand = pandemics_dinamics()

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
    media_pct = int(input("Enter percentage of resources for media: "))
    hospital_pct = int(input("Enter percentage of resources for hospital: "))
    primarycare_pct = int(input("Enter percentage of resources for Primary Care: "))
    box = resources - (media_pct + hospital_pct + primarycare_pct)
    print(f'Governor, you have {box} to next round')
    gov.distribute_resources(resources, media_pct, hospital_pct, primarycare_pct)
    hospital.resources = gov.hospital_resources
    primcare_resources = gov.primarycare_resources
    media.resources = gov.media_resources

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

    cases_tot = pand.er_cases + pand.icu_cases + pand.enf_cases
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
    print("Good Job")
    #print(f"Amount of resource was {diflev}")
