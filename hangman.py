import random
import secret # Module that holds the hints for each song.
import songs # Module that holds all the songs.

# Main loop for the game.
def gameLoop(song):
    # Assigning variables needed for game.
    status = True
    validGuesses = "abcdefghijklmnopqrstuvwxyz0123456789,'"
    lettersGuessed = []
    temp = list(song)
    lives = 6
    update = ''
    winningGuess = ''
    print('\n\nGood luck! The only possible inputs are a-z, 0-9, apostrophes, and commas...\nYou cannot guess the whole song at once.\nYou may use one hint by typing "hint".\n')
    print('Lives:', lives, end ='\n\n')
    # For loop to print out the hidden song.
    for letter in song:
        if letter == ' ':
            print('  ', end = '')
        else:
            print('_', end = ' ')
    # For loop to set the winning guess the user has to achieve.
    for letter in temp:
            if letter in validGuesses:
                winningGuess += letter + ' '
            else:
                winningGuess += '  '

    # While loop which asks the user to input guesses until the user wins or loses.
    while status == True and lives > 0:
        print('\n')
        guess = str(input('Enter a guess: '))
        if guess == 'hint':
            hints(song)
        elif guess not in validGuesses:
            print('\nThat was not a valid guess, Guess again.\n')
            print('Lives:', lives)
            print('\nUSED LETTERS/INPUTS: ', lettersGuessed, '\n')
            print(update)
        elif guess in lettersGuessed:
            print('\nYou have used that guess already, Try another.\n')
            print('Lives:', lives)
            print('\nUSED LETTERS/INPUTS: ', lettersGuessed, '\n')
            print(update)
        elif guess not in song:
            # Condition when a valid input is not incorrect/not in the song.
            lettersGuessed.append(guess)
            lives -= 1
            print('\nWrong! Try again.\n')
            print('Lives:', lives)
            if update == '':
                for letter in song:
                    if letter in lettersGuessed:
                        update += letter + ' '
                    elif letter == ' ':
                        update += '  '
                    else:
                        update += '_' + ' '
            # This if-statement prints out the user's past guesses.
            if lettersGuessed == []:
                None
            else:
                print('\nUSED LETTERS/INPUTS: ', lettersGuessed, '\n')
            if update == '':
                None
            else: 
                print(update)
        elif guess in song:
            # Condition when a valid input is correct/in the song.
            lettersGuessed.append(guess)
            print('\nGood Job! You got it right!\n')
            print('Lives:', lives)
            update = ''
            # This loops updates the hidden word whether the user correctly guessed a letter which then only reveals 
            for letter in song:
                if letter in lettersGuessed:
                    update += letter + ' '
                elif letter == ' ':
                    update += '  '
                else:
                    update += '_' + ' '
            #print(update)
            if lettersGuessed == []:
                None
            else:
                print('\nUSED LETTERS/INPUTS: ', lettersGuessed, '\n')
            if update == '':
                None
            else: 
                print(update)

        # Checks to see if the user has won/lost the game, if he did it will go to a play again option.
        if update == winningGuess:
            print('\nYOU WIN!\n')
            replay()
        elif lives <= 0:
            print('\nYOU LOSE!\n')
            replay()

# Asks the user if they want to play again, if yes it calls the categories function again if no exits the program.
def replay():
    playAgain = str(input('\nPlay again?\n\nYes(y) or No(n)\n'))
    if playAgain == 'Yes' or playAgain == 'yes' or playAgain == 'y':
        categories()
    elif playAgain == 'No' or playAgain == 'no' or playAgain == 'n':
        exit()
    else:
        print('\nNot a valid option. Try again.\n\n')
        replay()



# Prints out the hint of the song the user is trying to guess.
def hints(song):
    print(secret.hints[song])

# Returns a random song from the music genre the user chose.
def getSong(music_category):
    return gameLoop(random.choice(music_category).lower())

# Asks the user to pick a music genre.
def categories():
    category = str(input('\nChoose a music genre\nHIP-HOP | POP | R&B | COUNTRY\n'))
    category = category.lower()
    # This if-statement figures out what genre the user inputted, then calls the getSong() function to pick a random sonf from the genre.
    if category == 'hip-hop':
        category = songs.hiphop
        getSong(category)
    elif category == 'pop':
        category = songs.pop
        return getSong(category)
    elif category == 'r&b':
        category = songs.rnb
        return getSong(category)
    elif category == 'country':
        category = songs.country
        return getSong(category)
    elif category == 'quit':
        exit()
    else:
        print('\n\nInvalid category, Try again.\n')
        categories() # Keeps calling on itself until the user inputs a valid option (hip-hop, pop, r&b, country, or quit).


# Displays the start menu of the game, with the option to play or quit.
def startMenu():
    option = str(input('Welcome to MusicMan!\n- - - - - - - - - -\nThis game is hangman, but with a music twist with it.\nYou\'ll be able to choose a music genre which will\nin turn give you a random song to guess in that genre.\n- - - - - - - - - -\n  Start or Quit\n'))
    # This if-statement figures out what option the user chose, if "start" it condtinues to the next menu and if "quit" the game ends.
    if option == 'start' or option == 'Start':
        print()
        categories()
    elif option == 'quit':
        exit()
    else:
        print('\n\nOption not recognized. Try again.\n')
        startMenu() # Keeps calling on itself until the user inputs a valid option (start or quit).

startMenu()