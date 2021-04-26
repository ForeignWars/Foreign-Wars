import pygame
from nation import *

class Faction:
  def __init__ (self, gold, army):
    self.gold=5
    self.units=[]
    self.attack_units=[]
    self.army=army
    self.attack_army=self.army-1
  def attack (self, Nation):
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
    if Nation.health>=self.attack_army:
      Nation.health-=self.attack_army
      self.attack_army=0
      self.attack_units.clear()
    else:
      leftover = self.army - Nation.health
      while leftover>0:
        if self.army - Nation.health >= 4:
          if '4' in Nation.units:
            Nation.units.remove('4')
            leftover-=4
            self.attack_units.remove('4')
          elif '3' in Nation.units:
            Nation.units.remove('3')
            leftover-=3
            self.attack_units.remove('3')
          elif '2' in Nation.units:
            Nation.units.remove('2')
            leftover-=2
            self.attack_units.remove('2')
          elif '1' in Nation.units:
            Nation.units.remove('1')
            leftover-=1
            self.attack_units.remove('1')
          else:
            self.nations.append(Nation)
            Nation.units.append(self.attack_units)
      Nation.health=0
  def recruit (self,Nation):
     toto=toto
