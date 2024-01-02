import typing
import pygame

class AssetLoader():

    _ConvLevel = typing.Literal[None, "", "convert", "convert_alpha"]

    @staticmethod
    def loadAssetTexture(registry_name: str, texture_type: str, name: str, picture_type: str = "png", convertlevel:_ConvLevel = None) -> pygame.surface.Surface:
        match convertlevel:
            case "convert_alpha": return pygame.image.load(f"assets/{registry_name}/textures/{texture_type}/{name}.{picture_type}").convert_alpha()
            case "convert"      : return pygame.image.load(f"assets/{registry_name}/textures/{texture_type}/{name}.{picture_type}").convert()
            case _              : return pygame.image.load(f"assets/{registry_name}/textures/{texture_type}/{name}.{picture_type}")