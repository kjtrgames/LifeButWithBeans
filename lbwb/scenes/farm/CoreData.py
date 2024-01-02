import typing
from lbwb.plot.Plot import Plot
from lbwb.item.Item import Item
from lbwb.item.ItemGroup import ItemGroup

class CoreData():
    map: list[list[Plot]]
    _has_igroup: int = 0
    igroups:list[ItemGroup] = [None, None]
    
    beans:dict[str, dict[str, list[int, list[bool, bool]]]] = {}
    #    :    :    :    :    :    :
    #    :save crops data    :    :
    #         :save crops registry
    #                   :save crops name
    #                        :save other data of the crops
    #                             :save that how many crops you have
    #                                   :save whether this are crops, beans, seeds or other...
    #                       saleable | plantable 
    #                               0, 0        ->beans
    #                               0, 1        ->crops
    #                               1, 0        ->seeds
    #                               1, 1        ->others
    #                   ("No ploblem!"=0, "Are you stupid!?"=1)
    # Huh? "Seed is able to sale! Am not I stupid?" PLAYER CANNOT SALE SEEDS IN LBWB WORLD!! Am I stupid?
    selected_beans:str
    
    @staticmethod
    def setMap(new_map:list[list[Item]]) -> None: CoreData.map = new_map
    
    @staticmethod
    def getPlotWithPos(ix:int, iy:int) -> Plot: return CoreData.map[iy][ix]
    @staticmethod
    def setPlotWithPos(ix:int, iy:int, new:Plot) -> None: CoreData.map[iy][ix] = new
    
    @staticmethod
    def beanRegister():
        pass
    
    @staticmethod
    def getMapSizeX() -> int: return len(CoreData.map[0])
    @staticmethod
    def getMapSizeY() -> int: return len(CoreData.map)
    