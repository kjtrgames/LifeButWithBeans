import abc

class AbstractScene(abc.ABC):
    class CoreData: pass
    class MainLoop:
        def __init__(self): raise TypeError(f"'{self.__class__.__name__}' is not callable")
        
        @staticmethod
        def render(): pass