from Table import Table
from Player import Player, Player_user
import argparse
import string
import random

def main(args):
    # number of players = 4 default
    num_of_players = args.num_of_players

    # initilize all cards and initialize the cards on the table
    all_cards = list(map(lambda x: x + 1, range(104)))
    items = dict((alph, []) for alph in string.ascii_lowercase[:4])

    # put cards on the table
    for i,name in enumerate(items.keys()):
        items[name].append(all_cards[-i - 1])
    table = Table(items)

    # random shuffle and take you subsets of the cards
    random.shuffle(all_cards)
    players = {}
    for i,name in enumerate(['p' + str(i+1).zfill(2) for i in range(num_of_players)]):
        if i==0:
            player = Player_user(prefix=name, 
                                 hand_cards=all_cards[i * 10 : (i + 1) * 10], 
                                 table=table)
            players[name] = player
        else:
            player = Player(prefix=name, 
                            hand_cards=all_cards[i * 10 : (i + 1) * 10], 
                            table=table)
            players[name] = player

    while len(players['p01'].hand_cards) > 0:
        # show current table
        table.display_table()

        # pop cards this turn 
        cards_this_turn = [player.pop() for key,player in players.items()]

        # insert into Table
        table.insert_this_turn(cards_this_turn, players)

        # print out score this turn
        print('Scores: ',[(player.prefix, player.score) for key,player in players.items()])

    print('EOF')
    
if __name__ == '__main__':
    while 1:
        parser= argparse.ArgumentParser()
        parser.add_argument('-n', '--num_of_players', type=int, default=4,
                            help='num of player in the game, num <- [1 , 10].')
        args = parser.parse_args()
        if  0 < args.num_of_players <= 10:
            break
        else:
            print('num of players should be in the range of [1, 10]')
    main(args)