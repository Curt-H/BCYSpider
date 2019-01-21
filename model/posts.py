from model import Model


class Post(Model):
    def __init__(self, data):
        super().__init__(data)
        self.title = data.get('title', 'None')
        self.tag = data.get('tag', 'None')
