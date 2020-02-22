import random #To give a random song from my lists
import secret #Module that holds the hints for each song
import songs #Module that holds all the songs
import sys

# Main loop for the game
def gameLoop(song):
    status = True
    letters_guessed = []
    lives = 6
    print('\n\nGood luck! The only possible inputs are A-Z, 0-9, and apostrophes...\n You may use one hint by typing "hint".')
    print(len(song) * '_ ')
    
    while status == True:
        pass



def hints():
    pass

def getSong(music_category):
    return gameLoop(random.choice(music_category))

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