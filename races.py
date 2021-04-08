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
