import pygame

class Pixel:
    def __init__(self, rgbcol, col, row, pixelID, size):
        self.size = size
        self.rgbcol = rgbcol
        self.colnum = col
        self.rownum = row
        self.pixelID = pixelID

    def draw(self, screen, row, col):
        pygame.draw.rect(screen, self.rgbcol, (col*50, row*50, self.size, self.size))