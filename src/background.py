import os
import pygame

class Background:
    _background = pygame.transform.scale2x(
        pygame.image.load(os.path.join("images", "background.png")))

    VEl = 2

    def __init__(self, width, height):
        self._width = width
        self.height = height
        self.backgroundPosition = []
        self.backgroundMove = 0
        self.backgroundY = -50

        i = 0
        while i < width * 2:
            self.backgroundPosition.append(i)
            i += self._background.get_rect().size[0]

    def draw(self, win):
        for i in self.backgroundPosition:
            win.blit(self._background, (i - self.backgroundMove, self.backgroundY))

    def move(self):
        self.backgroundMove += self.VEl
        if self.backgroundMove > self._background.get_rect().size[0]:
            self.backgroundMove = 0