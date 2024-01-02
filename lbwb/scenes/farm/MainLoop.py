import pygame


from lbwb.GameCoreData import GameCoreData
from lbwb.item.Items import Items
from lbwb.plot.Plots import Plots
from synfpyg.util.HelpfulFuncs import HelpfulFuncs
from synfpyg.util.Renders import Renders

from lbwb.scenes.farm.CoreData import CoreData


#TODO(MAPPP) MODクラスを作成しそれを受け取る



cx:int = 0
cy:int = 0
cz:int = 16
# camera x

cmx:int = 0 # camera move x
cmy:int = 0
cmz:int = 0
move_range:int = 1
slipperiness:int = 0.8
count:int = 0

class MainLoop:
    def __init__():
        CoreData.setMap([
            [Plots().TEST, Plots().TEST, Plots().TEST, Plots().TEST],
            [Plots().TEST, Plots().EMPTY,Plots().EMPTY,Plots().TEST],
            [Plots().TEST, Plots().EMPTY,Plots().EMPTY,Plots().TEST],
            [Plots().TEST, Plots().TEST, Plots().TEST2,Plots().TEST]
        ])
    
    def render():
        GameCoreData.screen.fill(HelpfulFuncs.htCCT("#00ff00"))
        MainLoop._cameraMover()

        MainLoop._plotsRender()

        MainLoop._guiRender()

    def _cameraMover():
        global cx, cy, cz, cmx, cmy, cmz, move_range, slipperiness
        key_events = pygame.key.get_pressed()

        cmx = (key_events[pygame.K_d] - key_events[pygame.K_a]) * move_range
        cmy = (key_events[pygame.K_s] - key_events[pygame.K_w]) * move_range
        cmz = (key_events[pygame.K_q] - key_events[pygame.K_e]) * move_range

        cx += cmx
        cy += cmy
        cz += cmz
        if cz <=4:
            cz =4
            cmz=0
        cx += cmz
        cy += cmz


    def _plotsRender():
        global cx, cy, cz


        #"""
        for ix in range(CoreData.getMapSizeX()):
            for iy in range(CoreData.getMapSizeY()):
                CoreData.getPlotWithPos(ix, iy).render(x=ix, y=iy, cx=cx, cy=cy, cz=cz)#ReturneD Function

    def _guiRender():
        sipy = max(0, (GameCoreData.itembar_height-GameCoreData.itembar_width)//2)
        #selected_item_pos_y
        MainLoop._itembarRender(sipy)
        MainLoop._itemsRender(sipy)

    def _itembarRender(sipy):
        Renders.rectRender(0, 0, GameCoreData.itembar_width , GameCoreData.display_size_y, HelpfulFuncs.htCCT("#434"))
        Renders.rectRender(0, 0, GameCoreData.display_size_x, GameCoreData.itembar_height, HelpfulFuncs.htCCT("#767"))
        Renders.rectRender(0,sipy,GameCoreData.itembar_width, GameCoreData.itembar_width, HelpfulFuncs.htCCT("#ccc"))
        #TODO visible numbers of Beans and Money

    def _itemsRender(sipy):
        igroups = CoreData.igroups
        for index in range(len(igroups)):
            igroups[index].render(
                GameCoreData.itembar_width*index+(GameCoreData.itembar_width if GameCoreData.display_size_x>=GameCoreData.display_size_y else GameCoreData.itembar_height)
            )