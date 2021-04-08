import pygame
from faction import Faction
from nation import Nation

class Dwarf (Faction):
  def __init__(self, start, mithril, gyrocopter, dwarf_emblem):
    Faction.__init__(self, gold, army)
    self.gold=5
    self.army=0
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

class Orc (Faction):
  def __init__(self, start, rage, berzerker, orc_emblem):
    Faction.__init__(self, gold, army)
    self.gold=5
    self.army=0
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
      self.units+=self.units
      
class Demon (Faction):
  def __init__(self, start, souls, mephistopheles, demon_emblem):
    Faction.__init__(self, gold, army)
    self.gold=5
    self.army=0
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
