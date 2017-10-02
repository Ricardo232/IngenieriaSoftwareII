class KeyHandler:

    def __init__(self):
        self.mov_keyspressed = {}
        self.action_keyspressed = {}

    def keyreleased(self, keyname, _list):
        _list[keyname] = False

    def keypressed(self, keyname, _list):
        _list[keyname] = True

    def get_keynames(self, _list):
        names = []
        for key, value in _list.items():
            if value == True:
                names.append(key)

        return names
