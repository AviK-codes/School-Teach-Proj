from random import choice


class CardDeck:
    card_set = []
    clubs = []
    diamonds = []
    hearts = []
    spades = []
    deck = []

    def __init__(self, num_of_decks):
        self.num_of_decks = num_of_decks
        self.clubs = ['clubs', [i for i in range(1, 14)]]
        self.diamonds = ['diamonds', [i for i in range(1, 14)]]
        self.hearts = ['hearts', [i for i in range(1, 14)]]
        self.spades = ['spades', [i for i in range(1, 14)]]
        self.deck = [self.clubs, self.diamonds, self.hearts, self.spades]

    def reshuffle_deck(self):
        self.clubs = ['clubs', [i for i in range(1, 14)]]
        self.diamonds = ['diamonds', [i for i in range(1, 14)]]
        self.hearts = ['hearts', [i for i in range(1, 14)]]
        self.spades = ['spades', [i for i in range(1, 14)]]
        self.deck = [self.clubs, self.diamonds, self.hearts, self.spades]

    def draw_card(self):
        card_num = -1
        while card_num == -1:  # reselect is needed as the selected card was already submitted
            self.card_set = choice(self.deck)
            card_num = choice(self.card_set[1])
            self.card_set[1][int(card_num) - 1] = -1  # delete the selected card
        return card_num, self.card_set[0]


class Players(CardDeck):
    def __init__(self, game, num_of_decks):
        super().__init__(num_of_decks)
        self.game = game
        self.cards = []

    def player_draw(self):
        print("---Player cards:---")
        if self.game == "blackjack":
            for i in range(0,1):
                player_card_num, player_card_set = self.draw_card()
                self.cards.append(player_card_num)
                print(player_card_num, player_card_set,self.cards)
            print("---Player set:---")
            print(self.card_set)

    def dealer_draw(self):
        if self.game == "blackjack":
            for i in range(0,2):
                print("---Dealer cards:---")
                dealer_card_num, dealer_card_set = self.draw_card()
                self.cards.append(dealer_card_num)
                print(dealer_card_num, dealer_card_set,self.cards)
                print("---Dealer set:---")
                print(self.card_set)

    def calc(self):
        pass


players = Players("blackjack",1)
for i in range(1,10):
    players.player_draw()
    players.dealer_draw()

