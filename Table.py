import bisect

class MyValidationError(Exception):
    '''self-defined error'''
    pass

class Table:
    '''
    Table Class: 
    Represent 4 rows of cards on the table.

    Methods:
    ----
    display_table : print out current tables with card numbers.
    argsort : self-defined argsort function, same as numpy.argsort.
    check_six_cards : if there is any row on the table has 6 cards, return True.
    check_largest_smaller : if there is any negative number, return 1. 
                            all positive return 2.
    find_largest_smaller_idx_to_zero : find the closest number's idx smaller than zero.
    insert_this_turn : rule of game every turn. 
                       you are encouraged to make this method prettier. 
    '''
    
    def __init__(self, items):
        '''
        Parameters:
        ---
        items : nested list, shape=(4, 1) if it is a numpy array.
                Represent the cards on the table.
        
        '''
        self.items = items
        
    def display_table(self):
        print('-------------------')
        print('Current Table: \n{}'.format(('\n'.join([ 
             ' |'.join(list(map(str, self.items[key]))) 
                for key in self.items.keys()]))
                )
             )
    
    def argsort(self, seq):
        # http://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python/3382369#3382369
        # by unutbu
        return sorted(range(len(seq)), key=seq.__getitem__)
    
    def check_six_cards(self, items):
        if any(i == 6 for i in list(map(len, items.values()))):
            return 1
        return 0

    def check_largest_smaller(self, insert_list):
        if any(i < 0 for i in insert_list): return 1
        elif all(i > 0 for i in insert_list): return 2
        raise MyValidationError("Invalid insert_list")

    def find_largest_smaller_idx_to_zero(self, insert_list):
        # find the index of largest smaller number in items_last
        insert_idxs = self.argsort(insert_list)
        return insert_idxs[bisect.bisect_left(
            [insert_list[idx] for idx in insert_idxs], 0
            ) - 1]
    
    def insert_this_turn(self, cards_this_turn, players):
        '''
        insert cards this turn and calculate the scores of players, 
        and also refresh the items on the table.
        
        Parameters:
        ----
        cards_this_turn : list, cards that players insert at this trun.
        players : list, list contain list of Player class objects.
        '''
        # loop from smallest one
        cards_index = self.argsort(cards_this_turn)
        
        # loop over every cards in this turn
        for idx,c,key in zip(cards_index, 
                             [cards_this_turn[i] for i in cards_index], 
                             [list(players.keys())[i] for i in cards_index]):
            # the last item on the table in every rows
            items_last = [self.items[key][-1] if len(self.items[key]) != 0 else 0 
                          for key in self.items.keys()]

            # calculate which number is smaller than the card player insert
            insert_list = [i - c for i in items_last]

            # check if any number < 0 (largest smaller number have to be smaller than c)
            if  self.check_largest_smaller(insert_list) == 1:
                insert_idx = self.find_largest_smaller_idx_to_zero(insert_list)
                # append back to the items dict
                self.items[list(self.items.keys())[insert_idx]].append(c)

                # if any row has == 6 cards, empty the list and reduce the score of this player
                if self.check_six_cards(self.items):
                    players[key].score -= 5
                    self.items[list(self.items.keys())[insert_idx]] = []
                    self.items[list(self.items.keys())[insert_idx]].append(c)

            # if all items on the table are larger than the card which player insert
            # empty the row with least length and insert the card as the first card
            elif self.check_largest_smaller(insert_list) == 2:    
                # I am trying to avoid to use argmin in numpy, 
                # so I use self-defined argsort as an alternativs
                items_length = list(map(len, self.items.values()))
                least_length_idx = self.argsort(items_length)[0]

                # reduce the score based on least length of the items on the row
                # empty the row and append the card player inserted
                players[key].score -= items_length[least_length_idx]
                self.items[list(self.items.keys())[least_length_idx]] = []
                self.items[list(self.items.keys())[least_length_idx]].append(c)