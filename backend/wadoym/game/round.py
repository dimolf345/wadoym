import random


class Round:
    def __init__(self, players, judge=None, seq=0, timeout=90, judge_timeout=180):
        self.seq = 0
        self.timeout = timeout
        self.judge_timeout = judge_timeout
        self.players = players.copy()
        self.judge = judge
        self.meme = None
        self.play_enabled = False
        self.judge_enabled = False
        self.played = {}
        self.winner = None
        self.context = None
        self.waiter = None

    def start(self, context):
        self.context = context
        self.waiter = context.waiter
        self.make_judge()
        self.draw_meme()
        self.start_round()

    def make_judge(self):
        if self.judge:
            return
        self.judge = random.choice(self.players) # TODO: make turns
        self.players.remove(self.judge)

    def draw_meme(self):
        self.meme = self.context.meme_deck.pop(0)
    
    def start_round(self):
        self.play_enabled = True
        self.waiter.wait(timeout=self.timeout, callback=self.stop_round)

    def play(self, player, card):
        self.played[player.code] = card
        if all(((player in self.played) for player in self.players)):
            self.waiter.stop()
            self.stop_round()

    def stop_round(self):
        self.play_enabled = False
        self.judge_enabled = True
        self.waiter.wait(timeout=self.judge_timeout, callback=self.stop_judging)

    def judge_winner(self, card):
        self.waiter.stop()
        winner = {c: player for player, c in self.played.items()}[card]
        self.winner = (card, winner)
        self.end()

    def stop_judging(self):
        self.winner = None
        self.end()

    def end(self):
        self.judge_enabled = False
        self.give_points()
        self.deal()

    def give_points(self):
        if self.winner:
            self.context.scores[self.winner] += 1
    
    def deal(self):
        for player in self.players:
            player.draw(self.context.deck)
