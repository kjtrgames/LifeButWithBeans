import pygame
import sys
import importlib

from lbwb.GameCoreData import GameCoreData
from synfpyg.util.AssetLoader import AssetLoader
from synfpyg.util.HelpfulFuncs import HelpfulFuncs


class GameMainLoop():

    def __init__(self) -> None:
        pygame.init()

        self.timer = pygame.time.Clock()
        pygame.display.set_icon(AssetLoader.loadAssetTexture("lbwb", "logo", "icon"))
        pygame.display.set_caption(u"もやし生活")

    def get_to_mainloop(self) -> None:
        print(f"{sys.path}")
        while True:
            #"""
            events = pygame.event.get()
            for event in events:
            #"""
            #if pygame.QUIT in pygame.event.get():
            #"""
                if event.type == pygame.QUIT:  # quit event
                    pygame.quit()  # Close pygame window
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    GameCoreData.reCalcXY()
            #exec("import " + scene_resistry + ".scenes." + scene)
            #afterdo = eval(scene_resistry + ".scenes." + scene + ".render(GameCoreData.screen)")
            sceneobj = importlib.import_module(GameCoreData.getSceneName())
            sceneobj.MainLoop.render()

            pygame.display.update()
            self.timer.tick(30)
            #self.timer.tick(1)