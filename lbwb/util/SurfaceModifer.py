import pygame

class SurfaceModifier():
    @staticmethod
    def brightnessModifier(surface:pygame.surface.Surface, brightness:float) -> pygame.surface.Surface:#TODO Useable alpha
        #"""
        pxlarray = pygame.PixelArray(surface.convert_alpha())
        for y in range(surface.get_height()):
            for x in range(surface.get_width()):
                clr = pygame.color.Color(surface.unmap_rgb(pxlarray[x][y]))
                alp = clr.a
                clr = clr.correct_gamma(2-brightness) if alp!=0 else clr
                pxlarray[x][y] = clr
        return_surface = pxlarray.make_surface()
        del pxlarray
        return return_surface
        #"""