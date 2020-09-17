import sys


print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    user1 = input("Player 1 enter your name..")
    user2 = input("Player 2 enter your name..")
    player1 = str(input(f"{user1} make your pick...: "))
    player2 = str(input(f"{user2} make your pick...: "))
    a = game_dict.get(player1)
    b = game_dict.get(player2)
    dif = a - b

    if dif in [-1, 2]:
        print(f'{user1} wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print(f'{user2} wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')
