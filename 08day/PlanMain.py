import pygame
from MySprite import *
class PlaneGame(object):
    def __init__(self):
        
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        
    def start_game(self):
        while True:
            self.clock.tick(60)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()
    def __create_sprites(self):
        
        bg1 = BackGroundSprite()
        bg2 = BackGroundSprite(True)
        self.bg_group = pygame.sprite.Group(bg1,bg2)
        self.enemy_group = pygame.sprite.Group()
        
        self.hero = HeroSprite()
        self.hero_group = pygame.sprite.Group(self.hero)
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = EnemySprite()
                self.enemy_group.add(enemy)
                self.hero.fire()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0
        if keys_pressed[pygame.K_SPACE]:
            print("该发射子弹了")
            self.hero.fire()
    def __check_collide(self):
        pass
    def __update_sprites(self):
        
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()
if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()
