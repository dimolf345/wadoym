import uuid


class Card:
    @staticmethod
    def random_code():
        return uuid.uuid4().hex

    def __init__(self, name=None, code=None, background_color="173f5f"):
        self.code = self.random_code() if not code else code
        self.name = name
        self.background_color = background_color


class TextCard(Card):
    def __init__(self, text, text_color="f1faee", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = text
        self.text_color = text_color


class MemeCard(Card):
    def __init__(self, image_url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_url = image_url


class Freestyle(TextCard):
    def __init__(self, *args, text="Freestyle!", **kwargs):
        super().__init__(*args, text=text, **kwargs)