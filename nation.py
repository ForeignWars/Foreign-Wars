import pygame
import time

class Nation:
  pygame.init()
  def __init__(self, color, health, graph, x, y):
    self.color = color
    self.health = health
    self.graph = graph
    self.units=[]
    self.x=x
    self.y=y
  def faction(self, faction):
    faction.units.append(self.units)
  def conquered (self.faction):
    fenetre.blit(emblem, (self.x, self.y))
