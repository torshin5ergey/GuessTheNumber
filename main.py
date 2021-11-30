from random import randrange

print('𝗚𝗨𝗘𝗦𝗦 𝗧𝗛𝗘 𝗡𝗨𝗠𝗕𝗘𝗥')
print('\nWelcome to the game!\n'
'\nHOW TO PLAY\n'
'The program will pick a secret number.\n'
'You guess what number is it.\n'
'Lets start!\n'

'Pick a Level:\n'
'1 - Easy (1 to 10)\n'
'2 - Normal (1 to 100\n'
'3 - Hard (-100 to 100)')

picked_level = int(input())
if picked_level == 1:
    low_num, high_num = 1, 10
    goal_num = randrange(low_num, high_num)
    turns_cap, turns_left = 6, 5
elif picked_level == 2:
    low_num, high_num = 1, 100
    goal_num = randrange(low_num, high_num)
    turns_cap, turns_left = 8, 7
elif picked_level == 3:
    low_num, high_num = -100, 100
    goal_num = randrange(low_num, high_num)
    turns_cap, turns_left = 11, 10

print('\nPick a number between {} and {}.\n'
'You have {} turns left' .format(low_num, high_num, turns_left))
my_num = 0
is_win = False

while turns_left > 0:
    my_num = int(input())
    if my_num < goal_num:
        print('Your guess, {}, is too low.' .format(my_num))
    elif my_num > goal_num:
        print('Your guess, {}, is too high.' .format(my_num))
    else:
        is_win = True
        break
    turns_left -=1
    print('You have {} turns left' .format(turns_left)) 
    
if is_win == True:
    print('Congratulations, you win!\n'
    'It took you {} turns to guess the number.' .format(turns_cap - turns_left))
else:
    print('You lose!')
