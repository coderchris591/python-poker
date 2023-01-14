class Player:
    def __init__(self, ID, position, stack, bet_size, folded=False):
        self.ID = ID
        self.position = position
        self.stack = stack
        self.bet_size = bet_size
        self.folded = folded
        self.hole_cards = []

    def update_position(self, number_of_players):
        if self.position == number_of_players:
            self.position = 0
        else:
            self.position = self.position + 1
        return

    def update_stack(self, bet):
        self.stack += bet
        return

    def update_hole_cards(self, cards):
        self.hole_cards = cards
        return

    def update_folded_status(self, folded):
        self.folded = folded
        return

    def update_bet_size(self, bet):
        self.bet_size = bet
        return


preflop_positions = {5: 'UTG',  6: 'Middle Position', 4: 'Cutoff', 3: 'Button', 2: 'Small Blind', 1: 'Big Blind'}
number_of_players = 5
if number_of_players < 6:
    count = 6 - number_of_players
    for i in range(count):
        preflop_positions.pop(6 - i)

new = Player(69, 1, 1500, 0)

print(preflop_positions[new.position])
new.update_position(number_of_players)
print(preflop_positions[new.position])
