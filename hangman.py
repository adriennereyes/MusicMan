import random #To give a random song from my lists
import secret #Module that holds the hints for each song
import sys

hipHop = ['The Box']

# Main loop for the game
def gameLoop():
    print('Hello')

# Displays the start menu of the game, with the option to play or quit.
def startMenu():
    option = str(input('Welcome to MusicMan\n- - - - - - - - - -\n  Start or Quit\n'))
    if option == 'start' or option == 'Start':
        print()
        gameLoop()
    elif option == 'quit':
        sys.exit()
    else:
        print('\n\nOption not recognized. Try again.\n')
        startMenu()

startMenu()