import pygame
import time
from faction import Faction

class Nation:
  pygame.init()
  def __init__(self, color, health, graph, x, y):
    self.color = color
    self.health = health
    self.graph = graph
    self.army=0
    self.x=x
    self.y=y
  def conquered (self, Faction):
    fenetre.blit(Faction.emblem, (self.x, self.y))
  def attack (self, nation_ennemie, player_faction):
    if self.army>1:
      self.attack_army=self.army-1
      self.army-=self.attack_army
      if nation_ennemie.health>=self.attack_army:
        nation_ennemie.health-=self.attack_army
        self.attack_army=0
      else:
        leftover = self.attack_army - nation_ennemie.health
        self.attack_army-=nation_ennemie
        if nation_ennemie.army>leftover:
          nation_ennemie.army-=leftover
          leftover=0
        elif nation_ennemie.army==leftover:
          nation_ennemie = 0
          player_faction.append(nation_ennemie)
          nation_ennemie.army=1
        elif nation_ennemie.army<leftover:
          leftover-=nation_ennemie.army
          nation_ennemie.army=leftover
          player_faction.append(nation_ennemie)
