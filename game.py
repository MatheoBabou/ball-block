import pygame

Largeur_Ecran =800
Hauteur_Ecran =600

Largeur_Raquette=80
Hauteur_Raquette=10


PAS_DEPLACEMENT_RAQUETTE=1

#https://www.google.com/search?q=pygame+casse+brick&oq=pygame+casse+brick&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABgIGA0YHtIBCTEwNjkzajFqN6gCALACAA&sourceid=chrome&ie=UTF-8#fpstate=ive&vld=cid:a2a8021c,vid:YL3pdhxhcp0,st:0

class Poutre(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.surf = pygame.Surface((Largeur_Raquette,Hauteur_Raquette))
    self.surf.fill((0,255,0))
    self.rect = self.surf.get_rect()
    self.rect.x = Largeur_Ecran / 2 - Largeur_Raquette / 2
    self.rect.y = Hauteur_Ecran - 2*Hauteur_Raquette



  def update(self,pressed_keys):
    if pressed_keys[pygame.K_LEFT]:
      self.rect.move_ip(-PAS_DEPLACEMENT_RAQUETTE,0)
    if pressed_keys[pygame.K_RIGHT]:
      self.rect.move_ip(PAS_DEPLACEMENT_RAQUETTE,0)
    print(f"Position :  X={self.rect.x};Y={self.rect.y}")





def main():
  pygame.init()
  ecran = pygame.display.set_mode((Largeur_Ecran,Hauteur_Ecran))
  pygame.display.set_caption("ball-block")
  running = True

  tous_sprites = pygame.sprite.Group()
  ma_poutre = Poutre()
  tous_sprites.add(ma_poutre)


  while running :
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    ecran.fill("black")

    touches = pygame.key.get_pressed()

    for mon_sprite in tous_sprites:
      mon_sprite.update(touches)

    for mon_sprite in tous_sprites:
      ecran.blit(mon_sprite.surf,mon_sprite.rect)

    pygame.display.flip()

  pygame.quit()



main()