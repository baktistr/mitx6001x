low = 0
high = 100
answer = 0
guess = ''
print("Please think of a number between 0 and 100!")
while guess != 'c':
    answer = (low + high) // 2 
    print("Is your secret number ", str(answer), end='')
    print("?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if guess != 'h' and guess != 'l' and guess != 'c':
        print("Sorry, I did not understand your input.")
        continue
    elif guess == 'h':
        high = answer
    elif guess == 'c':
        break
    else:
        low = answer
print("Game over. Your secret number was: ", str(answer)) 
