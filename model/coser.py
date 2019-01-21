from model import Model


class Coser(Model):
    def __init__(self, data):
        super().__init__(data)
        self.id = data.get('id', 'None')
        self.name = data.get('name', 'None')
        self.posts = list()
