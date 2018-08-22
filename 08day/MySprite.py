import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新帧率
FRAME_PER_SEC = 60
#敌机事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#子弹事件常量
CREATE_BULLET_EVENT = pygame.USEREVENT + 1
#爆炸销毁图片

bg1 = pygame.image.load("./images/enemy0_down1.png")
bg2 = pygame.image.load("./images/enemy0_down2.png")
bg3 = pygame.image.load("./images/enemy0_down3.png")
bg4 = pygame.image.load("./images/enemy0_down4.png")

#爆炸精灵组
enemy1_down_group = pygame.sprite.Group()

#把爆炸图片放到列表中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,imagename,speed=1):
        super().__init__()
        self.image = pygame.image.load(imagename)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        self.rect.y+=self.speed
class EnemySprite(GameSprite):
    def __init__(self):
        self.imagename = "./images/enemy0.png"
        super().__init__(self.imagename)
        self.rect.bottom = 0
        maxvalue = SCREEN_RECT.width-self.rect.width
        self.rect.x = random.randint(0,maxvalue)
        self.speed = random.randint(1,10)
    def update(self):
        super().update()
        if self.rect.top >= SCREEN_RECT.height:
            self.kill()
class BackGroundSprite(GameSprite):
    def __init__(self,is_alt=False):
        self.imagename = "./images/background.png"
        super().__init__(self.imagename,5)
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        super().update()
        if self.rect.top >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
class HeroSprite(GameSprite):
    def __init__(self):
        self.imagename = "./images/hero.gif"
        super().__init__(self.imagename,0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.top = 550
        self.bullet_group = pygame.sprite.Group()
    def update(self):
        self.rect.x+=self.speed
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_RECT.width:
            self.rect.reght = SCREEN_RECT.width
    def fire(self):
        bullet = BulletSprite()
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.y = self.rect.top - 20
        self.bullet_group.add(bullet)

        bullet1 = BulletSprite()
        bullet1.rect.centerx = self.rect.centerx - 35
        bullet1.rect.y = self.rect.top + 35
        self.bullet_group.add(bullet1)

        bullet2 = BulletSprite()
        bullet2.rect.centerx = self.rect.centerx + 35
        bullet2.rect.y = self.rect.top + 35
        self.bullet_group.add(bullet2)
class BulletSprite(GameSprite):
    def __init__(self):
        self.imagename = "./images/bullet1.png"
        super().__init__(self.imagename,-20)
    def __del__(self):
        print("子弹销毁了")
    def update(self):
        super().update()
        if self.rect.bottom <= 0:
            self.kill()

