# Chris Martinez
# Python Poker Project

from player import Player
import random

playing_cards = {
    'Ac': 1, 'Ad': 1, 'Ah': 1, 'As': 1,
    '2c': 1, '2d': 1, '2h': 1, '2s': 1,
    '3c': 1, '3d': 1, '3h': 1, '3s': 1,
    '4c': 1, '4d': 1, '4h': 1, '4s': 1,
    '5c': 1, '5d': 1, '5h': 1, '5s': 1,
    '6c': 1, '6d': 1, '6h': 1, '6s': 1,
    '7c': 1, '7d': 1, '7h': 1, '7s': 1,
    '8c': 1, '8d': 1, '8h': 1, '8s': 1,
    '9c': 1, '9d': 1, '9h': 1, '9s': 1,
    '10c': 1, '10d': 1, '10h': 1, '10s': 1,
    'Jc': 1, 'Jd': 1, 'Jh': 1, 'Js': 1,
    'Qc': 1, 'Qd': 1, 'Qh': 1, 'Qs': 1,
    'Kc': 1, 'Kd': 1, 'Kh': 1, 'Ks': 1
}

# INPUT
number_of_players = int(input("Please enter the number of players: "))

# GLOBAL VARIABLES
list_of_players = []
STACK_SIZE = 1500
choices = ['check', 'call', 'raise', 'fold', 'bet']
positions = {2: 'Small Blind', 1: 'Big Blind', 5: 'UTG', 6: 'Middle Position', 4: 'Cutoff', 3: 'Button'}


def main():
    # determine positions
    if number_of_players < 6:
        count = 6 - number_of_players
        for i in range(count):
            positions.pop(6 - i)
    # POPULATE PLAYERS
    count = 0
    while count <= number_of_players - 1:
        # set player id, position, and stack size
        new_player = Player(count, count+1, STACK_SIZE, 0)
        count += 1
        # append new player to list
        list_of_players.append(new_player)
    # print players
    # for player in list_of_players:
    #     print(player.ID, positions[player.position], player.stack, player.bet_size, player.folded, player.hole_cards)

    simulate_round()

    # reset player status
    # for player in list_of_players:
    #     player.update_player_status('none')


# deal hole cards to each player
def deal_cards():
    for player in list_of_players:
        cards = []
        for i in range(2):
            card = get_random_card()
            cards.append(card)
            player.update_hole_cards(cards)


# update pot with bet amount
def update_pot(bet, pot):
    pot = pot + bet
    return pot


# get random card
def get_random_card():
    while True:
        card, in_use = random.choice(list(playing_cards.items()))
        if in_use == 1:
            break
    return card


# check if all players call
def all_players_call(bet):
    for player in list_of_players:
        if not player.folded:
            if player.bet_size != bet:
                return False
    return True


# get preflop choice from player
def get_preflop_choice(call_amount):
    if call_amount == 0:
        print("Please select a choice.")
        print("1) ", choices[1])  # call
        print("2) ", choices[2])  # raise
        choice = int(input(">> "))
    else:
        print("Please select a choice.")
        print("1) ", choices[1])  # call
        print("2) ", choices[2])  # raise
        print("3) ", choices[3])  # fold
        choice = int(input(">> "))
    return choice


# get post flop choice from player
def get_postflop_choice():
    return


def simulate_round():
    # deal hole cards
    deal_cards()
    # take blinds
    small_blind = 25
    big_blind = 50
    for player in list_of_players:
        if player.position == len(list_of_players) - 2:
            player.update_bet_size(small_blind)
            player.update_stack(-small_blind)
        elif player.position == len(list_of_players) - 1:
            player.update_bet_size(big_blind)
            player.update_stack(-big_blind)
    # print player instances
    for player in list_of_players:
        print(player.ID, positions[player.position], player.stack, player.bet_size, player.folded, player.hole_cards)
    # create pot
    pot = small_blind + big_blind
    # track round number
    round = 0
    print("\nPreflop")
    # start preflop
    current_bet = 50
    # check if players have called
    while not all_players_call(current_bet):
        # loop through players
        for player in list_of_players:
            # how much to call
            call_amount = current_bet - player.bet_size
            # check if player has folded
            if player.folded:
                continue
            print("\nPot: ", pot)
            print("Turn: ", positions[player.position])
            print("Stack size: ", player.stack)
            print("Hole cards: ", player.hole_cards)
            print(call_amount, "to call")
            # get preflop choice
            choice = get_preflop_choice(call_amount)
            # choice: call
            if choice == 1:
                print("player calls", current_bet)
                player.update_bet_size(current_bet)
                player.update_stack(-current_bet)
                pot = update_pot(current_bet, pot)
                # choice: raise
            elif choice == 2:
                print("player raises")
                current_bet = int(input("How much would you like to bet? "))
                player.update_stack(-current_bet)
                player.update_bet_size(current_bet)
                pot = update_pot(current_bet, pot)
                # choice: fold
            elif choice == 3:
                print("player folds")
                player.update_folded_status(True)
    for player in list_of_players:
        print(player.id, player.position, player.stack, player.bet_size, player.folded, player.hole_cards)
    # loop for 3 rounds
    print("\nPostflop")
    while round < 3:
        round = + 1
        get_postflop_choice()


main()
