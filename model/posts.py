from model import Model


class Post(Model):
    def __init__(self, data):
        super().__init__(data)
        self.coser = data.get('coser', 'None')
        # cid means coser id
        self.cid = data.get('cid', 'None')
        self.description = data.get('description', 'None')
