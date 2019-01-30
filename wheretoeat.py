#Header
print('__________ LET ME HELP YOU DECIDE __________')

#User's input
no_of_options = int(input('How many options do you have> '))

#In the case where meaning of "choice(S)" not met, prompts user for a new number. 
if no_of_options <= 1:
    print("NOTE: Please enter a number with value more than 1.\nIf you have only 1 option, you don't need this.\n")
    no_of_options = int(input('How many options do you have> '))

print('*')
print('*')
print('*')

#User's inputs and collates all the options.
print('What are the options?')
list = [' ']
for i in range(1, no_of_options + 1):
    where = input('Enter Option '+ str(i) + '> ')
    list = list + [where]

print('*')
print('*')
print('*')

#Random pick.
import random
chosen = random.randrange(1,no_of_options)

#Display the chosen option.
print(f'Go for {list[chosen]}!\n')
