import pygame
import os
import random
import time
from pygame.locals impor

limitrophes = {
  'thukten':{lildeilon,inno-6,aorizia},
  'lildeilon':{thukten,inno-6,ordogas,amlivor},
  'inno-6':{thukten,lildeilon,aorizia,amlivor,azaire},
  'aorizia':{thukten,inno-6,azaire,}
  'ordogas':{lildeilon,amlivor,baerdan,krar-zimak,}
  'amlivor':{lildeilon,inno-6,ordogas,azaire,baerdan,frodrine}
  'azaire':{inno-6,aorizia,amlivor,frodrine}
  'baerdan':{ordogas,amlivor,krar-zimak,frodrine}
  'krar-zimak':{ordogas,baerdan,frodrine,vaedran,andrinos}
  'frodrine':{amlivor,azaire,baerdan,krar-zimak,vaedran}
  'vaedran':{krar-zimak,frodrine,andrinos,phosthonia}
  'andrinos':{krar-zimak,vaedran,szet-as}
  'szet-as':{andrinos,mentu-hotep}
  'mentu-hotep':{eichornia,ryutada,kuargen,gargle,zhoshusat}
  'eichornia':{mentu-hotep,ryutada,loukinir,zhoshusat,alaneo}
  'ryutada':{mentu-hotep,eichornia,loukinir,kuargen}
  'kuargen':{}
  '':{}
  '':{}
  '':{}
  '':{}
  '':{}
  '':{}
  '':{}
  '':{}
  '':{}
  '':{}
  '':{}
  
}

#la région=toute les régions limitrophes
# ----------------- ecran -------------
# definition de la taille de l'écran
largeur_fenetre = 1366
hauteur_fenetre = 768
#definition des fonts de l'écran
font_style = pygame.font.SysFont("Garamond", 25)
# creation de l'ecran
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption('Snake Python')
# démarage du timer
clock = pygame.time.Clock()
