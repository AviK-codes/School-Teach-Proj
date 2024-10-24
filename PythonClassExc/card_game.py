import random
from random import choice


class CardDeck:
    cards_deck = []

    def __init__(self, num_of_decks):
        self.cards_suits = []
        self.cards_numbers = []
        self.num_of_decks = num_of_decks
        self.cards_suits = ["clubs", "diamonds", "spades", "hearts"]
        self.cards_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        CardDeck.cards_deck = [[i, j] for i in self.cards_suits for j in self.cards_numbers]
        random.shuffle(CardDeck.cards_deck)

    def reshuffle_deck(self):
        CardDeck.cards_deck = [[i, j] for i in self.cards_suits for j in self.cards_numbers]
        random.shuffle(CardDeck.cards_deck)

    @staticmethod
    def draw_card():
        if not CardDeck.cards_deck:
            return "no more cards in deck"
        else:
            return CardDeck.cards_deck.pop()


class Player:

    def __init__(self, name):
        self.player_cards = []
        self.name = name

    def player_draw(self):
        #print(f"For player: {self.name}")
        self.player_cards.append(CardDeck.draw_card())
        #print(self.player_cards)


class Dealer:
    def __init__(self):
        self.dealer_cards = []

    def dealer_draw(self):
        for i in range(0, 1):
            self.dealer_cards.append(CardDeck.draw_card())
            #print(self.dealer_cards)

    def dealer_hitting_phase(self):
        dealers_card = self.calc(self.dealer_cards)
        if dealers_card < 17:
            print("dealer's hitting phase as his drawn two cards are less than 17:")

        while dealers_card < 17:
            self.dealer_draw()
            dealers_card = self.calc(self.dealer_cards)

    def dealer_show_up_card(self):
        return self.dealer_cards[0]


class Game(CardDeck, Dealer):
    def __init__(self, game, num_of_decks, players_list):
        CardDeck.__init__(self, num_of_decks)
        Dealer.__init__(self)
        self.players_results=[]
        self.num_of_decks = num_of_decks
        self.game = game
        self.bet = 0
        self.players_dic = {}

        self.players_list = players_list
        for name in self.players_list:
            self.players_dic[name] = Player(name)

    def player_draw(self):
        for name in self.players_list:
            for i in range(0,2):
                self.players_dic[name].player_draw()

    def present_players_cards(self):
        for name in self.players_list:
            print(f"Player {name}, your cards are:")
            print (self.players_dic[name].player_cards)


    @staticmethod
    def calc(cards):
        card_sum = 0
        card_ace = 1
        for card in cards:
            if card[1] > 9:
                card_val = 10
            else:
                card_val = card[1]
            #print(card_val)
            if card_val == 1:
                card_ace = 11
            card_sum = card_sum + card_val

        if (card_sum < 22) and (card_ace == 11):
            if (card_sum - 1 + card_ace) < 22:
                card_sum = card_sum - 1 + card_ace

        if card_sum > 21:
            print(f"Result: {card_sum}, bust")
            return card_sum
        #print(f"Result: {card_sum}")
        return card_sum

    def showdown(self):
        print("Dealer cards calculation:")
        dealer_result = self.calc(self.dealer_cards)

        print("Players cards calculation:")
        for name in self.players_list:
            print(f"calculating results for player: {name}")
            player_result = self.calc(self.players_dic[name].player_cards)
            self.check_game_results(dealer_result,player_result, name)

    def check_game_results(self, dealer_result, player_result, player_name):

        if (dealer_result < 22) and (player_result < 22):
            if dealer_result > player_result:
                self.players_results.append(["won","dealer",dealer_result,player_name,player_result])
            elif dealer_result == player_result:
                self.players_results.append(["fit","dealer",dealer_result,player_name,player_result])
            else:
                self.players_results.append(["won",player_name,player_result,"dealer",dealer_result])

        else:
            if (dealer_result > 21) and (player_result < 22):
                self.players_results.append(["won",player_name, player_result,"dealer",dealer_result])
            elif (dealer_result < 22) and (player_result > 21):
                self.players_results.append(["won","dealer",dealer_result,player_name,player_result])
            else:
                self.players_results.append(["both lost","dealer",dealer_result,player_name,player_result])

    def player_hit(self,name):
        # Receive additional cards to improve their hand.
        self.players_dic[name].player_draw()

    def double_down(self,name):
        # Double their initial bet and receive only one more card.
        self.players_dic[name].player_draw()
        self.double_bet(name)

    def double_bet(self,name):
        self.bet = 2 * self.bet

    def enter_bet(self, bet):
        self.bet = bet

    def stand(self):
        # Keep their current hand.
        pass


players_name = []
name = ""
while name != 'q':
    name = input("Nice to meet you, I'm your blackjack dealer, who's playing? enter your name (q to quit) ")
    if name != 'q':
        if name:
            players_name.append(name)
        else:
            print("Player have to enter at least one character for his name")

blackjack = Game("blackjack", 1, players_name)

print("Dealer cards, starts with drawing two cards:")
blackjack.dealer_draw()
blackjack.dealer_draw()

print(f"Dealer up card is: {blackjack.dealer_show_up_card()}")
blackjack.player_draw()
blackjack.present_players_cards()
player_bets = {}

print("Placing a bet?")
while choice != 'q':
    for name in enumerate(players_name):
        print(f"{name[0]})   {name[1]} ?")
    choice = input("Who wants to place a bet?, enter your number: (q to proceed)")
    if choice.isdigit() and (int(choice) < len(players_name)):
        bet = input(f"Hi {players_name[int(choice)]}, enter your bet ")
        player_bets[players_name[int(choice)]] = int(bet)
        pos_choice = ''
        while pos_choice != 'q':
            print(pos_choice)
            pos_choice = input("0) Hit? (ask for another card), 1) Stand? (keep the cards), 2) Surrender? (loosing half of "
                       "bet) \n enter option number  (q when done)")
            if pos_choice == '0':
                blackjack.player_hit(players_name[int(choice)])
            if pos_choice == '1':
                print(f"{players_name[int(choice)]} keeps his cards")
            if pos_choice == '2':
                print(f"{players_name[int(choice)]} surrenders and loose half of his bet")
                player_bets[players_name[int(choice)]] *= 0.5
    else:
        print(f"Please enter a number between 0 and {len(players_name)-1}")

print("Player bets are: ", player_bets)

blackjack.dealer_hitting_phase()
blackjack.showdown()
print(blackjack.players_results)
