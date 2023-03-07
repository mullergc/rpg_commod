class Government:
    def __init__(self):
       # self.resources = 200
        self.media_resources = 0
        self.hospital_resources = 0
        self.primarycare_resources = 0
        self.rem_resources = 0
        self.social_isol = 0
        self.lockdown = "N"
    def gov_decisions(self):
        lockdown = input("Impose Lockdown? [Y/N] ")
        if lockdown.lower() == 'y':
           self.lockdown = True
        elif lockdown.lower() == 'n':
             self.lockdown = False
        else:
             print("Invalid input, please choose Y or N")
             self.gov_decisions()


    def distribute_resources(self,resources, media_pct, hospital_pct, primarycare_pct):
        self.media_resources = int(resources * (media_pct / 100))
        self.hospital_resources = int(resources * (hospital_pct / 100))
        self.primarycare_resources = int(resources * (primarycare_pct / 100))

class Media:
    def __init__(self):
        self.resources = 0
        self.positive_talk = True

    def choose_talk(self,player_media):
        print(f'{player_media}, you have {self.resources} to pay your workers and to manage')
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

    def buy_resources(self,player_hosp):
        bed_price = 2
        icu_price = 4
        er_price = 2
        max_beds = int(self.resources / bed_price)
        max_icu = int(self.resources / icu_price)
        max_er = int(self.resources / er_price)
        print(f"{player_hosp}, you can buy with {self.resources}$ a maximum of {max_beds} beds, {max_icu} icu units and {max_er} er units.")
        beds = int(input("How many beds do you want to buy? (each=2$)"))
        balance = self.resources - (beds * bed_price)
        print(f"You still have {balance}$")
        icu = int(input("How many icu units do you want to buy? (each=4$)"))
        balance = balance - (icu * icu_price)
        print(f"You still have {balance}$")
        er = int(input("How many er units do you want to buy? (each=2$)"))
        total_cost = beds * bed_price + icu * icu_price + er * er_price
        if total_cost > self.resources:
            print("Not enough resources to buy all the items.")
            self.buy_resources(player_hosp)
        else:
            self.beds += beds
            self.icu += icu
            self.er += er
            self.resources -= total_cost
