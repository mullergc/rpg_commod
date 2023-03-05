import players as pl
import pandemics as pnd

### TRANSICAO ENTRE ROUNDS
class get_res:
    def __init__(self):
        self.resources = 0
        self.mediatalk = "p"
        self.rem_pop = 0
        self.pct_pop = 0

class get_resources_r2:
    def __init__(self):
        self.resources = 0
        self.mediatalk = 0
        self.mult_factor_media = 1
        #self.rem_pop = 0
        #self.pct_pop = 0
    def start_round(self,init_resources,pct_pop,media_talk,box):
        res = int(init_resources * pct_pop) + box

        if media_talk == True:
            mult_factor = 1
        else:
            mult_factor = 0.8
        self.resources += res
        self.mult_factor_media += mult_factor


def rounds(res_pop,pct_pop,init_resources,box,media_talk):
    r1 = get_resources_r2()
    gov = pl.Government()
    media = pl.Media()
    hospital = pl.Hospital()
    pand = pnd.pandemics_dinamics()

    r1.start_round(init_resources,pct_pop,media_talk,box)
    resources = r1.resources
    pop2 = int(res_pop)
    print(f"Governor, you have {r1.resources} to spend in this round")

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
    pand.dynamics_pandemics(pop2, primcare_resources)
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
    res_pop2 = pop2 - total_deaths
    pct_pop = res_pop2 / pop2

    # game results
    if media.positive_talk:
        print("The media talked positively about the government.")
    else:
        print("The media talked negatively about the government.")

    print(f"The hospital has {hospital.beds} beds, {hospital.icu} icu units and {hospital.er} units")
    print(f"Number of cases needing hospital care of {tot_cases} and total deaths was {total_deaths}")
    print(f"The number of death excess was {deaths_excess}")
    print(f" {icu_excess} died waiting for ICU,{er_excess} waiting for ER and {enf_excess} for Infirmary ")
    print("Good Job, you survived to one more round")
    # Agora incluidos o output para o próximo round
    return {
            "init_res": resources,
            "res_pop": res_pop2,
            "pct_pop": pct_pop,
            "box": box,
            "media_talk": media.positive_talk,
            "social_isol":social_isol,
            'lockdown': gov.lockdown
                }