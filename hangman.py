import random #To give a random song from my lists
import secret #Module that holds the hints for each song
import songs #Module that holds all the songs
import sys

# Main loop for the game
def gameLoop(song):
    status = True
    validGuesses = "abcdefghijklmnopqrstuzwxyz0123456789,'"
    lettersGuessed = []
    temp = list(song)
    lives = 6
    update = ''
    print('\n\nGood luck! The only possible inputs are a-z, 0-9, apostrophes, and commas...\n You may use one hint by typing "hint".\n')
    print(song)
    for letter in song:
        if letter == ' ':
            print('  ', end = '')
        else:
            print('_', end = ' ')
    
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
            print('\nYou have used that guess already, Try another.')
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
        for m in lettersGuessed:
            for n in temp:
                if m == n:
                    status = False





def hints(song):
    print(secret.hints[song])

def getSong(music_category):
    return gameLoop(random.choice(music_category).lower())

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
        sys.exit()
    else:
        print('\n\nOption not recognized. Try again.\n')
        return startMenu()

startMenu()