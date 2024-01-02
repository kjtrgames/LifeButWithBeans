from lbwb.plot.Plot import Plot
from lbwb.plot.FarmingPlot import FarmingPlot
from lbwb.plot.ClickablePlot import ClickablePlot
from lbwb.scenes.farm.CoreData import CoreData


class Plots():
    def __init__(self):
        
        def test2_act(self:ClickablePlot):
            CoreData.setPlotWithPos(self.ix, self.iy, self.tobe)
            print("TEST2 got EMPTY")
        
        self.EMPTY:Plot = Plot(name="empty", texture_registry="lbwb", image_name="empty.png")
        self.TEST:Plot = Plot(name="test", texture_registry="lbwb", image_name="test.png")
        self.TEST2:Plot = ClickablePlot(name="test2", texture_registry="lbwb", tobe=self.EMPTY, image_name="test.png", if_click=test2_act)