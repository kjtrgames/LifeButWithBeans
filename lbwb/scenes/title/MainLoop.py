import pygame

from lbwb.GameCoreData import GameCoreData
from lbwb.util.Renders import Renders


title_bg = pygame.image.load("assets/lbwb/textures/title/titlebg.png").convert()

def render():
    Renders.surfaceRender(GameCoreData.screen, title_bg, 0, 0, GameCoreData.DISPLAY_SIZE_X, GameCoreData.display_size_y)
    #TODO スタートボタンを実装する