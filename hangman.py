import random
import secret #Module that holds the hints for each song.
import songs #Module that holds all the songs.

# Main loop for the game.
def gameLoop(song):
    status = True
    validGuesses = "abcdefghijklmnopqrstuzwxyz0123456789,'"
    lettersGuessed = []
    temp = list(song)
    lives = 6
    update = ''
    winningGuess = ''
    print('\n\nGood luck! The only possible inputs are a-z, 0-9, apostrophes, and commas...\n You may use one hint by typing "hint".\n')
    #print(song) # DELETE WHEN GAME IS FINISHED
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

    # While loop which asks the user to input guesses until the user wins or loses
    while status == True and lives > 0:
        print('\n')
        guess = str(input())
        if guess == 'hint':
            hints(song)
        elif guess not in validGuesses:
            print('\nThat was not a valid guess, Guess again.')
        elif guess == 'hint':
            hints(song)
        elif guess in lettersGuessed:
            print('\nYou have used that guess already, Try another.\n')
            print(update)
        elif guess not in song:
            lettersGuessed.append(guess)
            print('\nWrong! Try again.\n')
            if update == '':
                for letter in song:
                    if letter in lettersGuessed:
                        update += letter + ' '
                    elif letter == ' ':
                        update += '  '
                    else:
                        update += '_' + ' '
            if lettersGuessed == []:
                None
            else:
                print('USED LETTERS: ', lettersGuessed, '\n')
            if update == '':
                None
            else: 
                print(update)
            lives -= 1
        elif guess in song:
            lettersGuessed.append(guess)
            print('\nGood Job! You got it right!')
            update = ''
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
                print('\nUSED LETTERS: ', lettersGuessed, '\n')
            if update == '':
                None
            else: 
                print(update)

        # Checks to see if the user has won the game, if he did it will exit the game.
        if update == winningGuess:
            print('\nYOU WIN!\n')
            replay()
        elif lives <= 0:
            print('\nYOU LOSE!\n')
            replay()

def replay():
    playAgain = str(input('\nPlay again?\n\n    Yes or No\n'))
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
    category = str(input('Choose a music genre\nHIP-HOP | POP | R&B | COUNTRY\n'))
    category = category.lower()
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
    else:
        print('\n\nInvalid category, Try again.\n')
        return categories()


# Displays the start menu of the game, with the option to play or quit.
def startMenu():
    option = str(input('Welcome to MusicMan\n- - - - - - - - - -\n  Start or Quit\n'))
    if option == 'start' or option == 'Start':
        print()
        categories()
    elif option == 'quit':
        exit()
    else:
        print('\n\nOption not recognized. Try again.\n')
        return startMenu()

startMenu()