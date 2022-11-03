from pygame import sprite
from pygame.math import Vector2
import SpriteManager

class Player2(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.pos = Vector2(x,y)
        self.spriteMan = SpriteManager.SpriteManager()
        self.og_image = self.spriteMan.req_image("O_Sprite")
        self.image = self.og_image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]
