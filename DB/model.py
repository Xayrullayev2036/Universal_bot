from DB.config import DB


class Users(DB):
    def __init__(self, **fields):
        self.fields = fields


class Admin(DB):
    def __init__(self, **fields):
        self.fields = fields


class News(DB):
    def __init__(self, **fields):
        self.fields = fields
