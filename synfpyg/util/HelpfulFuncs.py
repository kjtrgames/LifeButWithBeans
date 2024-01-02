import pygame

class HelpfulFuncs():
    
    @staticmethod
    def htCCT(htvalues:str):
        if htvalues[0]=="#": htvalues = htvalues[1:]
        else: raise ValueError
        
        match len(htvalues):
            case 3:
                red   = int(htvalues[0]*2, 16)
                green = int(htvalues[1]*2, 16)
                blue  = int(htvalues[2]*2, 16)
            case 6:
                red   = int(htvalues[ :2], 16)
                green = int(htvalues[2:4], 16)
                blue  = int(htvalues[4: ], 16)
            case _:
                raise ValueError
        return pygame.color.Color(red, green, blue)
