import pygame

class GameCoreData():
    """
    GameCoreData
    ------------
    This class is used to store core game data."""
    display_size_x, display_size_y = 1080, 720
    display_center = (display_size_x//2, display_size_y//2)
    scene_resistry = "lbwb"
    scene = "title"#TODO titleから始め、プレイボタンを追加
    scene = "farm"
    
    itembar_width  = display_size_x* 2//16
    itembar_height = display_size_y* 2//16
    
    screen = pygame.display.set_mode((display_size_x, display_size_y), flags=pygame.RESIZABLE)
    
    quitmsg:bool = True
    
    @classmethod
    def reCalcXY(self):
        self.display_size_x, self.display_size_y= pygame.display.get_window_size()
        self.itembar_width  = self.display_size_x* 2//16
        self.itembar_height = self.display_size_y* 2//16
        
    @classmethod
    def getSceneName(self) -> str: return f"{self.scene_resistry}.scenes.{self.scene}.MainLoop"
    
    @classmethod
    def setScene(self, registry:str="lbwb", scene:str=None) -> None:
        self.scene_resistry = registry
        self.scene = scene
        return None