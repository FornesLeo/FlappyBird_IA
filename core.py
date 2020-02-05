#!/usr/bin/python

import pygame
from src.background import Background
from src.bird import Bird
from src.pipe import Pipe
from src.base import Base

WIN_WIDTH = 550
WIN_HEIGHT = 800

pygame.font.init()
font = pygame.font.SysFont(None, 50)

class Core:

    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.bird = Bird(200, 200)
        self.background = Background(WIN_WIDTH, WIN_HEIGHT)
        self.base = Base(WIN_HEIGHT - 75)
        self.pipes = [Pipe(600), Pipe(1000)]
        self.run = True
        self.pause = False
        self.loose = False
        self.clock = pygame.time.Clock()
        self.score = 0

    def start(self):
        while self.run:
            self.clock.tick(30)
            self.event()
            if not self.pause and not self.loose:
                self.update()
            self.display()
        pygame.quit()
        quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.bird.jump()
                if event.key == pygame.K_ESCAPE:
                    self.run = False
                if event.key == pygame.K_p:
                    self.pause = not self.pause

    def update(self):
        if self.bird.y >= WIN_HEIGHT - 100:
            self.loose = True
        rm = []
        for pipe in self.pipes:
            if pipe.x < -100:
                rm.append(pipe)
            if pipe.collide(self.bird):
                self.loose = True
            if not pipe.passed and pipe.x < self.bird.x:
                pipe.passed = True
                self.score += 1
                self.pipes.append(Pipe(1000))
        for r in rm:
            self.pipes.remove(r)

        self.background.move()
        self.bird.move()
        for pipe in self.pipes:
            pipe.move()
        self.base.move()

    def display(self):
        self.background.draw(self.win)
        self.bird.draw(self.win)
        for pipe in self.pipes:
            pipe.draw(self.win)
        self.base.draw(self.win)

        text = font.render("Score: " + str(self.score), 1, (255, 255, 255))
        self.win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
        pygame.display.update()

if __name__ == "__main__":
    # execute only if run as a script
    game = Core()
    game.start()
