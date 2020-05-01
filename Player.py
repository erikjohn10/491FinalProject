from Card import *

class Player:

	def __init__(self):

		self.hand = []
		self.handValue = 0
		self.playerInput = ""

	def Hit(self,deck, count): 

		self.hand.append(deck[count])

	"""Helper function for testing purposes"""
	def SetHand(self, card1, card2):

		self.hand[0] = card1
		self.hand[1] = card2

		self.handValue = self.hand[0].value + self.hand[1].value

	"""Helper function for testing purposes"""
	def AddCard(self, newCard):

		self.hand.append(newCard)

		self.handValue += newCard.value

	def GetPlayerInput(self):

		pInput = input("What do you want to do? (Hit/Stand): ")

		return pInput

	def PrintHand(self):

		tempHandVal = 0

		print("Player's Hand: ")

		for x in self.hand:

			print(x.number + " of " + x.suit)

			tempHandVal += x.value

		self.handValue = tempHandVal

		print("Hand Value: " + str(self.handValue) + "\n")

	def CheckForAces(self):

		turnEnd = False

		for x in self.hand:

			if x.number == "Ace":

				if x.value != 1:

					x.setValue(1)
					self.handValue = self.handValue - 10
					turnEnd = False
					break
				else:

					turnEnd = True

		return turnEnd

	def TakeTurn(self, deck, count):

		turnEnd = False

		while turnEnd is False:

			count = count + 1

			self.playerInput = self.GetPlayerInput()

			if self.playerInput == "Hit":

				self.Hit(deck, count)

				self.PrintHand()

				if self.handValue > 21:

					turnEnd = CheckForAces()

			elif self.playerInput == "Stand":

				turnEnd = True

			else:

				print("\n You have entered an invalid option. Valid options are 'Hit' or 'Stand'.\n")


			

