import pygame

from lbwb.GameCoreData import GameCoreData
from lbwb.util.AssetLoader import AssetLoader
from lbwb.util.Renders import Renders
from lbwb.util.SurfaceModifer import SurfaceModifier


class Plot():

    colrect: pygame.rect.Rect
    name: str
    image_name: str
    image:pygame.surface.Surface

    ix: int
    iy: int

    def __init__(self, name: str, texture_registry:str, image_name: str=""):

        self.name = name

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

        self.image = AssetLoader.loadAssetTexture(registry_name=texture_registry, texture_type="plot", name=aimage_name, picture_type=aimage_type)
    
    def render(self, x:int, y:int, cx:int, cy:int, cz:int, size:int):
        self.ix = x
        self.iy = y
        ppx = x*size*13//16 + cx*size//16 + GameCoreData.DISPLAY_CENTER[0]
        ppx-= y*size* 5//16
        ppy = y*size*10//16 + cy*size//16 + GameCoreData.DISPLAY_CENTER[1]
        
        colx = size* 1//16 + ppx
        coly = size* 6//16 + ppy
        colw = size*13//16
        colh = size*10//16
        self.colrect = pygame.rect.Rect(colx, coly, colw, colh)
        #"""
        modified_image = self.image.copy()
        if self.colrect.collidepoint(pygame.mouse.get_pos()):
            modified_image = SurfaceModifier.brightnessModifier(modified_image, 1.75)
        #"""

        if  -size < ppx and ppx < GameCoreData.display_size_x and \
            -size < ppy and ppy < GameCoreData.display_size_y:
            
            Renders.surfaceRender(modified_image, ppx, ppy, size, size)