import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, ac_x, ac_y, image_path,aircraft_speed):
        super().__init__()
        self.ac_img=pygame.image.load(image_path)
        self.image = self.ac_img.convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=ac_x
        self.rect.y=ac_y
        self.ac_speed=aircraft_speed


    def update(self):
        self.rect.x += self.ac_speed
        if self.rect.right>=850:
            self.ac_speed=-self.ac_speed
        elif self.rect.left<=0:
            self.ac_speed=-self.ac_speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self,b_x,b_y,type):
        super().__init__()
        self.image=pygame.image.load("bullet.png").convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=b_x
        self.rect.y=b_y
        if type=="e":
            self.b_speed=5
        else:
            self.b_speed=-5
        
    def update(self):
        self.rect.y+=self.b_speed

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image=pygame.image.load(image_path)
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)



    