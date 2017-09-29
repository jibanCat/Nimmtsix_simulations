import random

class Player:
    '''
    Player Class:

    Methods:
    pop : hand-out a card from your hand_cards based on strategy. 
    strategy : the way you choose an index to return in hand_cards list. 
               this is where we can study the best strategy of the game.
    '''
    
    def __init__(self, prefix, hand_cards, table):
        '''
        Parameters:
        ----
        prefix : string, name of the player.
        hand_cards : list, current cards on the player's hand.
        score : int, score of the player. negative is worse. 
        history : list, your previous hand-out cards. 
        table : table class, 
                you are eligible to use this object to see the current table.
        '''
        self.prefix = prefix
        self.hand_cards = hand_cards
        self.score = 0
        self.history = []
        self.table = table
        
    def pop(self):
        '''Pop out the cards with given strategy:'''
        out = self.hand_cards.pop(self.strategy())
        self.history.append(out)
        return out
        
#################### edit computer's method here ####################
    def strategy(self):
        '''
        Random strategy for the pop out rule.
        '''
        return random.randint(0, len(self.hand_cards) - 1)
#################### edit computer's method here ####################
    
class Player_user:
    
    
    def __init__(self, prefix, hand_cards, table):
        '''
        Parameters:
        ----
        prefix : string, name of the player.
        hand_cards : list, current cards on the player's hand.
        score : int, score of the player. negative is worse. 
        history : list, your previous hand-out cards. 
        table : table class, 
                you are eligible to use this object to see the current table.
        '''
        self.prefix = prefix
        self.hand_cards = hand_cards
        self.score = 0
        self.history = []
        self.table = table
        
    def pop(self):
        '''Pop out the cards with given strategy:'''
        out = self.hand_cards.pop(self.strategy())
        self.history.append(out)
        return out
        

#################### edit player's method here ####################        
    def strategy(self):
        while 1:
            print('Your Cards   : {}'.format(' |'.join([str(card).zfill(3) 
                                             for card in self.hand_cards])))
            out = int(input('Choose a Card: {}\n'.format(' |'.join([str(i).zfill(3) 
                         for i in range(len(self.hand_cards))]))))
            try:
                temp = self.hand_cards[out]
                del temp
                return out
            except IndexError as i:
                print('Please insert valid index.')
#################### edit player's method here ####################                        