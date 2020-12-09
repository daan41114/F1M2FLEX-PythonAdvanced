class rimuru:
    
    name = 'rimuru temest'
    monster='slime'
    ability='predetor'
    item="shizu's mask"
    
    def stats(self):
        print(self.name + "'s monster type is " + str(self.monster) + ", his item is " + str(self.item) +" and his ability is " + str(self.ability))

    def SayingName(self):
        print("my name is " + self.name)

class milim(rimuru):
    rank='demon lord'
    UniqueSkill='milim eye'
    def __init__(self):
        rimuru.name = "demon lord milim"
        rimuru.monster ='dragonoid'
        rimuru.ability = 'unknown'

    def stats(self):
        print(self.name + "'s monster type is " + str(self.monster) + ", her ability is " + str(self.ability) + ", her unique skill is " + (self.UniqueSkill) +  " and rank is " + self.rank)

    def SayingName(self):
        super().SayingName
        print('I am the ' + self.name + '!')

    def TalkingAboutRimuru(self):
        print('rimuru is my bestie!')

rimuruR = rimuru()

print("rimuru")
rimuruR.stats()
rimuruR.SayingName()
print("------------------------------")

milimR = milim()

print("milim")
milimR.stats()
milimR.SayingName()
milimR.TalkingAboutRimuru()
