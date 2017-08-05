#!/usr/bin/env python

"""A simple text-based Blackjack game."""

import sys
import time

from cards import Card, Shoe, Hand
from players import Player, Dealer


class Game:
    """
    Holds the shoe, the players, and the logic for going through the game.

    Parameters
    ----------
    dealer: Dealer
            The Dealer of the game.
    shoe: Shoe
          Shoe containing cards for use in the game.
    players: tuple of Player
             Sequence of Players playing the game.

    """

    def __init__(self, *players):
        self.dealer = Dealer()
        self.shoe = Shoe()
        if not players:
            raise ValueError("No players entered.")
        self.players = [Player(player) for player in players]

    def start_screen(self):
        """Start screen for the game."""
        print("\n" + "#"*79 + "\n"
              + "BLACKJACK".center(79) + "\n"
              + "#"*79)
        print("RULES".center(79) + "\n"
              + ("-"*5).center(79))
        print("*Standard Blackjack Rules apply."
              "\n*Six decks of cards are used in the shoe initially."
              "\n*Side-rules (doubling-down, splitting, etc.) are absent "
              "from this game."
              "\n*When dealer hits a 'Soft 17', he has to stand."
              "\n*All players start out with 100 credits each."
              "\n*Wins are paid out at 1:1, except for winning blackjacks "
              "which are paid at 3:2.")
        print("\n" + "#"*79)
        time.sleep(1.75)
    
    def play(self):
        """Logic for playing the full game."""
        self.shoe.shuffle()

        while True:
            # Print start screen and player details.
            self.start_screen()
            print("PLAYERS".center(79) + "\n"
                  + ("-"*7).center(79))
            for i in range(len(self.players)):
                print(f"Player {i+1}" + "\n"
                      + "="*len(f"Player {i+1}")
                      + f"\n\tName: {self.players[i].name}"
                      + f"\n\tCredits: {self.players[i].credit}")
            print("\n" + "#"*79)

            # Update shoe when more than 75% of cards are used up.
            if self.shoe.cards_left() < 78:
                self.shoe = Shoe()
                self.shoe.shuffle()
            
            # Betting process.
            print("PLAYERS, PLACE YOUR BETS".center(79) + "\n"
                  + ("-"*24).center(79) + "\n")
            for player in self.players:
                print(f"{player.name} has {player.credit} credits left.")
                player.bet = float(input(f"How many credits do you want"
                                       + f" to bet, {player.name}? "))
            print("\n" + "#"*79)
            
            # Beginning of Blackjack round.
            print("START OF ROUND".center(79) + "\n"
                  + ("-"*14).center(79))
            
            # Initial dealing of cards - 2 cards to each player.
            # (dealing starts from the players and ends with the dealers).
            for i in range(2):
                for player in self.players:
                    player.hand.draw_from(self.shoe)
                self.dealer.hand.draw_from(self.shoe)

            # Print details (hand, bet, credit)
            print("CURRENT BLACKJACK TABLE".center(79) + "\n"
                  + ("="*23).center(79))
            for player in self.players:
                print(f"{player.name},")
                player.show_hand()
                print("-"*79)
                time.sleep(2.5)
            print("="*79 + "\n")
            self.dealer.show_hand(initial=True)
            time.sleep(2.5)
            print("\n" + "#"*79)
            
            # Play starts from the players and ends with the dealers.
            print("PLAYERS, MAKE YOUR MOVES".center(79) + "\n"
                  + ("-"*24).center(79))
            is_bust = []                     # Checks how many players bust.
            for player in self.players:
                print(f"{player.name}'s move\n"
                      + "="*(len(player.name)+7))
                # Checks if player has a Blackjack.
                if player.hand.value == 21:
                    player.show_hand()
                    print("YOU HAVE GOT A BLACKJACK!\n")
                    player.hand.value = "21B"  # 'B' stands for Blackjack.
                    is_bust.append(False)
                    time.sleep(1.25)
                    print("-"*79)
                    continue
                # All the players start playing.
                while player.play():
                    player.hand.draw_from(self.shoe)  #Hit.
                if player.hand.value == "BUST":
                    is_bust.append(True)
                else:
                    is_bust.append(False)
                print("-"*79)
                time.sleep(1.5)
            # Proceeds only if at least one player did not bust.
            if False in is_bust:
                print("="*79)
                print("\nDealer's move\n"
                      + "="*(13) + "\n")
                if self.dealer.hand.value == 21:
                    self.dealer.show_hand()
                    print("Dealer has got a Blackjack!\n")
                    self.dealer.hand.value = "21B"
                    time.sleep(2)
                else:
                    while self.dealer.play():
                        self.dealer.hand.draw_from(self.shoe)  # Hit.
                        print("\n")
                        time.sleep(2)
            print("#"*79)
            time.sleep(2)

            #Results of the round.
            print("RESULTS OF THE ROUND".center(79) + "\n"
                  + ("-"*20).center(79), end='')
            for player in self.players:
                time.sleep(1.5)
                print("\n")
                if player.hand.value == "BUST":
                    # Bet lost by player.
                    print(player.name, "LOST THE ROUND!",
                          f"\n{player.name}, YOU LOSE", player.bet, "CREDIT(S).")
                    player.credit -= player.bet
                    continue

                elif self.dealer.hand.value == "BUST":
                     # Bet won by player.
                    print(player.name, "WON THE ROUND!",
                          f"\n{player.name}, YOU WIN", player.bet, "CREDIT(S).")
                    player.credit += player.bet
                    continue

                elif str(player.hand.value) > str(self.dealer.hand.value):
                    # Bet won by player.
                    if player.hand.value == "21B":
                        # Blackjack returns 1.5 times the original bet.
                        print(player.name, "WON THE ROUND!",
                              f"\n{player.name}, YOU WIN", player.bet*1.5, "CREDIT(S)",
                              "BECAUSE OF YOUR BLACKJACK!")
                        player.credit += (player.bet * 1.5)
                        continue
                    print(player.name, "WON THE ROUND!",
                          f"\n{player.name}, YOU WIN", player.bet, "CREDIT(S).")
                    player.credit += player.bet
                    continue

                elif str(player.hand.value) < str(self.dealer.hand.value):
                    # Bet lost by player.
                    print(player.name, "LOST THE ROUND!",
                          f"\n{player.name}, YOU LOSE", player.bet, "CREDIT(S).")
                    player.credit -= player.bet
                    continue
                
                elif player.hand.value == self.dealer.hand.value:
                    # Draw.
                    print(f"IT'S A DRAW, {player.name}!"
                          + "\nThere is no change in your credits.")
                    continue
            print("\n" + "#"*79)
            
            # Ask players if they want to replay.
            print("END OF ROUND".center(79) + "\n"
                  + ("-"*12).center(79) + "\n")
            for player in self.players.copy():
                time.sleep(1)
                if player.credit == 0:
                    print(f"Sorry {player.name}, you can't play anymore, "
                          "as you have no credits left.")
                    self.players.remove(player)
                else:
                    choice = input("Do you want to play another hand, "
                                  f"{player.name}? (Y/N) ")
                    del player.bet
                    player.hand.empty_cards()
                    player.hand.value = 0
                    if choice.upper() == "N":
                        self.players.remove(player)
            self.dealer.hand.empty_cards()
            self.dealer.hand.value = 0

            # If every player quits, end game.
            if not self.players:
                print("\n" + "GAME OVER!".center(79))
                print("#"*79 + "\n")
                time.sleep(1)
                break
                    

def main():
    """Main game-playing function."""
    game = Game(*(sys.argv[1:]))
    game.play()


if __name__ == "__main__":
    main()
