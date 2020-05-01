from Card import *
from Dealer import *
from Player import *
from random import shuffle

class BlackJack:

	def __init__(self):

		self.deck = []
		self.count = 0
		self.player = Player()
		self.dealer = Dealer()

	def MakeDeck(self):

		listSuits = ["Hearts","Diamonds","Clubs","Spades"]
		listNumbers = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
		value = 0

		for x in listSuits:

			for y in listNumbers:

				if y == "Jack" or y == "Queen" or y == "King":

					value = 10

				elif y == "Ace":

					value = 11

				else:

					value = int(y)
		
				newCard = Card(x, y, value)

				self.deck.append(newCard)

		shuffle(self.deck)

	def DealCards(self):

		for x in range(0,4):

			if x % 2 == 0:

				self.player.hand.append(self.deck[self.count])

			else:

				self.dealer.hand.append(self.deck[self.count])

			self.count = self.count + 1

	def PlayGame(self):

		self.DealCards()

		self.player.PrintHand()

		self.dealer.PrintHand()

		if self.player.handValue == 21 and self.dealer.handValue == 21:
	
			return "Tie Game!"

		elif self.dealer.handValue == 21:

			return "Dealer"

		elif self.player.handValue == 21:

			return "Player"

		else:

			self.player.TakeTurn(self.deck, self.count)

			if self.player.handValue > 21:

				print("Player busted!")

				return "Dealer"

			else:
			
				self.dealer.TakeTurn(self.deck, self.count)

				winner = self.CheckWinner(self.player.handValue, self.dealer.handValue)

				return winner		

	def GameLoop(self):

		winner = self.PlayGame()

		if winner == "Tie Game!":

			print("The game is a draw.\n")

		else:

			print("The " + winner + " wins the round! \n")

		playerInput = input("Play again? (Y/N): ")

		if playerInput == "Y":

			self.InitializeGame()


	def CheckWinner(self, playerVal, dealerVal):

		if dealerVal > 21:

			print("Dealer busted!")

			return "Player"

		if playerVal > dealerVal:

			return "Player"

		elif dealerVal > playerVal:

			return "Dealer"

		else:
			
			return "Tie Game!"


	def InitializeGame(self):		

		"""Initializes game the first time"""
		if self.player.hand == [] and self.dealer.hand == []:

			self.MakeDeck()

			self.GameLoop()

		else:

			"""Resets the game for a new round"""
			shuffle(self.deck)
			self.count = 0
			self.player = Player()
			self.dealer = Dealer()

			self.GameLoop()



	

		
