import unittest
import blackjack as BlackJackClass
import Card as CardClass

class Test_Hit(unittest.TestCase):

	def test_hit(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		testGame.dealer.Hit(testGame.deck, testGame.count)

		self.assertEqual(len(testGame.dealer.hand), 3)

	def test_hit_twice(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		testGame.dealer.Hit(testGame.deck, testGame.count)

		testGame.dealer.Hit(testGame.deck, testGame.count)

		self.assertEqual(len(testGame.dealer.hand), 4)


class Test_PrintHand(unittest.TestCase):

	def test_print_hand(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		testGame.dealer.PrintHand()

		tempHandVal = 0

		for x in testGame.dealer.hand:

			tempHandVal += x.value

		self.assertEqual(testGame.dealer.handValue, tempHandVal)

class Test_SetHand(unittest.TestCase):

	def test_set_hand(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		card1 = CardClass.Card("Hearts", "Jack", 10)
		card2 = CardClass.Card("Spades", "8", 8)

		testGame.dealer.SetHand(card1, card2)

		self.assertEqual(testGame.dealer.hand[0].number, card1.number)

class Test_AddCard(unittest.TestCase):

	def test_add_card(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		card1 = CardClass.Card("Hearts", "Jack", 10)	

		testGame.dealer.AddCard(card1)	

		self.assertEqual(testGame.dealer.hand[2].number, card1.number)

class Test_TakeTurn(unittest.TestCase):

	def test_take_turn(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		card1 = CardClass.Card("Hearts", "Jack", 10)
		card2 = CardClass.Card("Spades", "8", 8)

		testGame.dealer.SetHand(card1, card2)

		testGame.dealer.TakeTurn(testGame.deck, testGame.count)

		self.assertEqual(testGame.dealer.handValue, 18)

class Test_CheckForAces(unittest.TestCase):

	def test_check_for_aces_true(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		card1 = CardClass.Card("Hearts", "Jack", 10)
		card2 = CardClass.Card("Spades", "8", 8)
		card3 = CardClass.Card("Clubs", "Ace", 11)

		testGame.dealer.SetHand(card1, card2)
		testGame.dealer.AddCard(card3)

		testGame.dealer.CheckForAces()

		self.assertEqual(testGame.dealer.handValue, 19)


if __name__ == '__main__':
	unittest.main()
