import os
import operator
import pygame
import time
import datetime
from tkinter.filedialog import askopenfilename

from userString import UserString
from originalString import OriginalString


class Game:
    def __init__(self):
        self.screen_main_running, self.original_string, self.user_string, self.screen_running = None, None, None, None
        self.cnt_of_errors, self.cnt_of_symbols, self.time = 0, 0, 0
        self.keyboard_img = pygame.image.load("keyboard.png")
        self.errors_dict = {"escape": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "0": 0,
                            "-": 0, "=": 0, "q": 0, "w": 0, "e": 0, "r": 0, "t": 0, "y": 0, "u": 0, "i": 0, "o": 0,
                            "p": 0, "[": 0, "]": 0, "\\": 0, "a": 0, "s": 0, "d": 0, "f": 0, "g": 0, "h": 0, "j": 0,
                            "k": 0, "l": 0, ";": 0, "'": 0, "z": 0, "x": 0, "c": 0, "v": 0, "b": 0, "n": 0, "m": 0,
                            ",": 0, ".": 0, "/": 0, "space": 0}

    def update_errors(self):
        self.cnt_of_errors += 1

    def get_speed(self):
        return int(self.cnt_of_symbols / (self.time / 60))

    def get_errors(self):
        return self.cnt_of_errors

    def select_file_screen(self, screen, colors, fonts):
        self.screen_running = True
        text = fonts["system_50"].render("Press any key to select a file", True, colors["black"])
        while self.screen_running:
            screen.fill(colors["white"])
            screen.blit(text, (
                screen.get_width() / 2 - text.get_width() / 2,
                screen.get_height() / 2 - text.get_height() / 2))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    filename = askopenfilename(filetypes=[('Text files', '*.txt')])
                    return filename
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def result_screen_initialization(self, screen, colors, fonts, errors):
        text1 = fonts["system_50"].render(
            "Time " + str(time.strftime("%M:%S", time.gmtime(int(self.time)))), True,
            colors["black"])
        text2 = fonts["system_50"].render(
            "You have typed " + str(len(self.original_string.string)) + " characters", True,
            colors["black"])
        text3 = fonts["system_50"].render("Count of errors = " + str(self.get_errors()), True, colors["black"])
        text4 = fonts["system_50"].render("Speed of typing = " + str(self.get_speed()) + " ch/m", True,
                                          colors["black"])
        text5 = fonts["system_50"].render("Accuracy = " + (
            str(
                (len(self.original_string.string) - self.get_errors()) / len(self.original_string.string) * 100)[:5]
        ) + "%", True, colors["black"])
        text6 = fonts["system_50"].render("Press the space bar to start over", True, colors["gray"])
        screen.fill(colors["white"])
        text7 = fonts["system_50"].render("Press Enter to see the statistics", True, colors["light_gray"])
        screen.fill(colors["white"])
        text8 = fonts["system_50"].render("Most of all you made a mistake in these keys:", True,
                                          colors["black"])
        text9 = fonts["system_50"].render(errors, True, colors["red"])
        screen.blit(text1, (10, 0))
        screen.blit(text2, (10, 50))
        screen.blit(text3, (10, 100))
        screen.blit(text4, (10, 150))
        screen.blit(text5, (10, 200))
        screen.blit(text8, (10, 250))
        screen.blit(text9, (screen.get_width() / 2 - text9.get_width() / 2, 300))
        screen.blit(text6, (
            screen.get_width() / 2 - text6.get_width() / 2, screen.get_height() - 2 * text6.get_height()))
        screen.blit(text7, (
            screen.get_width() / 2 - text7.get_width() / 2, screen.get_height() - text7.get_height()))

    def results_screen(self, screen, colors, fonts):
        print(self.errors_dict)
        self.screen_running = True
        self.time = time.time() - self.time
        file = open("statistics.txt", "a")
        file.write("Time " + str(time.strftime("%M:%S", time.gmtime(int(self.time)))) + "; " + str(
            len(self.original_string.string)) + " characters; " + str(self.get_errors()) + " errors; " + str(
            self.get_speed()) + " ch/m; " + str(datetime.datetime.now()) + "\n")
        file.close()
        lis = []
        for i in range(5):
            tmp = max(self.errors_dict.items(), key=operator.itemgetter(1))[0]
            if self.errors_dict[tmp] != 0:
                lis.append(tmp)
                lis.append(self.errors_dict[tmp])
                del self.errors_dict[tmp]
        errors = ""
        for i in range(len(lis)):
            if i % 2 == 0:
                errors += str(lis[i])
            else:
                errors += "(" + str(lis[i]) + ") "
        while self.screen_running:
            self.result_screen_initialization(screen, colors, fonts, errors)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    print(pygame.key.name(event.key))
                    if pygame.key.name(event.key) == "space":
                        return
                    elif pygame.key.name(event.key) == "return":
                        os.system("start " + "statistics.txt")
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def main_screen(self, screen, colors, fonts):
        self.user_string = UserString()
        self.original_string = OriginalString(self.select_file_screen(screen, colors, fonts), self.user_string)
        self.screen_main_running = True
        time1 = time.time()
        while self.screen_main_running:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    self.user_string.update_char(self, event, self.original_string, screen, colors, fonts)
                elif event.type == pygame.QUIT:
                    pygame.quit()

                    quit()
            screen.fill(colors["white"])
            screen.blit(self.keyboard_img, (screen.get_width() / 2 - self.keyboard_img.get_width() / 2,
                                            screen.get_height() / 2 - self.keyboard_img.get_height() / 2))
            text_errors = fonts["system_30"].render("Count of errors = " + str(self.get_errors()), True,
                                                    colors["gray"])
            screen.blit(text_errors, (0, screen.get_height() - text_errors.get_height() - 10))
            if self.time != 0:
                text_time = fonts["system_30"].render(
                    str(time.strftime("%M:%S", time.gmtime(int(time.time() - self.time)))), True,
                    colors["gray"])
                text_speed = fonts["system_30"].render(
                    "{} ch/m".format(int((self.cnt_of_symbols / (time.time() - time1)) * 60)), True, colors["gray"])
            else:
                text_time = fonts["system_30"].render(str(time.strftime("%M:%S", time.gmtime(0))), True,
                                                      colors["gray"])
                text_speed = fonts["system_30"].render("0 ch/m", True, colors["gray"])
            screen.blit(text_time, (
                screen.get_width() / 2 - text_time.get_width() / 2, 0))
            screen.blit(text_speed, (
                screen.get_width() - text_speed.get_width(), screen.get_height() - text_speed.get_height() - 10))
            self.original_string.draw_text(screen, fonts, colors)
            pygame.draw.line(screen, colors["green"],
                             [screen.get_width() * self.original_string.get_progress(), screen.get_height()],
                             [0, screen.get_height()], 10)
            pygame.display.update()
