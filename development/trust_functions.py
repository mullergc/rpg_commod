class trust_function:
    def __init__(self):
        self.trust = 0
        #self.lockdown = 0
        #self.positive_talk = 0
        self.media_output = 0
        self.lockdown_output = 0
        self.trust_output = 0

    def trust_people(self,trust,positive_talk,lockdown):
        if positive_talk == True:
            media_output = 5
        else:
            media_output = -10

        if lockdown == True:
            lockdown_output = -20
        else:
            lockdown_output = 0

        trust_output = trust + media_output + lockdown_output
        # O número de confiança não pode ser > 100
        if trust_output > 100:
            trust_output = 100
        else:
            pass
        return trust_output

