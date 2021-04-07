import pygame
import time
from faction import Faction

class Nation:
  pygame.init()
  def __init__(self, color, health, graph, x, y):
    self.color = color
    self.health = health
    self.graph = graph
    self.units=[]
    self.x=x
    self.y=y
  def faction(self, Faction):
    Faction.units.append(self.units)
  def conquered (self, Faction):
    fenetre.blit(Faction.emblem, (self.x, self.y))
