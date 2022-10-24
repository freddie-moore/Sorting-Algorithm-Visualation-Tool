import time

from PIL import Image
from pixel import Pixel
from time import sleep
import pygame
import random
pygame.init()

pixel_list = []
FPS = 60
WIDTH = HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algorithm Visualiser ⦿ S = Shuffle ⦿ I = Insertion Sort ⦿ B = Bubble sort ⦿ D = Draw Pixels")

def get_pixels():
    myImage = Image.open('testimage4.jpg')  # Can be many different formats.
    pix = myImage.load()
    pixelsize = WIDTH / myImage.width
    global myWidth
    myWidth = myImage.width
    for i in range(0,myImage.width): #draw pixels on new row
        for j in range(0,myImage.height): #draw pixels in new col
            findID = lambda i,j: (i*myImage.width) + j
            rgbval = pix[j,i]
            pixel_list.append(Pixel(rgbcol=rgbval, col=j, row=i, pixelID=findID(i,j), size = pixelsize))
    draw_pixels()

def draw_pixels():
   for pixel in pixel_list:
      col = lambda x,y: x % y
      row = lambda x,z,y: (x-z) / y
      pixel.draw(screen = screen, row = row(pixel_list.index(pixel), col(pixel_list.index(pixel),myWidth), myWidth), col = col(pixel_list.index(pixel),myWidth))
      pygame.display.flip()

def shuffle():
    random.shuffle(pixel_list)
    draw_pixels()

def insertion_sort(A):
    for i in range(1, len(A)):  # iterate through the whole array
        j = i - 1  # set j to equal previous index
        while A[j].pixelID > A[
            j + 1].pixelID and j >= 0:  # while index before is greater than data we examine , and j is not out of list range
            A[j], A[j + 1] = A[j + 1], A[j]  # swap index before and data we examine around
            j -= 1  # decrease prev index again to compare to next data
        draw_pixels()
    return A


def bubble_sort(A):
    for i in range(0,len(A)):
        swaps = 0
        j = 0
        while j < len(A) - 1:
            if A[j].pixelID > A[j+1].pixelID:
                A[j], A[j+1] = A[j+1], A[j]
                swaps += 1
                #draw_pixels()  # visualise individual pixel swaps
            j += 1
        draw_pixels() # visualise passes
        if swaps == 0:
            return A

def whatkeypressed(keypressBool):
    keyPresses = {2: "B", 4: "D", 9: "I", 19: "S"}
    try:
        return keyPresses[keypressBool.index(True)-3]
    except KeyError:
        pass

def main(): #main game loop
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                get_pixels()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    keypress = pygame.key.get_pressed()
                    playerinput = (whatkeypressed(keypressBool=keypress))
                    print(playerinput)
                    if playerinput == "S":
                        shuffle()
                    if playerinput == "I":
                        insertion_sort(A=pixel_list)
                    if playerinput == "B":
                        bubble_sort(A=pixel_list)
                    if playerinput == "D":
                        get_pixels()



        pygame.display.flip()

main()