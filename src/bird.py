import os
import pygame

BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("images", "bird3.png")))
]

class Bird:
    _image = BIRD_IMGS
    _maxRotation = 25
    _rotVelocity = 20
    _animationTime = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tickCount = 0
        self.velocity = 0
        self.height = self.y
        self.imageCount = 0
        self.img = self._image[0]

    def jump(self):
        self.velocity = -10.5
        self.tickCount = 0
        self.height = self.y

    def move(self):
        self.tickCount += 1
        moveUp = self.velocity * self.tickCount + 1.5 * (self.tickCount ** 2)
        if moveUp >= 16:
            moveUp = 16
        self.y += moveUp
        if moveUp < 0 or self.y < self.height + 50:
            if self.tilt < self._maxRotation:
                self.tilt = self._maxRotation
        else:
            if self.tilt > -90:
                self.tilt -= self._rotVelocity

    def draw(self, win):
        self.imageCount += 1
        if self.imageCount <= self._animationTime:
            self.img = self._image[0]
        elif self.imageCount <= self._animationTime * 2:
            self.img = self._image[1]
        elif self.imageCount <= self._animationTime * 3:
            self.img = self._image[2]
        elif self.imageCount <= self._animationTime * 4:
            self.img = self._image[1]
        elif self.imageCount >= self._animationTime * 4 + 1:
            self.img = self._image[0]
            self.imageCount = 0
        if self.tilt <= -80:
            self.img = self._image[1]
            self.imageCount = self._animationTime * 2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)

        win.blit(rotated_image, new_rect.topleft)

    def getMask(self):
        return pygame.mask.from_surface(self.img)