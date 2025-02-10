class Result:
    def __init__(self, code: int = None, message: str = None, ok: bool = None):
        self.code = code
        self.message = message
        self.ok = ok

    def ok_result(message: str, code: int):
        return Result(code, message, True)

    def not_ok_result(message: str, code: int):
        return Result(code, message, False)
    



