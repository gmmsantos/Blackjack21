class Chips:
    def __init__(self):
        self.total = 100  # Valor inicial padrao, pode ser alterado, ou substituido por um input self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
