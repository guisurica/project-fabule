import uuid
import datetime

class Model:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = None