"""Class definitons of card-related details in Blackjack."""

import random


class Card:
    """
    Holds the value and suit of an individual card.

    Parameters
    ----------
    rank: str or int
          Number (or rank) of card.
    suit: str
          Suit of card.

    Attributes
    ----------
    face_values: dict of str: int
                 Mapping of face cards to their corresponding values.
    value

    """

    face_values = {"Ace": 11, "Jack": 10, "Queen": 10, "King": 10}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """
        Returns full name of the card.

        Returns
        -------
        str
            Full name of the card : rank + suit.

        Notes
        -----
        Overrides default '__str__' of the class.

        """
        return "{0.rank} of {0.suit}".format(self)

    @property
    def value(self):
        """int: Numerical value of card in Blackjack."""
        return self.face_values.get(self.rank, self.rank)


class Shoe:

    """
    Holds the cards and the logic for shuffling and dealing.

    The list of cards is treated like a stack

    Parameters
    ----------
    cards: list of cards
           Six standard 52-card decks of cards.

    Notes
    -----
    Analogous to 'Dealing shoes' used in casinos.

    """

    def __init__(self):
        # Initialize a standard 52-card deck of cards
        deck = []
        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            deck.append(Card("Ace", suit))
            deck.extend([Card(rank, suit) for rank in range(2, 11)])
            for face_card in ["Jack", "Queen", "King"]:
                deck.append(Card(face_card, suit))

        # The cards sequence contains 6 such decks
        self.cards = deck * 6

    def shuffle(self):
        """Shuffles the cards list in a random order."""
        random.shuffle(self.cards)

    def next_card(self):
        """
        Deals the next card from the cards list.

        The top-most (last) Card in the cards list is popped (returned and
        removed) from the sequence.

        Returns
        -------
        Card
            The last Card in the list cards (at the time of calling).

        """
        return self.cards.pop()

    def cards_left(self):
        """Returns the cards list in the shoe.

        Returns
        -------
        list of Card
            Current cards list.

        """
        return len(self.cards)


class Hand:

    """
    Collection of cards, with the logic for adding up scores.

    Parameters
    ----------
    cards: list of Card
           Cards in the player's hand.

    Arguments
    ---------
    value

    """

    def __init__(self):
        self.cards = []
        self._value = None

    def draw_from(self, shoe):
        """
        Draws a card from the shoe and adds it to list of cards in Hand.

        Parameters
        ----------
        shoe: Shoe
              Shoe of cards being used for the current play.

        """
        self.cards.append(shoe.next_card())

    def empty_cards(self):
        """Empties the list of cards in hand."""
        self.cards = []

    @property
    def value(self):
        """int or str: Score of current Hand."""
        if self._value == "21B" or self._value == "BUST":
            return self._value
        
        self._value = sum(card.value for card in self.cards)
        # Change value of Ace from 11 to 1 if value if the
        # hand is a BUST.
        if self._value > 21:
            ace_count = 0
            for card in self.cards:
                if "Ace" in str(card):
                    ace_count += 1
            for count in range(ace_count):
                if self._value > 21:
                    self._value -= 10
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    
