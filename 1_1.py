import collections

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    #split():以空格为分隔符对字符串进行切片

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')    #得到一个纸牌对象
print(beer_card)

deck = FrenchDeck()    #查看一叠牌有多少张
print(len(deck))

print(deck[0])    #抽取第一张牌
print(deck[-1])    #抽取最后一张牌

from random import choice    #随机选出一张牌
print(choice(deck))
print(choice(deck))
print(choice(deck))

print(deck[:3])    #查看一摞牌最上面3张和只看是A的牌的操作
print("\n")

print(deck[12::13])    #先抽出索引是12的那张牌，然后每向后数13张牌拿一张
print("\n")

for card in deck:
    #仅仅实现__getitem__方法，这一摞牌就变成可迭代的了
    print(card)
print("\n")

for card in reversed(deck):
    #反向迭代
    print(card)
print("\n")

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.rank.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
print("\n")