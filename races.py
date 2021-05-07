import pygame
from faction import *
from nation import *

class Dwarf (Faction):
    def __init__(self, start, mithril, gyrocopter, dwarf_emblem):
        super(Faction).__init__()
        self.start=(start.x, start.y)
        self.mithril=mithril
        self.gyrocopter=gyrocopter
        self.dwarf_emblem=dwarf_emblem
        self.nations=[start]
    def conquered_nations():
        for country in self.nations:
            country.conquered
    def fortress(Nation):
        if mithril>=30:
            Nation.health+=10
    def recruit_gyrocopter(self, Nation):
        if mithril>=10:
            Nation.army+=4
        else:
            print("Va miner, d'où tu viens me demander un gyrocoptère sans mithril?!")

class Orc (Faction):
    def __init__(self, start, rage, berzerker, orc_emblem):
        super(Faction).__init__()
        self.start=(start.x, start.y)
        self.rage=rage
        self.berzerker=berzerker
        self.orc_emblem=orc_emblem
        self.nations=[start]
    def conquered_nations():
        for country in self.nations:
            country.conquered
    def waaagh ():
        if rage>=50:
            self.army=self.army*2
    def recruit_berzerker(self, Nation):
        if rage>=10:
            Nation.army+=4
        else:
            print("Azy, kestuveux?! Tu vois pas ch'uis pas assez vénèr pour passer berzerk?")

class Demon (Faction):
    def __init__(self, start, souls, mephistopheles, demon_emblem):
        super(Faction).__init__()
        self.start=(start.x, start.y)
        self.souls=souls
        self.mephistopheles=mephistopheles
        self.demon_emblem=demon_emblem
        self.nations=[start]
    def conquered_nations():
        for country in self.nations:
            country.conquered
    def corruption(Nation):
        if souls>=80:
            self.nations.append(Nation)
            Nation.conquered
    def recruit_mephistopheles(self, Nation):
        if souls>=25:
            Nation.army+=4
        else:
            print("Tu veux invoquer notre Seigneur tout puissant sans sacrifice d'âmes? Va t'en, chien!")

class Centaure (Faction):
    def __init__(self, start, totems, centaurion, centaur_emblem):
        super(Faction).__init__()
        self.start=(start.x, start.y)
        self.totems=totems
        self.centaurion=centaurion
        self.centaur_emblem=centaur_emblem
        self.nations=[start]
    def conquered_nations():
        for country in self.nations:
            country.conquered
    def volley(Nation):
        if totems>=16:
            Nation.health-=5
    def recruit_centaurion(self, Nation):
        if totem>=5:
            Nation.army+=4
        else:
            print("Comment veux-tu former un centaurion sans faire appel à la puissance des ancêtres? Va sculpter des totems, et reviens me voir!")
