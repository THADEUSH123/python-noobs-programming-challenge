from random import shuffle

class PlayingCard(object):
    def __init__(self, rank="A", suit="♠"):
        self.valid_suits = ["♠", "♥", "♦", "♣"]
        self.valid_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J",
                            "Q", "K", "A"]

        if rank in self.valid_ranks:
            self.rank = rank
        else:
            print("Rank not valid")

        if suit in self.valid_suits:
            self.suit = suit
        else:
            print("Suit not valid")

    def __str__(self):
        str_map = {"\u2665": "HEARTS",
                   "\u2666": "DIAMONDS",
                   "\u2660": "SPADES",
                   "\u2663": "CLUBS"}

        return self.rank + " of " + str_map[self.suit]




class Deck(object):
    def __init__(self, suits=["♠", "♥", "♦", "♣"]):
        self.cards = []
        ranks = PlayingCard().valid_ranks
        for suit in suits:
            for rank in ranks:
                self.cards.append(PlayingCard(rank,suit))

        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.cards)

    def deal_card(self, card_count):
        if len(self.cards) >= card_count:
            cards = self.cards[0:card_count]
            self.cards = self.cards[card_count+1:]
            return cards
        else:
            print("out of cards")
            return []



print("Display a single card")
card1 = PlayingCard("A", "♦")
print(card1)
print("---------")

print("Display full deck")
deck = Deck()
for card in deck.cards:
    print(card)
print("---------")

print("Display a diamonds deck")
deck2 = Deck(["♦"])
for card in deck2.cards:
    print(card)
print("---------")

print("Display 2 cards delt")
delt_cards = deck2.deal_card(2)
for card in delt_cards:
    print(card)
print("---------")

print("Display remaining cards in deck")
for card in deck2.cards:
    print(card)
print("---------")

print("Same cards, just shuffled")
deck2.shuffle_deck()
for card in deck2.cards:
    print(card)
print("---------")
