
import pygame

class Display():
    def __init__(self):
        self.displayWidth = 500
        self.displayHeight = 500
        self.display = pygame.display.set_mode((self.displayWidth, self.displayHeight))
        self.setCaption("First Try")

    def setCaption(self, text):
        pygame.display.set_caption(text)

    def fill(self, color):
        self.display.fill(color)

    def blit(self, Surf, Rect):
        self.display.blit(Surf, Rect)