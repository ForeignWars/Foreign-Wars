import pygame
from nation import Nation

class Faction:
  def __init__ (self, start, gold, resource, power, commander, units, army):
    self.start=start
    self.gold=gold
    self.resource=resource
    self.power=power
    self.commander=commander
    self.units=[]
    self.army=army
  def attack (self, nation):
    if nation.health>=self.army:
      nation.health-=self.army
    else:
      nation.health=0
  def recruit (self,nation):
    
