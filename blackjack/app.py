from blackjack.game.deck import Deck
from blackjack.game.chips import Chips
from blackjack.game.hand import Hand
from blackjack.common.game_round_settings import (
    take_bet,
    show_some,
    hit_or_stand,
    player_busts,
    player_wins,
    hit,
    show_all,
    dealer_busts,
    dealer_wins,
    push,
)


def run():
    playing = True

    while True:
        print("Welcome to BlackJack!")

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal_one())
        player_hand.add_card(deck.deal_one())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal_one())
        dealer_hand.add_card(deck.deal_one())

        player_chips = Chips()  # default value is 100

        take_bet(player_chips)

        # Show cards
        show_some(player_hand, dealer_hand)

        while playing:
            # Hit or Stand
            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # play Dealer's hand until Dealer= 17
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

        # Inform Player chips total
        print("\nPlayer's winnings stand at", player_chips.total)

        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

        if new_game[0].lower() == "y":
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break
