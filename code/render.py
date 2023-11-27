import pygame
import time 
import random

WIDTH, HEIGHT = 1000, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("battleship")



def render():
    screen.fill("black")
    
    
    
    
    
    pygame.display.flip()
    clock.tick(60)
