import render
import pygame
import time 
import random
battleship_count = [1,1,1,1,1]
board_size = [10,10]

# define and create board array
board = []
for i in range(board_size[0]*board_size[1]):
    board.append(0)

#create battleship class
class battleship:
    def __init__(self, name, length, coords=None):
        self.name = name
        self.length = length
        self.coords = coords # meant to be set to an array in this format [x,y]


# creating battleship objects 
ships = {
    "carrier":[battleship("carrier", 5) for _ in range(battleship_count[0])], 
    "battleship":[battleship("battleship", 4) for _ in range(battleship_count[1])], 
    "submarine":[battleship("submarine", 3) for _ in range(battleship_count[2])],
    "cruiser":[battleship("cruiser", 2)for _ in range(battleship_count[4])],
    "destroyer":[battleship("destroyer", 2) for _ in range(battleship_count[3])]
    }
        

#game loop
def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("bye")
                run = False
                break
    pygame.quit()

main()






