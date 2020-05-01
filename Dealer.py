from Card import *

class Dealer:

	def __init__(self):

		self.stayValue = 17
		self.hand = []
		self.handValue = 0

	def Hit(self, deck, count):

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

	def PrintHand(self):

		tempHandVal = 0

		print("Dealer's Hand: ")

		for x in range(0, len(self.hand)):

			if x == 0:

				print("???")

			else:

				print(self.hand[x].number + " of " + self.hand[x].suit)

			tempHandVal += self.hand[x].value

		self.handValue = tempHandVal

		hiddenHandVal = self.handValue - self.hand[0].value

		print("Hand Value: " + str(hiddenHandVal) + " + ??? \n")

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

		print("\nDealer's turn...\n")

		while turnEnd is False:

			count = count + 1

			self.PrintHand()

			if self.handValue < self.stayValue:
				
				self.Hit(deck, count)

				if self.handValue > 21:

					turnEnd = CheckForAces()

					if turnEnd is True:

						print("Final Dealer Hand: ")

						for x in self.hand:

							print(x.number + " of " + x.suit)

						print("Final Dealer Hand Value: " + str(self.handValue))			
		
			else:

				print("Final Dealer Hand Value: " + str(self.handValue))

				turnEnd = True

