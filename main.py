import pygame
from pygame.locals import *
import time
from config import *
from sprites import * 
import sys
import random

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font("img/font1.ttf",30)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Sk8er Boy')
        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.elapsed_time = 0
        self.playing = True
        self.running = True
        self.hit = False
        self.bg = pygame.transform.scale(pygame.image.load('img/backgroundSky.jpg'),(WIDTH, HEIGHT)).convert_alpha()
        self.road = pygame.transform.scale(pygame.image.load('img/road2.png'), (EXTRAWIDE, HEIGHT/2)).convert_alpha()
        self.ground_scroll = 0
        self.scroll_speed = 4
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player_group = pygame.sprite.LayeredUpdates()
        self.obstacle_group = pygame.sprite.LayeredUpdates()
        self.topcar_timer = pygame.time.set_timer(USEREVENT+1, random.randint(MIN_DELAY//1.5, MAX_DELAY*5))
        self.bottomcar_timer = pygame.time.set_timer(USEREVENT+2, random.randint(MIN_DELAY//1.5, MAX_DELAY*5))
        self.topbarrier_timer = pygame.time.set_timer(USEREVENT+3, random.randint(MIN_DELAY//1.5, MAX_DELAY*5))
        self.bottombarrier_timer = pygame.time.set_timer(USEREVENT+4, random.randint(MIN_DELAY//1.5, MAX_DELAY*5))


    def checkCollisions(self):
        if pygame.sprite.spritecollide(self.player_group.get_sprite(0), self.obstacle_group, False, pygame.sprite.collide_mask):
            self.hit = True

    def groundScroll(self):
        self.ground_scroll -= self.scroll_speed
        if abs(self.ground_scroll) > 750:
            self.ground_scroll = 0

    def new(self):
        self.playing = True
        self.player = Player(self, PLAYER_WIDTH*2, (BOTTOM_LANE))


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == USEREVENT+1:
                TopCar(self, WIDTH+CAR_WIDTH, TOP_LANE)
                self.topcar_timertimer = pygame.time.set_timer(USEREVENT+1, random.randint(MIN_DELAY//1.5, MAX_DELAY*2))
            if event.type == USEREVENT+2:
                BottomCar(self, -CAR_WIDTH*2, BOTTOM_LANE)
                self.bottomcar_timer = pygame.time.set_timer(USEREVENT+2, random.randint(MIN_DELAY//1.5, MAX_DELAY*2))
            if event.type == USEREVENT+3:
                Barrier(self, WIDTH+BARRIER_WIDTH, TOP_SW)
                self.topbarrier_timer = pygame.time.set_timer(USEREVENT+3, random.randint(MIN_DELAY//1.5, MAX_DELAY*2))
            if event.type == USEREVENT+4:
                Barrier(self, WIDTH+BARRIER_WIDTH, BOTTOM_SW)
                self.bottombarrier_timer = pygame.time.set_timer(USEREVENT+4, random.randint(MIN_DELAY//1.5, MAX_DELAY*2))


    def update(self):
        self.clock.tick(FPS)
        pygame.display.update()
        self.checkCollisions()
        self.all_sprites.update()
        self.elapsed_time = time.time() - self.start_time
        if self.hit:
            self.gameOver()

    def draw(self):
        self.groundScroll()
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.road, (self.ground_scroll, 375))    
        for sprite in sorted(self.all_sprites.sprites(),key = lambda sprite: sprite.rect.centery):
            self.screen.blit(sprite.image, sprite)
            if isinstance(sprite, Player):
                self.screen.blit(sprite.getPseudo(), (sprite.rect.x, sprite.rect.y-75))
            elif isinstance(sprite, TopCar) or isinstance(sprite,BottomCar):
                self.screen.blit(sprite.getPseudo(), (sprite.rect.x, sprite.rect.y-50))
            elif isinstance(sprite, Barrier):
                self.screen.blit(sprite.getPseudo(), (sprite.rect.x, sprite.rect.y-40))
            # else:
            #     self.screen.blit(sprite.image, sprite.rect)
        time_text = self.font.render(f"Time: {round(self.elapsed_time)}", 1, "white")
        self.screen.blit(time_text,(10,10)) 

    def gameOver(self):
            lost_text = self.font.render("You Lost!", 1, "white")
            self.screen.blit(lost_text, (WIDTH/2-lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(5000)
            self.playing = False

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

if __name__ == '__main__':    
    g = Game()
    g.new()
    while g.running:
        g.main()

    pygame.quit()
    sys.exit()