import typing
import pygame

from lbwb.GameCoreData import GameCoreData
from lbwb.item.Item import Item
from lbwb.util.AssetLoader import AssetLoader
from lbwb.util.HelpfulFuncs import HelpfulFuncs
from lbwb.util.SurfaceModifer import SurfaceModifier
from lbwb.util.Renders import Renders

class ItemGroup():
    has_item:list[Item]
    index:str
    def __init__(self, name:str, texture_registry:str, image_name: str=""):
        
        self.name = name
        self.has_item = []

        if image_name == "":
            self.image_name = name + ".png"
            aimage_name = name # asset image name
            aimage_type = "png"
        else:
            self.image_name = image_name
            image_split = image_name.split(".")
            aimage_name = ".".join(image_split[0:-1])
            aimage_type = image_split[-1]
            del image_split

        self.image = AssetLoader.loadAssetTexture(registry_name=texture_registry, texture_type="item/group", name=aimage_name, picture_type=aimage_type)
    
    def __list__(self) -> list[Item]:return self.has_item
    
    def render(self, y:int):
        modified_image = self.image.copy()
        rect_tuple:tuple[int, int, int, int] = (0, y, GameCoreData.itembar_width, GameCoreData.itembar_width)
        rects = pygame.rect.Rect(*rect_tuple)
        
        Renders.surfaceRender(modified_image, *rect_tuple)
        if rects.collidepoint(pygame.mouse.get_pos()):
            SurfaceModifier.brightnessModifier(modified_image, 1.5)
        
        if rects.collidepoint(pygame.mouse.get_pos()):
            itembar_bg = pygame.surface.Surface((GameCoreData.display_size_x-GameCoreData.itembar_width, GameCoreData.itembar_width,))
            itembar_bg.fill(HelpfulFuncs.htColorCodeTranslater("#000"))
            itembar_bg.set_alpha(128)
            Renders.surfaceRender(itembar_bg, GameCoreData.itembar_width, y, itembar_bg.get_width(), itembar_bg.get_height())
            self._renderTheItemItHas(y)
    
    def _renderTheItemItHas(self, y:int):
        for index in range(len(self.has_item)):
            self.has_item[index].render(x=GameCoreData.itembar_width*(index+1), y=y)
        
        
    def appendGroup(self, item):
        self.has_item.append(item)