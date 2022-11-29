from lbwb.item.Item import Item
from lbwb.item.ItemGroup import ItemGroup
from lbwb.item.ItemGroups import ItemGroups


class Items():
    @staticmethod
    def _register(item:Item, igroup:ItemGroup):
        igroup.appendGroup(item)
        return item
    
    GREEN_BEANS = _register(Item(name="green_beans", texture_registry="lbwb", image_name="green_bean.png"), ItemGroups.BEANS)