class ErrorBaseForSynf(Exception):
    message:str = ""
    def __init__(self, *args) -> None:
        super().__init__(self.message, *args)