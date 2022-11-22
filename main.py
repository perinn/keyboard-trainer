import pygame
from game import Game

pygame.init()
colors = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "green": (50, 200, 50), "blue": (0, 0, 255),
          "gray": (128, 128, 128), "yellow": (255, 255, 0), "dark_gray": (50, 50, 50), "light_gray": (200, 200, 200),
          "very_light_gray": (230, 230, 230)}
fonts = {"system_50": pygame.font.SysFont("system", 50), "system_40": pygame.font.SysFont("system", 40),
         "system_30": pygame.font.SysFont("system", 30)}
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.update()
pygame.display.set_caption("Typing speed test")
running = True
while running:
    game = Game()
    game.main_screen(screen, colors, fonts)
    print("pupa")
pygame.quit()