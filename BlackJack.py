# Global variables for Card class
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

#Card object
class Cards:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


import random


class Deck:
    def __init__(self):
        # creates an empty deck of cards in list form
        self.full_deck = []

        # Adds Cards to the list
        for rank in ranks:
            for suit in suits:
                current_card = Cards(rank, suit)
                self.full_deck.append(current_card)

    def shuffle(self):
        # Shuffles the deck
        random.shuffle(self.full_deck)

    def deal_card(self):
        # removes a card from bottom of the deck
        if not self.full_deck:
            return None
        else:
            return self.full_deck.pop()


#Player Object
class Player:

    def __init__(self,name):
        self.name = name
        self.hand = []
#adds card to players hand
    def hit(self,card):
        self.hand.append(card)
#calculates players hand value        
    def calculate_hand_value(self):
        cvalue = sum(card.value for card in self.hand)
        ace_count = sum(1 for card in self.hand if card.rank == 'Ace')
        #ajusts tehe value of aces in players hand
        if cvalue > 21 and ace_count>0:
            cvalue -= 10
            ace_count -=1
        return cvalue
        
    def print_hand(self):
        for card in self.hand:
            print(f'{card}')        
        cvalue = self.calculate_hand_value()       
        print(f'Value of player card = {cvalue}\n')

class Dealer:

    def __init__(self):
        self.face_up_hand = []
        self.face_down_hand = []
    
    def hit(self,card,rnd):

        if rnd == 1:
            self.face_up_hand.append(card)
            self.face_down_hand.append(my_deck.deal_card())
        else:
            self.face_up_hand.append(card)
    
    def calculate_hand_value(self):
        cvalue = sum(card.value for card in self.face_up_hand)
        ace_count = sum(1 for card in self.face_up_hand if card.rank == 'Ace')
        
        if cvalue > 21 and ace_count>0:
            cvalue -= 10
            ace_count -=1
        return cvalue
            
            
    def print_hand(self,rnd):
        cvalue=0
        if rnd == 1:
            for card in self.face_up_hand:
                print(f'{card}')
                print('<hidden card>')
        else:
            my_set= set(self.face_up_hand + self.face_down_hand)
            #if self.face_down_hand not in self.face_up_hand:
                #self.face_up_hand.extend(self.face_down_hand)
                
                
            my_list = list(my_set)
            #my_list.sort()
            self.face_up_hand = my_list
            for card in self.face_up_hand:
                print(f'{card}')
            
            cvalue= self.calculate_hand_value()
            print(f"Value of dealer's cards is {cvalue}\n")


def do_you_want_to_play():
    ans = 'wrong'
    while ans not in ['Y','N']:
        ans = input('Do you want to play again?(Y/N): ')
    
    if ans == 'Y':
        return True
    else:
        return False

my_deck= Deck()
my_deck.shuffle()
dealer = Dealer()

name = input('What is your name: ')
player = Player(name)
game_on = True
hit_or_stand = 'wrong'
bust=False
pcval=0
dcvals=0
while game_on==True:
    rnd=1 
    if rnd == 1:
        for i in range(0,2):
            player.hit(my_deck.deal_card())
            #player card value
            pcval= player.calculate_hand_value()
            if pcval == 21:
                print(f'Blackjack!! {player.name} wins! ')
                game_on = do_you_want_to_play()
            if i == 1:  # Only the first card is face-down for the dealer
                dealer.hit(my_deck.deal_card(),rnd)
            i=i+1
        player.print_hand()
        dealer.print_hand(rnd)
    
    while bust == False:
        while hit_or_stand not in ['h','s']:        
            hit_or_stand=input('Do you want to hit or stand (h/s)')
        if hit_or_stand== 'h':
            hit_or_stand= ''
            player.hit(my_deck.deal_card())
            pcval = player.calculate_hand_value()
            player.print_hand()
            if pcval > 21:
                print(f'{player.name} loses!')
                bust = True
            else:
                hit_or_stand = ''
                
            
        elif hit_or_stand == 's':
            hit_or_stand = ''
            rnd+=1
            dealer.print_hand(rnd)
            #dealer card value
            dcvals = dealer.calculate_hand_value()
            while dcvals < 17:

                dcvals= dealer.calculate_hand_value()
                if dcvals>16:
                    break
                dealer.hit(my_deck.deal_card(),rnd)
                dealer.print_hand(rnd)
                #dcvals= dealer.calculate_hand_value()
            if dcvals>17 or dcvals==17:
                #dealer.print_hand(rnd)
                if dcvals>21:
                    print(f'{player.name} wins')
                    break
                elif dcvals>pcval:
                    print(f'{player.name} loses!')
                    break
                elif dcvals<pcval:  
                    print(f'{player.name} wins!')
                    break
                    
    game_on=do_you_want_to_play()
    if game_on==True:
        dealer.face_up_hand.clear()
        dealer.face_down_hand.clear()
        player.hand.clear()
        continue
