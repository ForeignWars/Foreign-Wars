import pygame
from faction import Faction

class Dwarf (Faction):
  def __init__(self, start, mithril, gyrocopter, dwarf_emblem):
    self.start=(start.x, start.y)
    self.mithril=mithril
    self.gyrocopter=gyrocopter
    self.dwarf_emblem=dwarf_emblem
  def fortress():