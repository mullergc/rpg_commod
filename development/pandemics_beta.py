import random
import math
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

    # Definindo o número de casos
    # O número de casos é gerado de forma aleatória (random), entretanto é feito a partir
    # do número de pessoas inserido pelo usuário e do investimento na atenção primária
    # + primcare_resources | - cases
    def dynamics_pandemics(self,pop,primcare_resources):
        percent = int(random.randrange(5,10))
        cases = int((pop*(percent/100)) - primcare_resources/10)

        # O número de casos nunca pode ser negativo
        if cases < 0:
            cases = 0
        else:
            pass

        # Definindo a relação no número de casos com o número de mortes
        # math.floor -> arredondar os números para baixo
        # Casos: 20% para a UTI; 20% para a enfermaria; 60% para a emergência
        # Mortes: 80% na UTI; 20% na emergência; 60% na enfermaria (ambulatório)
        icu_cases = math.floor(int(cases * 0.2))
        enf_cases = math.floor(int(cases * 0.2))
        er_cases = math.floor(int(cases * 0.6))
        icu_deaths = math.floor(int(icu_cases * 0.8))
        er_deaths = math.floor(int(er_cases * 0.2))
        enf_deaths = math.floor(int(enf_cases * 0.6))

        self.icu_cases += icu_cases
        self.enf_cases += enf_cases
        self.er_cases += er_cases
        self.icu_deaths += icu_deaths
        self.enf_deaths += enf_deaths
        self.er_deaths += er_deaths
        self.total_cases = self.icu_cases + self.enf_cases + self.er_cases
        self.total_death = self.er_deaths + self.enf_deaths + self.icu_deaths


class pandemics_dinamics_r2:
    def __init__(self):
        self.cases= 0
        self.icu_cases = 0
        self.er_cases = 0
        self.enf_cases = 0
        self.icu_deaths = 0
        self.er_deaths = 0
        self.enf_deaths = 0
        self.total_death = 0

    # Definindo o número de casos
    # O número de casos é gerado de forma aleatória (random), entretanto é feito a partir
    # do número de pessoas inserido pelo usuário e do investimento na atenção primária
    # + primcare_resources | - cases
    def dynamics_pandemics(self,pop,primcare_resources,soc_iso,public_t):
        percent = int(random.randrange(1,10))
        cases = int((pop*(percent/100)) - ((primcare_resources/10)) - (public_t*(soc_iso/10)))

        # O número de casos nunca pode ser negativo
        if cases < 0:
            cases = 0
        else:
            pass

        # Definindo a relação no número de casos com o número de mortes
        # math.floor -> arredondar os números para baixo
        # Casos: 20% para a UTI; 20% para a enfermaria; 60% para a emergência
        # Mortes: 80% na UTI; 20% na emergência; 60% na enfermaria (ambulatório)
        icu_cases = math.floor(int(cases * 0.2))
        enf_cases = math.floor(int(cases * 0.2))
        er_cases = math.floor(int(cases * 0.6))
        icu_deaths = math.floor(int(icu_cases * 0.8))
        er_deaths = math.floor(int(er_cases * 0.2))
        enf_deaths = math.floor(int(enf_cases * 0.6))

        self.icu_cases += icu_cases
        self.enf_cases += enf_cases
        self.er_cases += er_cases
        self.icu_deaths += icu_deaths
        self.enf_deaths += enf_deaths
        self.er_deaths += er_deaths
        self.total_cases = self.icu_cases + self.enf_cases + self.er_cases
        self.total_death = self.er_deaths + self.enf_deaths + self.icu_deaths
