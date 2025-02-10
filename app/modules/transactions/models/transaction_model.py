from app.base.Model import Model

class Transaction(Model):
    def __init__(self, name, description, transaciton_type, userId):
        super().__init__()
        self.name = name
        self.description = description,
        self.transaction_type = transaciton_type
        self.userId = userId

