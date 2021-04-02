import pygame
import os
import random
import time
from pygame.locals import *
from nation import Nation
from faction import Faction
from races import *
import PIL.Image          				# Module PIL.Image
pygame.init()

#---------ecran---------
#*inition de la taille de l'écran
largeur_fenetre=1366
hauteur_fenetre=768
#définition des polices affichées à l'écran
font_style=pygame.font.SysFont("Garamond",25)
#creation de l'écran
fenetre= pygame.display.set_mode((largeur_fenetre,hauteur_fenetre))
pygame.display.set_caption('Foreign Wars')
#démarrage du timer
clock=pygame.time.Clock()

tour=0  #initialisation du nombre de tour

limitrophe = {
  'thukten':{'lildeilon','inno-6','aorizia'},
  'lildeilon':{'thukten','inno-6','ordogas','amlivor'},
  'inno-6':{'thukten','lildeilon','aorizia','amlivor','azaire'},
  'aorizia':{'thukten','inno-6','azaire'},
  'ordogas':{'lildeilon','amlivor','baerdan','krar-zimak'},
  'amlivor':{'lildeilon','inno-6','ordogas','azaire','baerdan','frodrine'},
  'azaire':{'inno-6','aorizia','amlivor','frodrine'},
  'baerdan':{'ordogas','amlivor','krar-zimak','frodrine'},
  'krar-zimak':{'ordogas','baerdan','frodrine','vaedran','andrinos'},
  'frodrine':{'amlivor','azaire','baerdan','krar-zimak','vaedran'},
  'vaedran':{'krar-zimak','frodrine','andrinos','phosthonia'},
  'andrinos':{'krar-zimak','vaedran','szet-as'},
  'szet-as':{'andrinos','mentu-hotep'},
  'mentu-hotep':{'eichornia','ryutada','kuargen','gargle','zhoshusat'},
  'eichornia':{'mentu-hotep','ryutada','loukinir','zhoshusat','alaneo'},
  'ryutada':{'mentu-hotep','eichornia','loukinir','kuargen'},
  'kuargen':{'mentu-hotep','ryutada','gargle','thunodel'},
  'gargle':{'mentu-hotep','kuargen','thunodel','zhoshusat','alaneo'},
  'alaneo':{'eichornia','loukinir','thunodel','gargle','zhoshusat'},
  'zhoshusat':{'mentu-hotep','eichornia','alaneo','gargle'},
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
  'scalare':{'dawi','helek','al-rion','sslitherin'},
  'helek':{'dawi','scalare','al-rion','hua'},
  'al-rion':{'scalare','helek','sslitherin'},
  'sslitherin':{'scalare','al-rion','shyzzia'},
  'shyzzia':{'sslitherin','murem'},
  'finnär':{'nordland','vestgeir','defnar'},
  'vestgeir':{'nordland','finnär','defnar','hol-drer'},
  'defnar':{'finnär','vestgeir','hol-drer','ergli','dhondru'},
  'hol-drer':{'vestgeir','defnar','dhondru'},
  'ergli':{'defnar','dhondru'},
  'dhondru':{'defnar','hol-drer','ergli','rimmassee'},
  'rimmassee':{'dhondru','hua'},
  'hua':{'helek','rimmassee','idenia'},
  'idenia':{'hua','baganda','brillup'},
  'baganda':{'idenia','brillup'},
  'brillup':{'idenia','baganda','murem'},
  'murem':{'shyzzia','brillup'},
}

embleme_centaure=PIL.Image.open("SPRITES/Centaures/Emb_Centaure.png")
embleme_demon=PIL.Image.open("SPRITES/Demons/Emb_Demon.png")
embleme_nains=PIL.Image.open("SPRITES/Nains/Emb_Nain.png")
embleme_orc=PIL.Image.open("SPRITES/Nains/Emb_Nain.png")



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
        items = (
            ('NAINS', application.quitter),#texte du premier bouton jouer
            ('DEMONS', application.quitter),#texte du deuxième bouton, quitter
            ('CENTAURES', application.quitter),#texte du deuxième bouton, quitter
            ('ORCS', application.quitter)#texte du deuxième bouton, quitter
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




def interface (): #faire une interface
  totot=totot

def player_order(): #fonction qui permet de savoir qui qui joue
  faction_list=[1,2,3,4]
  player_faction=dwarf

NAINS=Dwarf(dawi, 3, gyrocopter, embleme_nain)

def condition_attaque (): #fonction qui permet de savoir si le joueur peut attaquer une région
  totot=totot

def tour_machine (): #fonction qui fait jouer la machine
  totot=totot

app = Application() #appelle la fonction Application
app.menu()
while app.statut :
    app.update()  #appelle uopdate pour rafraichir l'interface
    clock.tick(30)  #avec la fréquence de 30 fois par secondes
pygame.quit() #fin du programme
