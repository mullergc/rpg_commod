import random


class Government:
    def __init__(self):
        self.resources = 200
        self.media_resources = 0
        self.hospital_resources = 0
        self.primarycare_resources = 0

    def distribute_resources(self, media_pct, hospital_pct, primarycare_pct):
        self.media_resources = int(self.resources * (media_pct / 100))
        self.hospital_resources = int(self.resources * (hospital_pct / 100))
        self.primarycare_resources = int(self.resources * (primarycare_pct / 100))
        self.resources -= self.media_resources + self.hospital_resources + self.primarycare_resources


class Media:
    def __init__(self):
        self.resources = 0
        self.positive_talk = True

    def choose_talk(self):
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
        print(f"You can buy a maximum of {max_beds} beds, {max_icu} icu units and {max_er} er units.")
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


def play_game():
    gov = Government()
    media = Media()
    hospital = Hospital()

    # distribute resources
    media_pct = int(input("Enter percentage of resources for media: "))
    hospital_pct = int(input("Enter percentage of resources for hospital: "))
    primarycare_pct = 100 - media_pct - hospital_pct
    gov.distribute_resources(media_pct, hospital_pct, primarycare_pct)

    # choose talk
    media.choose_talk()

    # buy resources
    hospital.resources = gov.hospital_resources
    hospital.buy_resources()

    # game results
    if media.positive_talk:
        print("The media talked positively about the government.")
    else:
        print("The media talked negatively about the government.")
    print(f"The hospital has {hospital.beds} beds, {hospital.icu} icu units and {hospital.er} units")

