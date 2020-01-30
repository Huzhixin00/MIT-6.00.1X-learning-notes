print('Please think of a number between 0 and 100!')
low = 0
high = 100
while(True):
    mid = (low+high)/2
    print('Is your secret number ' + str(mid) + '?')
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    action = raw_input(str)
    if action == 'h':
        high = mid
    elif action == 'l':
        low = mid
    elif action == 'c':
        print("Game over. Your secret number was: " + str(mid))
        break
    else:
        print("Sorry, I did not understand your input.")

