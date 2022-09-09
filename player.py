from faker import Faker


class Player:
    def __init__(self, name=Faker().name()):
        self.name = name
        self.balance = 3000
        self.cards = []
        self.bet = 0
        self.values = 0

    def player_win(self, bet):
        self.balance += bet
        return f"Você ganhou {bet}"

    def player_lose(self, bet):
        self.balance -= bet
        return f'Você perdeu {bet}'
