import random
import uuid
from round import Round
from loaders import Loader


class NullWaiter:
    def wait(self, timeout, callback):
        pass

    def stop(self):
        pass


class GameContext:
    def __init__(self, players, meme_deck=[], deck=[]):
        self.meme_deck = meme_deck
        self.deck = deck
        self.waiter = NullWaiter()
        self.scores = {player: 0 for player in players}

    def shuffle(self):
        for _ in range(3):
            random.shuffle(self.deck)
        for _ in range(3):
            random.shuffle(self.meme_deck)


class Session:
    @staticmethod
    def random_code():
        return "ABC"  # TODO

    def __init__(self, loader_factory=Loader):
        self.code = self.random_code()
        self.players = []
        self.rounds = []
        self.loader = loader_factory()
        self.context = GameContext(self.players, meme_deck=self.loader.load_memes(), deck=self.loader.load_cards())

    def add_player(self, player):
        self.players.append(player)

    def start(self):
        self.context.shuffle()
        for player in self.players:
            player.draw(self.context.deck, count=7)
        self.next()

    def next(self):
        last_round = self.rounds[-1] if self.rounds else None
        if last_round:
            judge = last_round.winner[1]
            players = [p for p in self.players if p != judge]
            seq = last_round.seq + 1
            next_round = Round(players, judge, seq)
        else:
            next_round = Round(self.players)
        self.rounds.append(next_round)
        next_round.start(self.context)
