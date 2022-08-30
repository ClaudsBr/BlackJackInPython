from faker import Faker


class Player:
    def __init__(self, name=Faker().name()):
        self.name = name
        self.balance = 3000
        self.cards = []
