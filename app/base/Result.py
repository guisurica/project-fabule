class Result:
    def __init__(self, code: int = None, message: str = None, ok: bool = None):
        self.code = code
        self.message = message
        self.ok = ok

    def ok_result(self, message: str, code: int):
        self.code = code
        self.message = message
        self.ok = True
        return self

    def not_ok_result(self, message: str, code: int):
        self.code = code
        self.message = message
        self.ok = False
        return self
    



