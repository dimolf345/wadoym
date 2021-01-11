from pymongo import MongoClient

from cards import MemeCard, TextCard, Freestyle


class Loader:
    def load_memes(self):
        return []

    def load_cards(self):
        return []


class MongoLoader(Loader):
    def __init__(self, mongo_url, meme_collection="memes", cards_collection="cards"):
        self.client = MongoClient(mongo_url)
        self.db = self.client.get_database()
        self.meme_collection = meme_collection
        self.cards_collection = cards_collection

    @property
    def memes(self):
        return getattr(self.db, self.meme_collection)

    @property
    def cards(self):
        return getattr(self.db, self.cards_collection)

    def _meme(self, document):
        return MemeCard(
            name=document.name, 
            code=document.code,  
            background_color=document.background_color, 
            image_url=document.image_url
        )

    def _card(self, document):
        if document.type == "text":
            return TextCard(
                text=document.text,
                name=document.name, 
                code=document.code, 
                background_color=document.background_color, 
                text_color=document.text_color
            )
        elif document.type == "freestyle":
            return Freestyle()

    def load_memes(self):
        return [self._meme(doc) for doc in self.memes.find()]

    def load_cards(self):
        return [self._card(doc) for doc in self.cards.find() if self._card(doc)]