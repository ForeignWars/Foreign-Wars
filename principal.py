import pygame
import os
import random
import time
from pygame.locals import *
from nation import Nation
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
class Menu:
    """création et gedtions des boutons du menu"""
    def __init__(self, application, *groupes) :
        self.couleurs = dict(
            normal=(0, 200, 0),
            survol=(0, 200, 200),
        )
        font = pygame.font.SysFont('Garamond', 25, bold=True)
        # noms des menus et commandes associées
        items = (
            ('JOUER', application.jeu),
            ('QUITTER', application.quitter)
        )
        x = 400
        y = 200
        self._boutons = []
        for texte, cmd in items :
            mb = MenuBouton(
                texte,
                self.couleurs['normal'],
                font,
                x,
                y,
                200,
                50,
                cmd
            )
            self._boutons.append(mb)
            y += 120
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
                bouton.dessiner(self.couleurs['survol'])
                # Si le clic gauche a été pressé
                if clicGauche :
                    # Appel de la fonction du bouton
                    bouton.executerCommande()
                break
            else :
                # Le pointeur n'est pas au-dessus du bouton
                bouton.dessiner(self.couleurs['normal'])
        else :
            # Le pointeur n'est pas au-dessus d'un des boutons
            # initialisation au pointeur par défaut
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
    def detruire(self) :
        pygame.mouse.set_cursor(*pygame.cursors.arrow) # initialisation du pointeur


class MenuBouton(pygame.sprite.Sprite) :
    """ Création d'un simple bouton rectangulaire """
    def __init__(self, texte, couleur, font, x, y, largeur, hauteur, commande) :
        super().__init__()
        self._commande = commande

        self.image = pygame.Surface((largeur, hauteur))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.texte = font.render(texte, True, (0, 0, 0))
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (largeur/2, hauteur/2)

        self.dessiner(couleur)

    def dessiner(self, couleur) :
        self.image.fill(couleur)
        self.image.blit(self.texte, self.rectTexte)

    def executerCommande(self) :
        # Appel de la commande du bouton
        self._commande()
class Application :
    """ Classe maîtresse gérant les différentes interfaces du jeu """
    def __init__(self) :
        pygame.init()
        pygame.display.set_caption("ISN ILIES")

        self.fond = (150,)*3

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

    def jeu(self) :
        # Affichage du jeu
        self._initialiser()
        self.ecran = Jeu(self, self.groupeGlobal)

    def quitter(self) :
        self.statut = False

    def update(self) :
        events = pygame.event.get()

        for event in events :
            if event.type == pygame.QUIT :
                self.quitter()
                return

        self.fenetre.fill(self.fond)
        self.ecran.update(events)
        self.groupeGlobal.update()
        self.groupeGlobal.draw(self.fenetre)
        pygame.display.update()
def interface (): #faire une interface
  
  
def qui_qui_joue(): #fonction qui permet de savoir qui joue
  faction_list=(1,2,3,4)
   
  
def condition_attaque (): #fonction qui permet de savoir si le joueur peut attaquer une région
  
  
def tour_machine (): #fonction qui fait jouer la machine
  
  
app = Application()
app.menu()
while app.statut :
    app.update()
    clock.tick(30)
pygame.quit()
