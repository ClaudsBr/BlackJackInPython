class Dealer:

    def __init__(self):
        self.name = "Dealer"
        self.balance = 100000
        self.cards = []
        self.bet = 0
        self.values = 0

    def dealer_win(self, bet):
        self.balance += bet

    def dealer_lose(self, bet):
        self.balance -= bet