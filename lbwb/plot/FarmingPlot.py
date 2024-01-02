import importlib

from lbwb.plot.Plot import Plot

class FarmingPlot(Plot):
    
    def __init__(self, name: str, tobe, whentobe: int, texture_registry:str, image_name:str = ""):
        super().__init__(name=name, texture_registry=texture_registry, image_name=image_name)
        self.count = 0
        self.tobe = tobe #TODO Use ReturnScript and this class will be Plot
        self.whentobe = whentobe

    def render(self, x: int, y: int, cx: int, cy: int, cz: float):
        super().render(x=x, y=y, cx=cx, cy=cy, cz=cz)
        self.count += 1
        if self.whentobe == self.count:
            CoreData = importlib.import_module("lbwb.scenes.farm.CoreData")
            CoreData.CoreData.setPlotWithPos(self.ix, self.iy, self.tobe) # TODO (MAPPP) to be changeable registry