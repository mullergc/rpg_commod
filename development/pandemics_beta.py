import random
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

        if cases < 0:
            cases = 0
        else:
            pass

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
