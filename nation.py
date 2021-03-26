import pygame
import Time

class Nation:
  pygame.init()
  def __init__(self, color, health, graph):
    self.color = color
    self.health = health
    self.graph = graph
