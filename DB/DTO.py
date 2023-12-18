class AdminDTO:
    def __init__(self, id: int, name: str, password: str):
        self.id = id
        self.name = name
        self.password = password


class NewsDTO:
    def __init__(self, id: int, image: str, image_text: str):
        self.id = id
        self.image = image
        self.image_text = image_text


class UsersDTO:
    def __init__(self, id: int, fullname: str, username: str, userid: str):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.userid = userid
