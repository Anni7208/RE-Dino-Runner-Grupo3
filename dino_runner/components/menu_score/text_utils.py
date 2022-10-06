from tkinter import CENTER
import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = "freesansbold.ttf"
black_color = (0,0,0)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 25)

    text =font.render("POINTS:" + str(points), True, black_color)
    text.rect = text.get_rect()
    text_rect.center = (1000, 48)

    return text, text_rect


def get_center_message(message, width = SCREEN_WIDTH // 2, heigth = SCREEN_HEIGHT //2):
    font = pygame.font.Font(FONT_STYLE, 35)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, heigth)
    return text, text_rect


