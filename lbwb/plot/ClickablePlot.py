import abc
import types
import pygame

from lbwb.plot.Plot import Plot

class ClickablePlot(Plot):

    def __init__(self, name: str, tobe:Plot, texture_registry:str, if_click:types.FunctionType = types.FunctionType, image_name: str = ""):
        super().__init__(name, texture_registry, image_name)
        self.tobe = tobe #TODO Use ReturnScript and this class will be Plot
        self.if_click = if_click

    
    
    def render(self, x: int, y: int, cx: int, cy: int, cz: int):
        super().render(x, y, cx, cy, cz)
        if self.colrect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]: # TODO Item/ItemGroupとの当たり判定問題の解決
            self.if_click(self)
            """
            CoreData = importlib.import_module("lbwb.scenes.farm.CoreData")
            CoreData.CoreData.setPlotWithPos(self.ix, self.iy, self.tobe) # TODO (MAPPP) to be changeable registry
            #"""

    @abc.abstractmethod
    def if_click():
        pass