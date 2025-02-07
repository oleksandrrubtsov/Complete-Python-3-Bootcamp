import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit 
    
class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card) 
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):  
        if len(self.all_cards) > 0: 
            return self.all_cards.pop()
        else:
            print("No more cards left in the deck")
            return None
    
    def __str__(self):
        return f"Deck of {len(self.all_cards)} cards"
    

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        if card:
            self.cards.append(card)
            self.value += card.value
            if card.rank == 'Ace':
                self.aces += 1
            self.adjust_for_ace()
        else:   
            print("No card to add")
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def __str__(self):
        return f"Hand value: {self.value}, Cards: {', '.join(str(card) for card in self.cards)}" 
    

class Chips:
    def __init__(self):
        self.total = 100  
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
                chips.bet = int(input("Place your bet: "))
        except ValueError:
                print("Must be an integer")
        else:
            if chips.bet > chips.total:
                    print("Sorry, your bet can't exceed",chips.total)
            else:
                break
    
def hit(deck, hand):
    hand.add_card(deck.deal_one())   
    hand.adjust_for_ace()  
        
    
def hit_or_stand(deck,hand):
    global playing  
    while True:
        x = input("Would you like 'h' or 's'? ")

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        
        else:
            print("Sorry, please try again")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand: ")
    print("<Hidden Card>")
    print('', dealer.cards[1])
    print("\nPlayer's hand: ", *player.cards, sep='\n')

    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\Player's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)


def player_busts(chips):
    print("Player Busts!")
    chips.lose_bet()

def player_wins(chips):
    print("Player Wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()
def dealer_wins(chips):
    print("Dealer Wins!")
    chips.lose_bet()

def push():
    print("It's a tie!")



# Game Logic
player_chips = Chips()
# Game Setup
while True:
    # Print an opening statement
    print("'Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.'")

    # Create & shuffle the deck, deal two cards to each player
    newdeck = Deck()
    newdeck.shuffle()
    player_hand = Hand()
    player_hand.add_card(newdeck.deal_one())
    player_hand.add_card(newdeck.deal_one())
    dealer_hand = Hand()
    dealer_hand.add_card(newdeck.deal_one())
    dealer_hand.add_card(newdeck.deal_one())

    # Set up the Player's chips
  
       
    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    playing =True
    while playing:
        # Prompt for Player to Hit or Stand
        hit_or_stand(newdeck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value >21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        elif player_hand.value == 21:
            print("Blackjack! You hit 21!")
            player_wins(player_chips)
            

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(newdeck,dealer_hand)

        # Show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()

    # Inform Player of their chips total
    print(f"\nCurrent amount: {player_chips.total}")
    

    # Ask to play again

    new_game = input("Wanna play a new game 'y' or 'n'? ").lower()

    if new_game[0].lower() == 'y':
        playing =True
        continue
    else:
        print("Thanks for playing")
        break