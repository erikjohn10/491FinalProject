import unittest
import blackjack as BlackJackClass
import Card as CardClass

class Test_PlayHit(unittest.TestCase):

	def test_hit(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		testGame.player.Hit(testGame.deck, testGame.count)

		self.assertEqual(len(testGame.player.hand), 3)

	def test_hit_twice(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		testGame.player.Hit(testGame.deck, testGame.count)

		testGame.player.Hit(testGame.deck, testGame.count)

		self.assertEqual(len(testGame.player.hand), 4)


class Test_PlayPrintHand(unittest.TestCase):

	def test_print_hand(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		testGame.player.PrintHand()

		tempHandVal = 0

		for x in testGame.player.hand:

			tempHandVal += x.value

		self.assertEqual(testGame.player.handValue, tempHandVal)

class Test_PlaySetHand(unittest.TestCase):

	def test_set_hand(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		card1 = CardClass.Card("Hearts", "Jack", 10)
		card2 = CardClass.Card("Spades", "8", 8)

		testGame.player.SetHand(card1, card2)

		self.assertEqual(testGame.player.hand[0].number, card1.number)

class Test_PlayAddCard(unittest.TestCase):

	def test_add_card(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		card1 = CardClass.Card("Hearts", "Jack", 10)	

		testGame.player.AddCard(card1)	

		self.assertEqual(testGame.player.hand[2].number, card1.number)

class Test_PlayCheckForAces(unittest.TestCase):

	def test_check_for_aces_true(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		card1 = CardClass.Card("Hearts", "Jack", 10)
		card2 = CardClass.Card("Spades", "8", 8)
		card3 = CardClass.Card("Clubs", "Ace", 11)

		testGame.player.SetHand(card1, card2)
		testGame.player.AddCard(card3)

		testGame.player.CheckForAces()

		self.assertEqual(testGame.player.handValue, 19)

if __name__ == '__main__':
	unittest.main()
