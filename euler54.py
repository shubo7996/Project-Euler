'''
    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

'''

from collections import namedtuple

Card=namedtuple('Card',['rank','suit'])
Duplicate=namedtuple('Duplicate',['rank','value'])
Ten,Jack,Queen,King,Ace=10,11,12,13,14

def map_card_rank(rank):
	if rank=='T':
		return Ten
	if rank=='J':
		return Jack
	if rank=='Q':
		return Queen
	if rank=='K':
		return King
	if rank=='A':
		return Ace
	return int(rank)

def map_card_suit(suit):
	if suit=='H':
		return 1
	if suit=='D':
		return 2
	if suit=='C':
		return 3
	if suit=='S':
		return 4
	return int(suit)

def map_card(_card_):
	return Card(rank=map_card_rank(_card_[0]),suit=map_card_suit(_card_[1]))

class Hand(object):
	
	def __init__(self,*args):
		self.cards=sorted(args,key=lambda c: -c.rank)
		self.duplicates={}
		for card in self.cards:
			if card.rank in self.duplicates:
				continue
			_duplicates=0
			for card2 in self.cards:
				if card.rank==card2.rank:
					_duplicates+=1
			self.duplicates[card.rank]= _duplicates
	
	def __lt__(self,other):
		for rule in self.rules():
			#print(rule+ '')
			rule=getattr(self,rule)
			val=rule(other)
			if val:
				return val
	
	def rules(self):
		return []
	
	def _straight(self):
		last_card_rank=False
		for card in self.cards:
			if last_card_rank and last_card_rank!=card.rank+1:
				return False
			last_card_rank=card.rank
		return True

	def _flush(self):
		last_card_suit=False
		for card in self.cards:
			if last_card_suit and last_card_suit!= card.suit:
				return False
			last_card_suit=card.suit
		return True

	def _duplicate_count(self,c):
		for rank,value in self.duplicates.items():
			if value==c:
				yield rank
			


class PokerHand(Hand):
	def rules(self):
		rules=super(PokerHand,self).rules()
		rules.append('royal_flush')
		rules.append('straight_flush')
		rules.append('four_of_a_kind')
		rules.append('three_of_a_kind')
		rules.append('two_pair')
		rules.append('full_house')
		rules.append('flush')
		rules.append('straight')
		rules.append('highest_card')
		return rules

	def royal_flush(self,other):
		hand1=self.cards[0].rank == Ace and self._flush and self._straight
		hand2=other.cards[0].rank == Ace and other._flush and other._straight
		if hand1 and not hand2:
			return 1
		if hand2 and not hand1:
			return -1
		if hand1 and hand2:
			return 0 

	def straight_flush(self,other):
		#has_sf=False
		#current_suit=False 
		#for card in self.hand:
		#	if not current_suit:
		#		current_suit=card.suit
		#	elif current_suit!=card.suit:
		#		break
		hand1=self._flush() and self._straight()
		hand2=other._flush() and other._straight()
		if hand1 and not hand2:
			return 1
		if hand2 and not hand1:
			return -1
		if hand1 and hand2:
			return self.highest_card(other)

	def four_of_a_kind(self,other):
		#for hand1,hand2 in zip(self._duplicate_count(4),other._duplicate_count(4)):
		#	print('four_of_a_kind' ,h1,h2)
		#	if hand1 and not hand2:
		#		return 1
		#	if hand2 and not hand1:
		#		return -1
		#	if hand1 and hand2 and hand1>hand2:
		#		return 1
		#	if hand1 and hand2 and hand2>hand1:
		#		return -1
		#hand1=[r for r in self._duplicate_count(4)]
		#hand2=[r for r in other._duplicate_count(4)]
		#if hand1 and not hand2:
		#	return 1
		#if hand2 and not hand1:
		#	return -1
		#for h1_c,h2_c in zip(hand1,hand2):
		#	if h1_c>h2_c:
		#		return 1
		#	if h2_c>h1_c:
		#		return -1
		return self._of_a_kind(other,4)

	def three_of_a_kind(self,other):
		return self._of_a_kind(other,3)

	def _of_a_kind(self,other,value):
		hand1=[r for r in self._duplicate_count(value)]
		hand2=[r for r in other._duplicate_count(value)]
		if hand1 and not hand2:
			return 1
		if hand2 and not hand1:
			return -1
		if hand1 and hand2 and len(hand1)>len(hand2):
			return 1
		if hand1 and hand2 and len(hand2)>len(hand1):
			return -1
		for h1_c,h2_c in zip(hand1,hand2):
			if h1_c>h2_c:
				return 1
			if h2_c>h1_c:
				return -1
			#return self.highest_card(other)

	def two_pair(self,other):
		return self._of_a_kind(other,2) 


	def full_house(self,other):
		hand1_3=[r for r in self._duplicate_count(3)]
		hand2_3=[r for r in other._duplicate_count(3)]
		hand1_2=[r for r in self._duplicate_count(2)]
		hand2_2=[r for r in other._duplicate_count(2)]
		if hand1_3 and hand2_2 and not (hand2_3 and hand1_2):
			return 1
		if hand2_3 and hand2_2 and not (hand1_3 and hand1_2):
			return -1
		if hand1_3 and hand1_2 and hand2_3 and hand2_2:
			for h1_c,h2_c in zip(hand1_3,hand2_3):
				if h1_c>h2_c:
					return 1
				if h2_c>h1_c:
					return -1
			for h1_c,h2_c in zip(hand1_2,hand2_2):
				if h1_c>h2_c:
					return 1
				if h2_c>h1_c:
					return -1

	def flush(self,other):
		hand1=self._flush()
		hand2=other._flush()
		if hand1 and not hand2:
			return 1
		if hand2 and not hand1:
			return -1
		if hand1 and hand2:
			return self.highest_card(other)


	def straight(self,other):
		hand1=self._straight()
		hand2=other._straight()
		if hand1 and not hand2:
			return 1
		if hand2 and not hand1:
			return -1
		if hand1 and hand2:
			return self.highest_card(other)



	def highest_card(self,other):
		for c1,c2 in zip(self.cards, other.cards):
			if c1.rank!=c2.rank:
				if c1.rank>c2.rank:
					return 1
				else:
					return -1
		raise Exception("Tie in Highest Card")

	




#hand1=PokerHand(Card(rank=5,suit=1), Card(rank=5,suit='1'), Card(rank=5,suit='1'),Card(rank=6,suit='1'),Card(rank=6,suit='1'))
#hand2=PokerHand(Card(rank=2,suit=1), Card(rank=13,suit=1), Card(rank=13,suit=1),Card(rank=13,suit='1'),Card(rank=3,suit='1'))
#print(hand1<hand2) 
#print(hand1.__lt__(hand2))
#rint(hand2.duplicates)

#print(Hand(Card(rank=6,suit=1), Card(rank=5,suit='D'), Card(rank=7,suit='5'), Card(rank=3,suit='H')).straight())
#for count  in hand1._duplicate_count(4):
#	prind (count)

def get_hands_from_file(s):
	cards=[map_card(c) for c in s.split(' ')]
	return PokerHand(*cards[0:5]),PokerHand(*cards[5:])

p1_wins=0
with open('euler54.txt') as f:
	for line in f:
		hand1,hand2=get_hands_from_file(line.strip())
		if hand1>hand2:
			p1_wins+=1

print(p1_wins)