import unittest
from DealerTest import *
from blackjacktest import *
from PlayerTest import *

def suite():

	suite = unittest.TestSuite()

	"""Dealer tests"""
	suite.addTest(Test_Hit('test_hit'))
	suite.addTest(Test_Hit('test_hit_twice'))
	suite.addTest(Test_PrintHand('test_print_hand'))
	suite.addTest(Test_SetHand('test_set_hand'))
	suite.addTest(Test_AddCard('test_add_card'))
	suite.addTest(Test_TakeTurn('test_take_turn'))
	suite.addTest(Test_CheckForAces('test_check_for_aces_true'))

	"""Player tests"""
	suite.addTest(Test_PlayHit('test_hit'))
	suite.addTest(Test_PlayHit('test_hit_twice'))
	suite.addTest(Test_PlayPrintHand('test_print_hand'))
	suite.addTest(Test_PlaySetHand('test_set_hand'))
	suite.addTest(Test_PlayAddCard('test_add_card'))
	suite.addTest(Test_PlayCheckForAces('test_check_for_aces_true'))
	

	"""Blackjack game tests"""
	suite.addTest(Test_MakeDeck('test_make_deck'))
	suite.addTest(Test_MakeDeck('test_all_cards_present'))
	suite.addTest(Test_DealCards('test_giving_equal_cards'))
	suite.addTest(Test_DealCards('test_proper_number_of_cards'))
	suite.addTest(Test_DealCards('test_deck_starts_at_proper_place'))
	suite.addTest(Test_CheckWinner('test_dealer_over_21'))
	suite.addTest(Test_CheckWinner('test_player_beats_dealer'))
	suite.addTest(Test_CheckWinner('test_dealer_beats_player'))
	suite.addTest(Test_CheckWinner('test_tie_game'))


	return suite

if __name__ =='__main__':

	runner = unittest.TextTestRunner()
	runner.run(suite())
