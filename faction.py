import pygame
from nation import Nation

class Faction:
  def __init__ (self, gold, army):
    self.gold=gold
    self.units=[]
    self.attack_units=[]
    self.army=army
    self.attack_army=self.army-1
    self.nations=[]
  def attack (self, nation):
    self.attack_units.append(self.units)
    self.units.clear()
    if '1' in self.attack_units:
      self.attack_units.remove('1')
      self.units.append('1')
    elif '2' in self.attack_units:
      self.attack_units.remove('2')
      self.units.append('2')
    elif '3' in self.attack_units:
      self.attack_units.remove('3')
      self.units.append('3')
    elif '4' in self.attack_units:
      self.attack_units.remove('4')
      self.units.append('4')
    if nation.health>=self.attack_army:
      nation.health-=self.attack_army
    else:
      leftover = self.army - nation.health
      while leftover>0:
        if self.army - nation.health >= 4:
          if '4' in nation.units:
            nation.units.remove('4')
            leftover-=4
            self.attack_units.remove('4')
          elif '3' in nation.units:
            nation.units.remove('3')
            leftover-=3
            self.attack_units.remove('3')
          elif '2' in nation.units:
            nation.units.remove('2')
            leftover-=2
            self.attack_units.remove('2')
          elif '1' in nation.units:
            nation.units.remove('1')
            leftover-=1
            self.attack_units.remove('1')
          else:
            self.nations.append(nation)
            nation.units.append(self.attack_units)
      nation.health=0
  def recruit (self,nation):
