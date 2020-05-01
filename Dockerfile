FROM python
ADD blackjack.py/ Dealer.py/ Player.py/ Card.py / game.py
CMD ["python", "./game.py]
