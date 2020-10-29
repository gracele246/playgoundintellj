from random import randint
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

##########################################################################
# This function is to validate user input and return string 'Yes' or 'No'
##########################################################################
def guessthenum():
 def validate_input_function():
   C_answer = True # initialize to true for while loop conditional
   while C_answer:
     try:
       YourAnswer = input('Would you like to play again? Enter: Yes or No: ')
       if YourAnswer == 'Yes':
         return 'Yes'
       if YourAnswer == 'No':
         return 'No'
       C_answer = False # set conditional to false to exit while loop
     except:
      print('Invalid. Please type valid Yes or No.')
#########################################################################


 print("\u001b[36m   _____                       _   _            _   _                 _ ")
 print("  / ____|                     | | | |          | \ | |               | |        ")
 print(" | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ ")
 print(" | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|")
 print(" | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |  ")
 print("  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   ")
 #secret_number = randint(1,20)
 secret_number = 4
 guess_count = 0
 guess_limit = 3
 Correct_guess = 0
 thisdict = {
   "game": "guess the number",
   "made": "Week one",
   "is it fun": "Yes",
 }
 print(thisdict)
 print('\033[1;35mWhat is your name?')
 myName = input()
 print("First Victim Acquired - " + myName + ", \033[1;32mpick a number between 1-20")
 while guess_count < guess_limit:
    try: #this is how the prizes are generated
        guess = int(input('Guess: '))
        guess_count += 1
        if guess == secret_number:
            print("\u001b[32m You Got Lucky And Won!", myName)
            if guess_count == 1:
              
                def doit(screen):
                  effects =[
                    Cycle(
                          screen,
                            FigletText("You", font='big'),
                            int(screen.height/2-8)),
                    Cycle(
                            screen,
                            FigletText("Won!", font ='big'),
                            int(screen.height/2+3)),
                    Stars(screen,200)
                    ]
                  screen.play([Scene(effects,5000)])
                Screen.wrapper(doit)
              
#######################################################################



########################################################################

            elif guess_count == 2:
                 print("  /\ ___ /\ ")
                 print(" (  o   o  ) " )
                 print("  \  >#<  /")
                 print("  /       \ "  ) 
                 print(" /         \       ^" )
                 print("|           |     //"  )
                 print(" \         /    //  ")
                 print("  ///  ///   --")
            elif guess_count == 3:
               print("  __")
               print("<(o )___")
               print(" ( ._> /")
               print("  `---'  ")
            YourAnswer= validate_input_function()
            if YourAnswer == 'Yes':
                guess_count = 0
                secret_number = randint(1, 20)
            if YourAnswer == 'No':
                print('Bye Now!')
                def main():
                  exec(open("main.py").read())
                break
        elif guess < secret_number:
            print("Guess A Higher Number")
        elif guess > secret_number:
            print("\u001b[33;1mGuess A Lower Number")
        if guess_count == 3:
            print("\u001b[31;1mHAHAHA, You Failed", myName)
            print("\033[1;33mThe Random Number Was", secret_number)
            # YourAnswer = input('Would you like to play again? Enter: Yes or No: ')
            YourAnswer=validate_input_function()
            if YourAnswer == 'Yes':
                print('Good Luck')
                guess_count = 0
                #secret_number= randint(1, 20)
                secret_number = 4
            if YourAnswer == 'No':
                print('So long!')
    except:
        print('Invalid Answer. Please type in a number between 1-20.')
            # print()
            #'eYourAnswer = input('Would you like to play again. Enter: Yes or No: ')
            #validate_function()




'''
else:
  print("\u001b[31;1mHAHAHA, You Failed", myName)
  print("\033[1;33mThe Random Number Was", secret_number )
  print('Would you like to play again enter: Yes or No: ')
  myVar2 = input()
  if myVar2=='Y':
   print(guess_count)
   guess_count=0
   print(guess_count)
#=============================================================

if correct_guess == true:
   print("Would you like to play again?")
   myVar= input()
   set the guess = 0
   if the answer is no break.
if correct_false == false:
   print("Would you like to play again?")
   myVar = input()
   if the answer is yes then set guess=0
   no then break.
'''


  
2
