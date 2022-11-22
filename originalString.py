import pygame


class OriginalString:
    def __init__(self, file_way, user_string):
        self.user_string = user_string
        self.file = open(file_way, "r").read()
        self.string = ""
        for i in range(len(self.file)):
            if self.file[i] == "\n":
                self.string += " "
            else:
                self.string += self.file[i]
        self.string_idx = 0

    def update_string_idx(self, game, screen, colors, fonts):
        self.string_idx += 1
        if self.string_idx == len(self.string):
            game.results_screen(screen, colors, fonts)
            game.screen_main_running = False

    def get_char(self):
        return self.string[self.string_idx]

    def get_progress(self):
        return self.string_idx / len(self.string)

    def draw_text(self, screen, fonts, colors):
        text1 = fonts["system_50"].render(self.string[:self.string_idx], True, colors["gray"])
        text2 = fonts["system_50"].render(self.string[self.string_idx:], True, colors["black"])
        pygame.draw.rect(screen, colors["very_light_gray"],
                         (90, 90, screen.get_width() / 2 - 90, text1.get_height() + 20))
        screen.blit(text1, (screen.get_width() / 2 - text1.get_width(), 100))
        screen.blit(text2, (screen.get_width() / 2, 100))
        pygame.draw.rect(screen, colors["white"], (0, 100, 100, text1.get_height()))
        pygame.draw.rect(screen, colors["very_light_gray"],
                         (90, 90, 10, text1.get_height() + 20))
        pygame.draw.rect(screen, colors["white"], (screen.get_width() - 100, 100, 100, text2.get_height()))
        pygame.draw.rect(screen, colors["black"], (90, 90, screen.get_width() - 180, 55), 3)
