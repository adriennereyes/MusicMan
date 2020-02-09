import random #To give a random song from my lists
import secret #Module that holds the hints for each song
import sys

hipHop = ['The Box']

def gameLoop():
    print('Hello')

def startMenu():
    option = str(input('Welcome to MusicMan\n- - - - - - - - - -\n  Start or Quit\n'))
    option.lower()
    if option == 'start':
        print()
        gameLoop()
    elif option == 'quit':
        sys.exit()
    else:
        print('\n\nOption not recognized. Try again.\n')
        startMenu()

startMenu()