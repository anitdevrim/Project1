# COM2044 // PROJECT-1
# Anıt Devrim Akdeniz
# 19291078



import random

types = ["Diamonds","Hearts","Spades","Clubs"]
values = list(range(2,15))


player_score = 0
computer_score = 0
winning_number = 3
player_card = ""
computer_card = ""


faceCards = {
    11: "J",
    12: "Q",
    13: "K",
    14: "A"
}

card_values = {

    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14

}



class Card(object):
    def __init__(self,value,type):
        self.type = type
        self.value = value

def generateCards(values,types):
    deckOfCards = []
    for i in values:
        for j in types:
            if i in faceCards:
                card_value = faceCards[i]
                deckOfCards.append(Card(card_value, j))
            else:
                deckOfCards.append(Card(i,j))
    return deckOfCards

deckOfCards = generateCards(values,types)

print('\x1b[6;30;46m' + '-----------------Welcome To Our Card Game-----------------' + '\x1b[0m')
print('\x1b[6;30;46m' +'-----In this game you will draw cards from our shuffled deck with 52 cards on it.-----' + '\x1b[0m')
print('\x1b[6;30;46m' +'--------Your goal is to get a higher card then the computer to win.--------' + '\x1b[0m')
print('\x1b[6;30;46m' +'-----------------The game ends in 3.-----------------' + '\x1b[0m')


while True:

    player_card = random.choice(deckOfCards)
    print("Your card is {} of {}.".format(player_card.value, player_card.type))

    computer_card = random.choice(deckOfCards)
    print("Computer's card is {} of {}.".format(computer_card.value, computer_card.type))

    if card_values[player_card.value] > card_values[computer_card.value]:
        player_score = player_score + 1
        print("!!You win the round!!")
        print("!!!YOU= {} COMPUTER={}!!!".format(player_score, computer_score))
        player_card = ""
        computer_card = ""
    elif card_values[player_card.value] < card_values[computer_card.value]:
        computer_score = computer_score + 1
        print("!!You lose the round!!")
        print("!!!YOU= {} COMPUTER={}!!!".format(player_score, computer_score))
        player_card = ""
        computer_card = ""
    elif card_values[player_card.value] == card_values[computer_card.value]:
        print("!!It's a tie game.!!")
        print("!!!YOU= {} COMPUTER={}!!!".format(player_score, computer_score))
        player_card = ""
        computer_card = ""

    
    if player_score == 3:
        print('\x1b[6;30;42m' +'-----!!Congrats!! YOU WIN!!-----' + '\x1b[0m')
        break
    elif computer_score == 3:
        print('\x1b[6;30;41m' + '-----!!Sorry!! YOU LOST!!-----' + '\x1b[0m' )
        break
    else:
        input1 = input("Press enter to continue.")
        continue