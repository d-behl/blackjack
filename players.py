"""Class definitions of player-related deatils in Blackjack."""

import time

from cards import Card, Shoe, Hand


class Player:

    """
    This class has a Hand of cards and the input logic for the Player.

    Contains info (name, credit) of Player, their Hand, and the move-making
    logic for the Player.

    Parameters
    ----------
    name: str
          Name of the Player.
    credit: int
            Cash carried by the Player in the form of credits.
    hand: Hand
          Hand received by the Player.
    bet: int
         Bet raised by PLayer for the given Hand.

    """

    def __init__(self, name):
        self.name = name
        self.credit = 100
        self.hand = Hand()
        self._bet = None
    
    @property
    def bet(self):
        """float: Credits being bet by player."""
        return self._bet

    @bet.setter
    def bet(self, val):
        """Setting balue of player's bet."""
        if val <= self.credit or val is None:
            self._bet = val 
            print("\n")
        else:
            raise ValueError("You dont't have enough credits.")

    @bet.deleter
    def bet(self):
        self._bet = None
    
    def show_hand(self):
        """Prints all cards in the player's hand along with the total value."""
        print("\nYour current hand\n"
              + "-"*17)
        for card in self.hand.cards:
            print(str(card))
        print("\nTotal value of Hand:", self.hand.value, "\n")

    def hit_or_stand(self):
        """
        Hitting and standing logic for the game.
        
        Returns
        -------
        bool
            True, if hitting. False, if standing.

        """
        choice = int(input("-----------------"
                           "\n¦     MOVES     ¦"
                           "\n-----------------"
                           "\n¦    HIT  : 1   ¦"
                           "\n¦   STAND : 2   ¦"
                           "\n-----------------"
                           "\nYOUR MOVE: "))

        if choice == 1:
            print("You have chosen to HIT.")
            return True
            
        elif choice == 2:
            print("You have chosen to STAND.")
            return False

        else:
            raise ValueError("Invalid move.")
   
    def play(self):
        """
        Selection of next move to play by the Player.

        Player can choose to either hit or stand.

        """
        self.show_hand()

        if self.hand.value > 21:
            print(f"{self.name} BUSTS!")
            self.hand.value = "BUST"
            return False
        
        elif self.hand.value < 21:
            return self.hit_or_stand()

        else:
            print("You have got a score of 21!")
            return False

class Dealer(Player):
    """This class contains a hand of cards and the input logic for the dealer."""

    def __init__(self):
        self.hand = Hand()
    
    def show_hand(self, initial=False):
        """
        Prints the dealer's cards according to Blackjack rules.

        Notes
        -----
        Overrides the show_hand() function of the base class.
        
        """
        """Prints all cards in the player's hand along with the total value."""
        print("Dealer's current hand\n"
              + "-"*21)
        if initial:
            print(self.hand.cards[0])
            print("---HOLE CARD---\n")
        else:
            for card in self.hand.cards:
                print(str(card))
            print("\nTotal value of Hand:", self.hand.value, "\n")
    
    def play(self):
        """
        Game-playing logic for the Dealer.
        
        Dealer hits till his score exceeds 16. He busts if score exceeds 21.
        
        """
        
        self.show_hand()
        time.sleep(2.25)

        if self.hand.value > 21:
            print("DEALER BUSTS!")
            self.hand.value = "BUST"
            return False
        elif self.hand.value == 21:
            print("Dealer has got a score of 21!")
            return False
        elif self.hand.value < 17:
            print("Dealer's score is less than 17."
                  + "\nDealer will HIT.")
            return True
        else:
            print("Dealer has exceeded 16."
                  + "\nDealer will STAND.")
            return False
