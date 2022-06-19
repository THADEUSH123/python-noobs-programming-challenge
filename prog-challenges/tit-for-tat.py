lnk = "https://www.forbes.com/sites/rogerkay/2011/12/19/generous-tit-for-tat-a-winning-strategy/#249316e666eb"


class Player(object):
    pass

    def __init__(self, archetype):
        self.wins = 0
        self.losses = 0
        self.archetype = archetype
  
    def win_score(self):
        return self.wins

    def decision(self):
        if self.achetype == "jesus":
            return "dont fink"
        if self.achetype == "satan":
            return "fink"
             


def challenge(p1,p2):
    if p1.decision == "fink" and p2.decision == "fink":
        p1.losses += 1
        p2.losses += 1
    elif p1.decision == "fink" and p2.decision == "dont fink":
        p1.wins += 2
        p2.losses += 3
    elif p1.decision == "dont fink" and p2.decision == "fink":
        p1.losses += 3
        p2.wins += 2
    elif p1.decision == "dont fink" and p2.decision == "dont fink":
        p1.wins += 1
        p2.wins += 1


jesus = Player("jesus") 

satan = Player("satan") 

for i in range(0,10):
     challenge(jesus,satan)
     

print(satan.win_score())
