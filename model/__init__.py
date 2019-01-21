class Model(object):
    def __init__(self, data):
        self.id = data.get('id', 'None')
        self.url = data.get('url', 'None')

    def __repr__(self):
        result = [f'{k}: {v}' for k, v in self.__dict__.items()]

        return '\n'.join(result)
