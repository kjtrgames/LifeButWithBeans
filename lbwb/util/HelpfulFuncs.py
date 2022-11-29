import pygame

class HelpfulFuncs():
    
    @staticmethod
    def htColorCodeTranslater(htvalues:str):
        htvalues = htvalues[1:]
        rgblen = len(htvalues)//3
        red = int(htvalues[:rgblen], 16) * (256 // 16**rgblen)
        green = int(htvalues[rgblen:rgblen*2], 16) * (256 // 16**rgblen)
        blue = int(htvalues[rgblen*2:], 16) * (256 // 16**rgblen)
        return pygame.color.Color(red, green, blue)