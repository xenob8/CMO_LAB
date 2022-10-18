class GuiElement:
    def __init__(self, type):
        self.values = [0]
        self.texts = [None]
        self.type = type

    def add(self, val, text=None):
        self.values.append(0.7*val)
        self.texts.append(text)

    def change_current(self, new_val, text=None):
        self.values[-1] = 0.7*new_val
        self.texts[-1] = text
