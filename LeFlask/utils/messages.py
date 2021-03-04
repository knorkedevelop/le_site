class Error(Exception):
    codes = {
        "ERROR": "Hat nicht funktioniert.",
    }

    def __init__(self, error_code):
        self.error_code = error_code
        self.message = self.codes[error_code]

    def asdict(self):
        return {"error_code": self.error_code, "message": self.message}


class Success(Exception):
    codes = {
        "SUCCESS": "Hat funktioniert.",
    }

    def __init__(self, succes_code):
        self.message = self.codes[succes_code]

    def asdict(self):
        return {"message": self.message}
