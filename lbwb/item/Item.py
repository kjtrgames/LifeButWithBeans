import pygame
from lbwb.GameCoreData import GameCoreData

from lbwb.util.AssetLoader import AssetLoader
from lbwb.util.Renders import Renders
from lbwb.util.SurfaceModifer import SurfaceModifier

class Item():
    
    name: str
    image_name: str
    image: pygame.surface.Surface
    
    def __init__(self, name: str, texture_registry: str, image_name: str=""):

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

        self.image = AssetLoader.loadAssetTexture(registry_name=texture_registry, texture_type="item", name=aimage_name, picture_type=aimage_type)
        
        
    def render(self, x:int, y:int):
        padding = GameCoreData.itembar_width* 2//16
        
        x+=padding
        y+=padding
        s =GameCoreData.itembar_width-padding*2
        
        Renders.surfaceRender(self.image, x=x, y=y, width=s, height=s)
        