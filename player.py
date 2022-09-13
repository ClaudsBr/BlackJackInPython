from faker import Faker


class Player:
    def __init__(self, name=Faker().name()):
        self.name = name
        self.balance = 3000
        self.cards = []
        self.bet = 0
        self.values = 0

    def player_win(self, bet):
        return f"Você ganhou {bet}"
        self.balance += bet

    def player_lose(self, bet):
        return f'Você perdeu {bet}'
        self.balance -= bet




    def __str__(self):
        string_de_retorno = f"Jogador: {self.name}\n"
        for carta in self.cards:
            string_de_retorno += f'{carta}\n'
        string_de_retorno += f'Mão: {self.values}\nSaldo: {self.balance}'
        return string_de_retorno

