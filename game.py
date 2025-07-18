import pygame
from math import cos , sin , radians




Largeur_Ecran =800
Hauteur_Ecran =750

Largeur_Raquette=80
Hauteur_Raquette=10
Altitude_Raquette=150


game_over= False


Largeur_brique = 50
Hauteur_brique = 25
Inter_brique = 20
Marge_brique = 20
Nb_Brique_Par_Ligne = 11
Nb_Ligne_Brique = 4


PAS_DEPLACEMENT_RAQUETTE=25
PAS_DEPLACEMENT_BALLE = 20

Diamètre_balle=20

ANGLE_LANCER=50


Nombre_Vie_Debut=3


pygame.font.init()
Police= pygame.font.SysFont("Comic Sans MS",size=30)

#https://www.google.com/search?q=pygame+casse+brick&oq=pygame+casse+brick&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABgIGA0YHtIBCTEwNjkzajFqN6gCALACAA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:a2a8021c,vid:YL3pdhxhcp0,st:0

class Poutre(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.surf = pygame.Surface((Largeur_Raquette,Hauteur_Raquette))
    self.surf.fill((0,255,0))
    self.rect = self.surf.get_rect()
    self.rect.x = Largeur_Ecran / 2 - Largeur_Raquette / 2
    self.rect.y = Hauteur_Ecran - 2*Hauteur_Raquette - Altitude_Raquette

  def update(self,pressed_keys):
    if pressed_keys[pygame.K_LEFT]:
      self.rect.move_ip(-PAS_DEPLACEMENT_RAQUETTE,0)
      if ma_balle.stick:
        ma_balle.rect.move_ip(-PAS_DEPLACEMENT_RAQUETTE, 0)
    if pressed_keys[pygame.K_RIGHT]:
      self.rect.move_ip(PAS_DEPLACEMENT_RAQUETTE,0)
      if ma_balle.stick:
        ma_balle.rect.move_ip(PAS_DEPLACEMENT_RAQUETTE, 0)
    if self.rect.left <0:
      self.rect.left = 0
      if ma_balle.stick:
        ma_balle.rect.left = Largeur_Raquette/2 - Diamètre_balle/2
    if self.rect.right > Largeur_Ecran:
      self.rect.right = Largeur_Ecran
      if ma_balle.stick:
        ma_balle.rect.right = Largeur_Ecran - Largeur_Raquette / 2 + Diamètre_balle / 2
    print(f"Position :  X={self.rect.x};Y={self.rect.y}")


class Balle(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.surf = pygame.Surface((Diamètre_balle,Diamètre_balle))
    self.surf.fill((255,0,0))
    self.rect = self.surf.get_rect()
    self.stick = True
    self.nombre_vie = Nombre_Vie_Debut
    self.moving_x = PAS_DEPLACEMENT_BALLE * cos(radians(ANGLE_LANCER))
    self.moving_y = -PAS_DEPLACEMENT_BALLE * sin(radians(ANGLE_LANCER))
    self.init_position()

  def init_position(self):
    self.stick = True
    self.rect.x = ma_poutre.rect.x + Largeur_Raquette/2 - Diamètre_balle/2
    self.rect.y = ma_poutre.rect.y - Hauteur_Raquette*2
    self.moving_x = PAS_DEPLACEMENT_BALLE * cos(radians(ANGLE_LANCER))
    self.moving_y = -PAS_DEPLACEMENT_BALLE * sin(radians(ANGLE_LANCER))

  
  def update(self , pressed_keys):
    if pressed_keys[pygame.K_SPACE]:
      self.stick=False
    if not self.stick:
      self.rect.x += self.moving_x
      self.rect.y += self.moving_y
    if self.rect.y < 0:
      self.moving_y = -self.moving_y
    if self.rect.x < 0 or self .rect.x > Largeur_Ecran - Diamètre_balle/2:
      self.moving_x = -self.moving_x
    if self.rect.y > Hauteur_Ecran:
      self.nombre_vie -= 1
      self.init_position()


  def rebond_raquette(self):
    self.moving_y = -self.moving_y

  def inverse_x(self):
    self.moving_x = -self.moving_x

  def inverse_y(self):
    self.moving_y = -self.moving_y
   

class Brique(pygame.sprite.Sprite):
  
  def __init__(self,x,y):
    super().__init__()
    self.surf = pygame.Surface((Largeur_brique,Hauteur_brique))
    self.surf.fill((0,30,255))
    self.rect = self.surf.get_rect()
    self.rect.x = x
    self.rect.y = y


  staticmethod
  def init_mur_briques():
    y = Marge_brique
    for j in range(Nb_Ligne_Brique):
      x = Marge_brique
      for i in range(Nb_Brique_Par_Ligne):
        brique = Brique (x,y)
        tous_sprites.add(brique)
        groupe_brique.add(brique)
        x = Marge_brique + (Largeur_brique + Inter_brique)*(i+1)
      y = Marge_brique + (Hauteur_brique + Inter_brique)*(j+1) 






class Score(pygame.sprite.Sprite):
  
  def __init__(self):
    super().__init__()
    self.scoreCourant = 0
    self._setText()


  def _setText(self):
    self.surf = Police.render('Score :' + str(self.scoreCourant),False,(255,255,255))
    self.rect = self.surf.get_rect(center=(Largeur_Ecran-200, Hauteur_Ecran-Altitude_Raquette/2))



  def reset(self):
    self.scoreCourant = 0
  


  def update(self, pressed_keys):
    self._setText()

  def incremente(self, valeur):
    self.scoreCourant += valeur

class GameOver(pygame.sprite.Sprite):
  
  def __init__(self):
    super().__init__()
    self._setText()


  def _setText(self):
    self.surf = Police.render('Game over',False,(255,0,0))
    self.rect = self.surf.get_rect(center=(Largeur_Ecran/2, Hauteur_Ecran/2))
  
  def update(self, pressed_keys):
    self._setText()


class VieRestante(pygame.sprite.Sprite):
  
  def __init__(self):
    super().__init__()
    self._setText()


  def _setText(self):
    self.surf = Police.render('Vies :' + str(ma_balle.nombre_vie),False,(255,255,255))
    self.rect = self.surf.get_rect(center=(200, Hauteur_Ecran-Altitude_Raquette/2))
  


  def update(self, pressed_keys):
    self._setText()


class Menu():

  def __init__(self):
    super().__init__()

  def showMenu(self,ecran):
    play = False
    running = True

    #self.surf = pygame.image.load("images/background.jpg").convert()
    surf = pygame.image.load("images/play2.png").convert()
    surf.set_colorkey((255,255,255))
    pygame.display.set_caption("menu")
    #clock = pygame.time.Clock()
    #running = True
    while running :
      ecran.blit(surf, surf.get_rect(center=(Largeur_Ecran/2,Hauteur_Ecran/2)))
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        touches = pygame.key.get_pressed()
        if touches[pygame.K_p]:
          play=True
          running = False

    return play




pygame.init()
ecran = pygame.display.set_mode((Largeur_Ecran,Hauteur_Ecran))
pygame.display.set_caption("ball-block")
clock = pygame.time.Clock()
running = True

menu = Menu()
veuxJouer = menu.showMenu(ecran)

tous_sprites = pygame.sprite.Group()
ma_poutre = Poutre()
ma_balle = Balle()
tous_sprites.add(ma_poutre)
tous_sprites.add(ma_balle)
groupe_raquette = pygame.sprite.Group()
groupe_raquette.add(ma_poutre)
groupe_brique = pygame.sprite.Group()
mon_score = Score()
tous_sprites.add(mon_score)
tous_sprites.add(VieRestante())

Brique.init_mur_briques()

while running :
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  ecran.fill("black")

  if ma_balle.nombre_vie == 0:
    tous_sprites.add(GameOver())
  else:
    if pygame.sprite.spritecollideany(ma_balle , groupe_raquette):
      ma_balle.rebond_raquette()


    briques_touchees = pygame.sprite.spritecollide(ma_balle,groupe_brique,True)
    for brique in briques_touchees:
      mon_score.incremente(10)
      relative_x = ma_balle.rect.x-brique.rect.x
      relative_y = ma_balle.rect.y-brique.rect.y
      if relative_x > 0 and relative_y > 0 or relative_x > 0 > relative_y :
        ma_balle.inverse_y( )
      if relative_x < 0 < relative_y or relative_x > 0 > relative_y:
        ma_balle.inverse_x()

    touches = pygame.key.get_pressed()

    for mon_sprite in tous_sprites:
      mon_sprite.update(touches)

  for mon_sprite in tous_sprites:
    ecran.blit(mon_sprite.surf,mon_sprite.rect)

  pygame.display.flip()

  clock.tick(30)

pygame.quit()


