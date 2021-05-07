import pygame
from nation import *

class Faction :
  def __init__(self,gold):
    self.gold=5
  def recruit_inf (self,Nation):
     if self.gold>=1:
        Nation.army+=1
     else:
        print("Pas assez d'or")
  def recruit_cav (self, Nation):
     if self.gold>=3:
        Nation.army+=2
     else:
        print("Pas assez d'or")
  def recruit_art (self, Nation):
     if self.gold>=5:
        Nation.army+=3
     else:
        print("Pas assez d'or")
