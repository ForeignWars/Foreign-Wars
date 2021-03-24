import pygame
import os
import random
import time
from pygame.locals impor
pygame.init()
#---------ecran---------
#definition de la taille de l'écran
largeur_fenetre=1366
hauteur_fenetre=768
#définition des polices affichées à l'écran
font_style=pygame.font.SysFont("Garamond",25)
#creation de l'écran
fenetre= pygame.display.set_mode((largeur_fenetre,hauteur_fenetre))
pygame.display.set_caption('Foreign Wars')
#démarrage du timer
clock=pygame.time.Clock()


limitrophe = {
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
  'kuargen':{mentu-hotep,ryutada,gargle,thunodel}
  'gargle':{mentu-hotep,kuargen,thunodel,zhoshusat,alaneo}
  'alaneo':{eichornia,loukinir,thunodel,gargle,zhoshusat}
  'zhoshusat':{mentu-hotep,eichornia,alaneo,gargle}
  'loukinir':{eichornia,ryutada,alaneo,thunodel,doldrec}
  'thunodel':{kuargen,gargle,alaneo,loukinir,doldrec}
  'doldrec':{loukinir,thunodel}
  'phosthonia':{vaedrann,kharrak,vyndono}
  'kharrak':{phosthonia,vyndono,lycurgus}
  'vyndono':{phosthonia,kharrak}
  'lycurgus':{kharrak,bamzar,jaldumka}
  'jaldumka':{lycurgus,bamzar}
  'bamzar':{lycurgus,jaldumka,diable}
  'diable':{bamzar,kayal,nordland}
  'kayal':{diable,raseldor,tchorroppoi,qeralukia,vaelinore}
  'raseldor':{kayal,tchorroppoi,karithyr}
  'tchorroppoi':{kayal,raseldor,karithyr,vaelinore,qeralukia}
  'qeralukia':{kayal,tchorroppoi,vaelinore,drulguk}
  'vaelinore':{kayal,tchorroppoi,qeralukia,karithyr,drulguk}
  'karithyr':{raseldor,tchorroppoi,vaelinore}
  '':{}
  '':{}
  '':{}
  '':{}
  
}

