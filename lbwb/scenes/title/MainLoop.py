import pygame

from lbwb.GameCoreData import GameCoreData
from synfpyg.util.Renders import Renders

class MainLoop:

    title_bg = pygame.image.load("assets/lbwb/textures/title/titlebg.png").convert()

    def render():
        Renders.surfaceRender(MainLoop.title_bg, 0, 0, GameCoreData.display_size_x, GameCoreData.display_size_y)#TODO 縦横比固定
        #TODO スタートボタンを実装する