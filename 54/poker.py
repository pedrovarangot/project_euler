from collections import Counter, OrderedDict
import sys

class Card(object):

    figure_to_number = {
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
            }

    def __init__(self, code):
        if code[0] not in self.figure_to_number.keys():
            self.value = int(code[0])
        else:
            self.value = self.figure_to_number[code[0]]
        self.suit = code[1]

    def __repr__(self):
        return "{}-{}".format(self.value, self.suit)

def dictinvert(d):
    inv = {}
    for k, v in d.iteritems():
        keys = inv.setdefault(v, [])
        keys.append(k)
    return inv

def analyze(cards):
    values = map(lambda c: c.value, cards)
    same_suit = len(set(map(lambda c: c.suit, cards))) == 1
    value_counts = OrderedDict(Counter(sorted(values, reverse=True)))
    values = sorted(value_counts.keys(), key=lambda k: value_counts[k], reverse=True)
   
    if values == [14, 5, 4, 3, 2]:
        values = [5, 4, 3, 2, 1]

    straight = len(values) == 5 and values[0] - values[4] == 4

    pairs = 0
    for (k,v) in value_counts.items():
        if v == 2:
            pairs += 1
    two_pairs = pairs == 2

    counts = sorted(value_counts.values())

    hand_type = "ERROR"
    if same_suit and values == [14, 13, 12, 11, 10]:
        hand_type = 9
    elif same_suit and straight:
        hand_type = 8
    elif counts == [1, 4]:
        hand_type = 7
    elif [2, 3] == counts:
        hand_type = 6
    elif same_suit:
        hand_type = 5
    elif straight:
        hand_type = 4
    elif [1, 1, 3] == counts:
        hand_type = 3
    elif [1, 2, 2] == counts:

        hand_type = 2
    elif [1, 1, 1, 2] == counts:
        hand_type = 1
    elif [1, 1, 1, 1, 1] == counts:
        hand_type = 0

    return (hand_type, values) 

if __name__ == "__main__":

    p1_wins = 0
    while True:
        try:
            cards = input().strip().split()
            hand = cards.copy()
        except EOFError:
            print(p1_wins)
            sys.exit(0) 

        cards = list(map(Card, cards))

        p1 = analyze(cards[0:5])
        p2 = analyze(cards[5:])

        print(p1,p2)
        if p1[0] > p2[0]:
            p1_wins += 1
        elif p1[0] == p2[0] and p1[1] > p2[1]:
            if p1[1][0] == p2[1][0]:
                print("AAA")
            p1_wins += 1

        print(p1[0] > p2[0] or p1[0] == p2[0] and p1[1][0] >= p2[1][0], hand)

