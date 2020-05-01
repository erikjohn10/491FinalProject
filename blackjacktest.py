import unittest
import blackjack as BlackJackClass
import Player as PlayerClass
import Dealer as DealerClass

class Test_MakeDeck(unittest.TestCase):

	"""Function Case: This test ensures that the MakeDeck function creates a list of cards that is 52 cards long"""
	def test_make_deck(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		self.assertEqual(len(testGame.deck) , 52)

	"""Function Case: This test ensures that the MakeDeck function adds all of the proper cards to the deck"""
	def test_all_cards_present(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testListSuits = ["Hearts","Diamonds","Clubs","Spades"]
		testListNumbers = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

		cardsCorrect = True

		for x in testGame.deck:

			if x.suit in testListSuits:

				if x.number in testListNumbers:

					if x.number == "Jack" or x.number == "Queen" or x.number == "King" and x.value == 10:

						cardsCorrect = True

					elif x.number == "Ace" and x.value == 11:

						cardsCorrect = True

					elif int(x.number) == x.value:

						cardsCorrect = True

					else:

						cardsCorrect = False
						break

				else:

					cardsCorrect = False
					break
			else:

					cardsCorrect = False
					break

		self.assertTrue(cardsCorrect)
		

class Test_DealCards(unittest.TestCase):

	"""Function Case: This test ensures that the DealCards function gives the same number of cards to the player and the dealer"""
	def test_giving_equal_cards(self):

		testGame = BlackJackClass.BlackJack()
		
		testGame.MakeDeck()

		testGame.DealCards()

		self.assertEqual(len(testGame.player.hand), len(testGame.dealer.hand))

	"""Function Case: This test ensures that the DealCards function gives the right number of cards to the player and dealer"""
	def test_proper_number_of_cards(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		totalCardsDealt = len(testGame.player.hand) + len(testGame.dealer.hand)

		self.assertEqual(totalCardsDealt, 4)

	"""Function Case: This test ensures that the DealCards function sets the deck to start at the proper place for the 
       game after dealing cards"""
	def test_deck_starts_at_proper_place(self):

		testGame = BlackJackClass.BlackJack()

		testGame.MakeDeck()

		testGame.DealCards()

		self.assertEqual(testGame.count, 4)

class Test_CheckWinner(unittest.TestCase):

	"""Function Case: This test ensures that the CheckWinner function works if the dealer goes over 21"""
	def test_dealer_over_21(self):

		testGame = BlackJackClass.BlackJack()

		testString = testGame.CheckWinner(20, 24)

		self.assertEqual(testString, "Player")

	"""Function Case: This test ensures that the CheckWinner function works if the player beats the dealer"""
	def test_player_beats_dealer(self):

		testGame = BlackJackClass.BlackJack()

		testString = testGame.CheckWinner(21, 20)

		self.assertEqual(testString, "Player")

	"""Function Case: This test ensures that the CheckWinner function works if the dealer beats the player"""
	def test_dealer_beats_player(self):

		testGame = BlackJackClass.BlackJack()

		testString = testGame.CheckWinner(20, 21)

		self.assertEqual(testString, "Dealer")

	"""Function Case: This test ensures that the CheckWinner function works if the dealer and the player have the same score"""
	def test_tie_game(self):

		testGame = BlackJackClass.BlackJack()

		testString = testGame.CheckWinner(21, 21)

		self.assertEqual(testString, "Tie Game!")

if __name__ == '__main__':
	unittest.main()
