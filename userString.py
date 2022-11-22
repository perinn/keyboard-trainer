import pygame
import time


class UserString:
    def __init__(self):
        self.text = None
        self.string = ""
        self.char = ""
        self.start_typing = False

    def update_char(self, game, event, original_str, screen, colors, fonts):
        self.char = event.unicode
        if self.char == original_str.get_char():
            if not self.start_typing:
                game.time = time.time()
                self.start_typing = True
            game.cnt_of_symbols += 1
            original_str.update_string_idx(game, screen, colors, fonts)
        elif self.char != "":
            game.update_errors()
            if pygame.key.name(event.key) in game.errors_dict.keys():
                game.errors_dict[pygame.key.name(event.key)] += 1