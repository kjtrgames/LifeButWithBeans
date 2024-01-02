import typing
import pygame

from lbwb.GameCoreData import GameCoreData

class Renders():
    @staticmethod
    def textRender(text:str, x:int, y:int, size:int, color:tuple[int, int, int], fonttype:str, iscenter=False):
        pyfonttype = pygame.font.SysFont(fonttype, size)
        renderedtext = pyfonttype.render(text, True, color)

        if iscenter:
            rrx = renderedtext.get_rect().right // 2 #Rendered Rect X position = R R X  ->rrx
            position = (x-rrx, y)
        else:
            position = (x, y)

        GameCoreData.screen.blit(renderedtext, position)


    @staticmethod
    def rectRender(x:int, y:int, width:int, height:int, color:tuple[int, int, int]):
        rects = pygame.Rect(x, y, width, height)
        GameCoreData.screen.fill(color, rects)


    @staticmethod
    def surfaceRender(surface:pygame.surface.Surface, x:int, y:int, width:int, height:int, iscenter:bool=False):
        if iscenter:
            position = (x-width//2, y-height//2)
        else:
            position = (x, y)
        surface = pygame.transform.scale(surface, (width, height))
        return GameCoreData.screen.blit(surface, position)

    """
    @staticmethod
    def titleButtonRender(text, y_index, fonttype, display_data, is_mouse_clicked=False):
        size = loadSettingFile(["any", "font", "button_size"])
        padding_percent = 20#%
        padding_w = display_data["width"]*padding_percent//100
        padding_h = size*padding_percent//100

        height = display_data["height"]//2

        positions = (padding_w+100, height+(size+padding_h)*y_index, display_data["width"]-padding_w*2, size)

        rect = pygame.Rect(positions[0], positions[1], positions[2], positions[3])

        colors = [loadColor(["any", "bgcolor"]), loadColor(["any", "font", "color"])]

        is_this_clicked = False

        if rect.collidepoint(pygame.mouse.get_pos()):
            buttonbg  = colors[0]
            fontcolor = colors[1]
            if is_mouse_clicked:
                is_this_clicked = True
                # Q. Why use this valiable?
                # A. Beacuse, catch click event.
        else:
            buttonbg  = colors[1]
            fontcolor = colors[0]

        rectRender(screen, positions[0], positions[1], positions[2], positions[3], buttonbg)
        textRender(screen, text, (display_data["width"]//2+100), (positions[1]+size*1//8), (size*3//4), fontcolor, fonttype, iscenter=True)
        return is_this_clicked
    #"""