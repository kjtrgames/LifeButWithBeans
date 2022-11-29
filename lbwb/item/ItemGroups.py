from lbwb.item.ItemGroup import ItemGroup
from lbwb.scenes.farm.CoreData import CoreData

class ItemGroups():
    @staticmethod
    def _register(igroup:ItemGroup, index:int=-1)-> ItemGroup:
        CoreData.igroups[index] = igroup
        igroup.index = index
        return igroup
    BEANS:ItemGroup = _register(ItemGroup("beans", texture_registry="lbwb", image_name="beans.png"), 0)
    TEST:ItemGroup = _register(ItemGroup("ig_test",texture_registry="lbwb", image_name="test.png"), 1)