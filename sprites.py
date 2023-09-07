import pygame
from pygame.sprite import *
from config import *
import time


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.groups = self.game.player_group, self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.psuedo_image = pygame.transform.scale(pygame.image.load("img/sk8er.png"),(PLAYER_WIDTH,PLAYER_HEIGHT)).convert_alpha()
        self.image = pygame.Surface.subsurface(self.psuedo_image, (0,75,PLAYER_WIDTH,PLAYER_HEIGHT//5))
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.rect = self.image.get_rect()
        self.rect.midbottom = [x, y]

    def getPseudo(self):
        return self.psuedo_image

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x - PLAYER_VEL >= 0:
            self.x_change -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and self.rect.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            self.x_change += PLAYER_VEL
        if keys[pygame.K_UP] and self.rect.y - PLAYER_VEL >= HEIGHT/2 - PLAYER_HEIGHT/4+20:
            self.y_change -= PLAYER_VEL
        if keys[pygame.K_DOWN] and self.rect.y + PLAYER_VEL + PLAYER_HEIGHT/4 <= HEIGHT:
            self.y_change += PLAYER_VEL

class TopCar(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.groups = self.game.obstacle_group, self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
        self.psuedo_image = pygame.transform.scale(pygame.image.load("img/car8.png"),(self.width,self.height)).convert_alpha()
        self.image = pygame.Surface.subsurface(self.psuedo_image, (0,50,self.width, self.height//2))
        self.rect = self.image.get_rect(midbottom=(WIDTH + CAR_WIDTH, TOP_LANE))
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def getPseudo(self):
        return self.psuedo_image

    def update(self):
        self.rect.x -= CAR_VEL*2
        if self.x < -CAR_WIDTH:
            self.kill()

class BottomCar(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.groups = self.game.obstacle_group, self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
        self.psuedo_image = pygame.transform.scale(pygame.image.load("img/bottomcar8.png"),(self.width,self.height)).convert_alpha()
        self.image = pygame.Surface.subsurface(self.psuedo_image, (0,50,self.width, self.height//2))
        self.rect = self.image.get_rect(midbottom=(WIDTH + CAR_WIDTH, BOTTOM_LANE))
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)        

    def update(self):
        self.rect.x += CAR_VEL/2
        if self.x > WIDTH + CAR_WIDTH:
            self.kill()

    def getPseudo(self):
        return self.psuedo_image

class Barrier(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.groups = self.game.obstacle_group, self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = BARRIER_WIDTH
        self.height = BARRIER_HEIGHT
        self.psuedo_image = pygame.transform.scale(pygame.image.load("img/barrier.png"),(self.width,self.height)).convert_alpha()
        self.image = pygame.Surface.subsurface(self.psuedo_image, (0,40,self.width, self.height//2))
        # self.image = pygame.transform.scale(pygame.image.load("img/barrier.png"),(self.width,self.height)).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(WIDTH + CAR_WIDTH, BOTTOM_LANE))
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        self.rect.x -= self.game.scroll_speed
        if self.x < -BARRIER_WIDTH:
            self.kill()

    def getPseudo(self):
        return self.psuedo_image


class Coin(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.groups = self.game.obstacle_group, self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x
        self.y = y
        self.width = BARRIER_WIDTH
        self.height = BARRIER_HEIGHT
        # self.psuedo_image = pygame.transform.scale(pygame.image.load("img/barrier.png"),(self.width,self.height)).convert_alpha()
        # self.image = pygame.Surface.subsurface(self.psuedo_image, (0,50,self.width, self.height//2))
        self.image = pygame.transform.scale(pygame.image.load("img/barrier.png"),(self.width,self.height)).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(WIDTH + CAR_WIDTH, BOTTOM_LANE))
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        self.rect.x -= self.game.scroll_speed
        if self.x < -BARRIER_WIDTH:
            self.kill()

