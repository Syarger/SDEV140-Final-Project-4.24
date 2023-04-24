#SDEV 140 class, Spring 2023, Scott Yarger Final Project Test Validation
#user_input = input('Enter a number ')
#User_input = float(user_input)
#user_input = int(user_input)
#Print(2 + user_input)

while True:
    user_input = input('Enter a number ')
    
    try:
        user_input = int(user_input)
        break

    except ValueError:
        print('INVALID: You need to enter a number!')
        print()

print('You entered: ')
print(user_input)
