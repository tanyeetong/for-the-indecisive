#Header
print('__________ LET ME HELP YOU DECIDE __________')

print('Instructions:')
print('1. Key in options available, press "enter" to key in another option.')
print('2. Once all options have been keyed in, key in "Done" to generate result.')
print()

num = 1
choice = input('Enter Option' + str(num) + ": ").lower()
lst = []
while choice != 'done':
    lst += [choice]
    num += 1
    choice = (input('Enter Option' + str(num) + ": ")).lower()

#Random pick.
import random
chosen = random.randrange(len(lst))

print('*')
print('*')
print('*')

#Display the chosen option.
print(f'Go for {lst[chosen]}!\n')
