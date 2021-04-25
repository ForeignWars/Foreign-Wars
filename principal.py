import pygame
import os
import random
import time
from pygame.locals import *
from nation import Nation
from faction import Faction
from races import *
pygame.init()

#---------ecran---------
#définition de la taille de l'écran
largeur_fenetre=1365
hauteur_fenetre=657
#définition des polices affichées à l'écran
font_style=pygame.font.SysFont("Garamond",25)
#création de l'écran
fenetre= pygame.display.set_mode((largeur_fenetre,hauteur_fenetre))
pygame.display.set_caption('Foreign Wars')
#démarrage du timer
clock=pygame.time.Clock()

tour=0  #initialisation du nombre de tour

limitrophe = {
  'thukten':{'lildeilon','inno6','aorizia'},
  'lildeilon':{'thukten','inno6','ordogas','amlivor'},
  'inno6':{'thukten','lildeilon','aorizia','amlivor','azaire'},
  'aorizia':{'thukten','inno6','azaire'},
  'ordogas':{'lildeilon','amlivor','baerdan','krarzimak'},
  'amlivor':{'lildeilon','inno6','ordogas','azaire','baerdan','frodrine'},
  'azaire':{'inno6','aorizia','amlivor','frodrine'},
  'baerdan':{'ordogas','amlivor','krarzimak','frodrine'},
  'krarzimak':{'ordogas','baerdan','frodrine','vaedran','andrinos'},
  'frodrine':{'amlivor','azaire','baerdan','krarzimak','vaedran'},
  'vaedran':{'krarzimak','frodrine','andrinos','phosthonia'},
  'andrinos':{'krarzimak','vaedran','szetas'},
  'szetas':{'andrinos','mentuhotep'},
  'mentuhotep':{'szetas','eichornia','ryutada','kuargen','gargle','zhoshusat'},
  'eichornia':{'mentuhotep','ryutada','loukinir','zhoshusat','alaneo'},
  'ryutada':{'mentuhotep','eichornia','loukinir','kuargen'},
  'kuargen':{'mentuhotep','ryutada','gargle','thunodel'},
  'gargle':{'mentuhotep','kuargen','thunodel','zhoshusat','alaneo'},
  'alaneo':{'eichornia','loukinir','thunodel','gargle','zhoshusat'},
  'zhoshusat':{'mentuhotep','eichornia','alaneo','gargle'},
  'loukinir':{'eichornia','ryutada','alaneo','thunodel','doldrec'},
  'thunodel':{'kuargen','gargle','alaneo','loukinir','doldrec'},
  'doldrec':{'loukinir','thunodel'},
  'phosthonia':{'vaedran','kharrak','vyndono'},
  'kharrak':{'phosthonia','vyndono','lycurgus'},
  'vyndono':{'phosthonia','kharrak'},
  'lycurgus':{'kharrak','bamzar','jaldumka'},
  'jaldumka':{'lycurgus','bamzar'},
  'bamzar':{'lycurgus','jaldumka','diable'},
  'diable':{'bamzar','kayal','nordland'},
  'kayal':{'diable','raseldor','tchorroppoi','qeralukia','vaelinore'},
  'raseldor':{'kayal','tchorroppoi','karithyr'},
  'tchorroppoi':{'kayal','raseldor','karithyr','vaelinore','qeralukia'},
  'qeralukia':{'kayal','tchorroppoi','vaelinore','drulguk'},
  'vaelinore':{'kayal','tchorroppoi','qeralukia','karithyr','drulguk'},
  'karithyr':{'raseldor','tchorroppoi','vaelinore','drulguk'},
  'drulguk':{'qeralukia','vaelinore','karithyr'},
  'nordland':{'diable','finnär','vestgeir','dawi'},
  'dawi':{'nordland','scalare','helek'},
  'scalare':{'dawi','helek','alrion','sslitherin'},
  'helek':{'dawi','scalare','alrion','hua'},
  'alrion':{'scalare','helek','sslitherin'},
  'sslitherin':{'scalare','alrion','shyzzia'},
  'shyzzia':{'sslitherin','murem'},
  'finnär':{'nordland','vestgeir','defnar'},
  'vestgeir':{'nordland','finnär','defnar','holdrer'},
  'defnar':{'finnär','vestgeir','holdrer','ergli','dhondru'},
  'holdrer':{'vestgeir','defnar','dhondru'},
  'ergli':{'defnar','dhondru'},
  'dhondru':{'defnar','holdrer','ergli','rimmassee'},
  'rimmassee':{'dhondru','hua'},
  'hua':{'helek','rimmassee','idenia'},
  'idenia':{'hua','baganda','brillup'},
  'baganda':{'idenia','brillup'},
  'brillup':{'idenia','baganda','murem'},
  'murem':{'shyzzia','brillup'},
}

#import des images
embleme_centaure = pygame.image.load("SPRITES/Centaures/Emb_Centaure.png")
embleme_demon = pygame.image.load("SPRITES/Demons/Emb_Demon.png")
embleme_nain = pygame.image.load("SPRITES/Nains/Emb_Nain.png")
embleme_orc = pygame.image.load("SPRITES/Orcs/Emb_Orc.png")
img_inf_centaure = pygame.image.load("SPRITES/Centaures/Inf_Centaure.png")
img_cav_centaure = pygame.image.load("SPRITES/Centaures/Cav_Centaure.png")
img_art_centaure = pygame.image.load("SPRITES/Centaures/Art_Centaure.png")
img_spec_centaure = pygame.image.load("SPRITES/Centaures/Spec_Centaure.png")
img_inf_demon = pygame.image.load("SPRITES/Demons/Inf_Demon.png")
img_cav_demon = pygame.image.load("SPRITES/Demons/Cav_Demon.png")
img_art_demon = pygame.image.load("SPRITES/Demons/Art_Demon.png")
img_spec_demon = pygame.image.load("SPRITES/Demons/Spec_Demon.png")
img_inf_nain = pygame.image.load("SPRITES/Nains/Inf_Nain.png")
img_cav_nain = pygame.image.load("SPRITES/Nains/Cav_Nain.png")
img_art_nain = pygame.image.load("SPRITES/Nains/Art_Nain.png")
img_spec_nain = pygame.image.load("SPRITES/Nains/Spec_Nain.png")
img_inf_orc = pygame.image.load("SPRITES/Orcs/Inf_Orc.png")
img_cav_orc = pygame.image.load("SPRITES/Orcs/Cav_Orc.png")
img_art_orc = pygame.image.load("SPRITES/Orcs/Art_Orc.png")
img_spec_orc = pygame.image.load("SPRITES/Orcs/Spec_Orc.png")

class Menu:
    """création et gestions des boutons du menu"""
    def __init__(self, application, *groupes) :
        self.couleurs = dict(
            normal=(133, 1, 100),
            survol=(96, 0, 0),
        )
        font = pygame.font.SysFont('Garamond', 25, bold=True) #police d'écritur eainsi que taille de celle-ci.
        # noms des menus et commandes associées
        items = (
            ('JOUER', application.btn_classe),#texte du premier bouton jouer
            ('QUITTER', application.quitter)#texte du deuxième bouton, quitter
        )
        x = largeur_fenetre/2   #position première fenêtre, la deuxième est juste décalé de 120 en y vers le bas.
        y = (hauteur_fenetre/2)-60
        self._boutons = []
        for texte, cmd in items :
            mb = MenuBouton(
                texte,
                self.couleurs['survol'],
                font,
                x,
                y,
                200, #taille rectangla avec x et y x=200 et y=50
                50,
                cmd
            )
            self._boutons.append(mb)
            y += 120    #décalage de 120 vers lez bas pour la deuxième fenêtre.
            for groupe in groupes :
                groupe.add(mb)
    def update(self, events) :
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self._boutons :
            # Si le pointeur souris est au-dessus d'un bouton
            if bouton.rect.collidepoint(*posPointeur) :
                # Changement du curseur par un quelconque
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # Changement de la couleur du bouton
                bouton.dessiner(self.couleurs['normal'])
                # Si le clic gauche a été pressé
                if clicGauche :
                    # Appel de la fonction du bouton
                    bouton.executerCommande()
                break
            else :
                # Le pointeur n'est pas au-dessus du bouton
                bouton.dessiner(self.couleurs['survol'])
        else :
            # Le pointeur n'est pas au-dessus d'un des boutons
            # initialisation au pointeur par défaut
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
    def detruire(self) :
        pygame.mouse.set_cursor(*pygame.cursors.arrow) # initialisation du pointeur


class MenuBouton(pygame.sprite.Sprite) :
    """  fonction qui fait les boutons et crée un simple bouton rectangulaire """
    def __init__(self, texte, couleur, font, x, y, largeur, hauteur, commande) :
        super().__init__()
        self._commande = commande

        self.image = pygame.Surface((largeur, hauteur))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y) #voir au dessus

        self.texte = font.render(texte, True, (255, 255, 255))
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (largeur/2, hauteur/2)#permet de centre le texte dans le rectangle

        self.dessiner(couleur)

    def dessiner(self, couleur) :
        self.image.fill(couleur)
        self.image.blit(self.texte, self.rectTexte)

    def executerCommande(self) :
        # Appel de la commande du bouton
        self._commande()

class Btn_classe :
    """ Simulacre de l'interface du jeu """
    def __init__(self, application, *groupes) :
        self.couleurs = dict(
            normal=(80, 80, 80),
            survol=(0, 0, 0),
        )
        font = pygame.font.SysFont('Garamond', 25, bold=True) #police d'écritur eainsi que taille de celle-ci.
        # noms des menus et commandes associées
        items = (                               #boutons de sélection de faction
            ('NAINS', application.start, player_faction=NAINS),
            ('DEMONS', application.start, player_faction=DEMONS),
            ('CENTAURES', application.start, player_faction=CENTAURES),
            ('ORCS', application.start, player_faction=ORCS)
        )
        x = (largeur_fenetre/2) -330  #position première fenêtre, la deuxième est juste décalé de 120 en y vers le bas.
        y = (hauteur_fenetre/2)
        self._boutons = []
        for texte, cmd in items :
            mb = MenuBouton(texte,self.couleurs['survol'],font,x,y,200,50,cmd)
            self._boutons.append(mb)
            x += 220

            for groupe in groupes :
                groupe.add(mb)

    def update(self, events) :
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self._boutons :
            # Si le pointeur souris est au-dessus d'un bouton
            if bouton.rect.collidepoint(*posPointeur) :
                # Changement du curseur par un quelconque
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # Changement de la couleur du bouton
                bouton.dessiner(self.couleurs['normal'])
                # Si le clic gauche a été pressé
                if clicGauche :
                    # Appel de la fonction du bouton
                    bouton.executerCommande()
                break
            else :
                # Le pointeur n'est pas au-dessus du bouton
                bouton.dessiner(self.couleurs['survol'])

    def detruire(self) :
        pygame.time.set_timer(self._CLIGNOTER, 0) # désactivation du timer

class Application :
    """ Classe maîtresse gérant les différentes interfaces du jeu """
    def __init__(self) :
        pygame.init()
        pygame.display.set_caption("Foreign-Wars")

        self.fond = (235,97,4)  #couleur du fond

        self.fenetre = pygame.display.set_mode((largeur_fenetre,hauteur_fenetre))
        # Groupe de sprites utilisé pour l'affichage
        self.groupeGlobal = pygame.sprite.Group()
        self.statut = True

    def _initialiser(self) :
        try:
            self.ecran.detruire()
            # Suppression de tous les sprites du groupe
            self.groupeGlobal.empty()
        except AttributeError:
            pass

    def menu(self) :
        # Affichage du menu
        self._initialiser()
        self.ecran = Menu(self, self.groupeGlobal)

    def btn_classe(self) :
        # Affichage du jeu
        self._initialiser()
        self.ecran = Btn_classe(self, self.groupeGlobal)

    def start(self):
        game(nation)

    def quitter(self) : #fonction qui finit le programme
        self.statut = False #kill le programme

    def update(self) : #fonction qui rafraichit le jeu
        events = pygame.event.get() #remplace event par le evengt actuelle

        for event in events :
            if event.type == pygame.QUIT :
                self.quitter()
                return

        self.fenetre.fill(self.fond)#on remplit la fenetre par la couleur de fond
        self.ecran.update(events)#appelle event
        self.groupeGlobal.update()
        self.groupeGlobal.draw(self.fenetre)
        pygame.display.update()

def game ():
  faction_list=['nains','demons','orcs','centaures']
  faction_order=[]
  for i in range len(faction_list):
    j=random.randint(0,len(faction_list)
    faction_order.append(faction_list[j])
    faction_list.remove(faction_list[j])
                     
#définition des nations
dawi=Nation((255,0,0), 10, limitrophe, 962, 421)
defnar=Nation((144,59,59), 5, limitrophe, 1258, 548)
diable=Nation((255,128,128),2, limitrophe, 676, 320)
andrinos=Nation((0,100,0), 3, limitrophe, 218, 317)
thukten=Nation((255,184,184), 7, limitrophe, 235, 612)
lildeilon=Nation((0,255,0), 8, limitrophe, 188, 560)
inno6=Nation((255,255,111), 5, limitrophe, 283, 569)
aorizia=Nation((255,193,71), 3, limitrophe, 385, 550)
ordogas=Nation((0,0,100), 6, limitrophe, 153, 494)
amlivor=Nation((255,255,0), 9, limitrophe, 223, 504)
azaire=Nation((0,0,255), 4, limitrophe, 310, 527)
baerdan=Nation((100,255,100), 9, limitrophe, 211, 453)
frodrine=Nation((0,151,0), 5, limitrophe, 288, 450)
krarzimak=Nation((103,32,0), 4, limitrophe, 202, 395)
vaedran=Nation((0,255,255), 3, limitrophe, 318, 395)
szetas=Nation((171,50,255), 6, limitrophe, 244, 268)
mentuhotep=Nation((0,150,150), 8, limitrophe, 205, 189)
kuargen=Nation((100,255,255), 3, limitrophe, 205, 107)
ryutada=Nation((50,150,150), 6, limitrophe, 175, 160)
loukinir=Nation((150,0,135), 5, limitrophe, 141, 138)
doldrec=Nation((100,0,90), 8, limitrophe, 146, 110)
thunodel=Nation((200,200,200), 7, limitrophe, 130, 95)
eichornia=Nation((100,100,155), 6, limitrophe, 103, 151)
alaneo=Nation((50,50,150), 8, limitrophe, 95, 95)
gargle=Nation((59,0,100), 4, limitrophe, 154, 80)

#définition des factions
NAINS=Dwarf(dawi, 3, 0, embleme_nain)
ORCS=Orc(defnar, 0, 0, embleme_orc)
DEMONS=Demon(diable, 0, 0, embleme_demon)
CENTAURES=Centaur(andrinos, 4, 0, embleme_centaure)

def condition_attaque (): #fonction qui permet de savoir si le joueur peut attaquer une région
  totot=totot

def computer_turn (): #fonction qui fait jouer la machine
  totot=totot

app = Application() #appelle la fonction Application
app.menu()
while app.statut :
    app.update()  #appelle uopdate pour rafraichir l'interface
    clock.tick(30)  #avec la fréquence de 30 fois par secondes
pygame.quit() #fin du programme
