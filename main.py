# THIS IS OUR MENU, WHERE YOU CHOOSE WHAT YOU WANT TO DO

from guessthenumber import guessthenu
from wordguess import word
from calculator import calc

def calculator():
    exec(open("calculator.py").read())


def guessthenumber():
    exec(open("guessthenumber.py").read())


def wordguess():
    exec(open("wordguess.py").read())

def menu():
  print('\u001b[32;1m __  __')                   
  print('\u001b[31m|  \/  |')                 
  print('\u001b[33m| \  / | ___ _ __  _   _ ')
  print("\u001b[34m| |\/| |/ _ \ '_ \| | | |")
  print('\u001b[35m| |  | |  __/ | | | |_| |')
  print("\u001b[36m|_|  |_|\___|_| |_|\__,_|")                        
  print("\u001b[32;1mChoose Something You Want To Do")
  print("===================")
  print("1: Guess the Number")
  print("2: Word guess")
  print("3: Calculator")
  print("4: Exit")
  print("===================")
  print("\u001b[0m ")


while True:
  menu()
  selection = int(input())

  if selection == 1:
    print("This is our number guessing game")   
    guessthenum()

  if selection == 2:
    print("this is word guess")
    word()

  if selection == 3:
    print("this is calculator")
    calc()
  if selection == 4:
    print("Good bye!")
    break
    
