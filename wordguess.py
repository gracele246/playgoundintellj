from random import randint
#This code defines the words the computer will generate when the game is played.

#word bank
def word():
  '''
  words = ["aback","abaft","abandoned","abashed","aberrant","abhorrent","abiding","abject","ablaze","able","abnormal","aboard","aboriginal","abortive","abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted","absurd","abundant","breezy","brief","bright","bright","broad","broken","brown","bumpy","burly","bustling","busy","coordinated","courageous","crabby","craven","crazy","creepy","crooked","crowded","cuddly","cultured","cumbersome","curious","curly","curved","curvy","cut","cute","cute","cynical","daffy","daily","damaged","damaging","damp","dangerous","dapper","dark","dashing","dazzling","dead","eager","early","even","excellent","excited","exciting","exclusive","exotic","expensive","extra-large","extra-small","exuberant","exultant","fabulous","faded","faint","fair","flimsy","flippant","flowery","fluffy","fluttering","foamy","foolish","foregoing","forgetful""fuzzy","gabby","gainful","gamy","gaping","garrulous","gaudy","general","gentle","giant","giddy","gifted","gigantic","glamorous","gleaming","glib","glistening","glorious","glossy","godly","good","goofy","gorgeous","graceful","grandiose","grateful","gratis","gray","greasy","great","greedy","green","grey","grieving","groovy","grotesque","grouchy","grubby","healthy","heartbreaking","heavenly","heavy","helpful","helpless","hesitant","hideous","husky","hypnotic","hysterical","icky","icy","ignorant","ill","illegal","illustrious","imaginary","immense","imminent","impartial","imperfect","impolite","important","imported","impossible","incandescent","incompetent","inconclusive","industrious","incredible","itchy","jaded","jagged","jazzy","jealous","jittery","jobless","jolly","joyous","judicious","juicy","jumbled","jumpy","juvenile","kaput","keen","kind","kindhearted","kindly","knotty","knowing","knowledgeable","known","labored","languid","large","last","late","merciful","mere","messy","mighty","military","milky","mindless","miniature","minor","naive","nappy","narrow","nasty","natural","naughty"]
  '''

  with open('wordlist.txt', 'r') as f:
    text = f.read()
    words = text.split('\n')


  word_count = len(words) 
  word_index = randint(0, word_count-1)
  selected_word = words[word_index]
  hidden_word = ["_"]*len(selected_word)

  while True:

    print(' '.join(hidden_word))
  
    print("Guess a letter...")
    guess = input().lower()

    while len(guess) > 1:
      print("Enter only one letter!")
      guess = input().lower()
  
    if guess in selected_word:
      print("Good Job!")
      for index, letter in enumerate(selected_word):
        if guess == letter:
          hidden_word[index] = guess

    else:
      print("Sorry. Not a letter in the word.")

   #ASCII ART
    print() 

    if '_' not in hidden_word:
        print("                         ____")
        print("                   .---'-    \ " )
        print("      .-----------/           \ ")
        print("     /           (         ^  |   __"  )
        print("&   (             \        O  /  / .'")
        print("'._/(              '-'  (.   (_.' /")
        print("     \                    \     ./")
        print("      |    |       |    |/ '._.'")
        print("       )   @).____\|  @ |")
        print("   .  /    /       (    | mrf")
        print("  \|, '_:::\  . ..  '_:::\ ..\).")
        print("\u001b[32m GOOD JOB!!!")


        print('Would you like to play again?')
        print("Enter Yes or No: ")
        YourAnswer = input()
        if YourAnswer == 'Yes':
          word_count = len(words)
          word_index = randint(0, word_count-1)
          selected_word = words[word_index]
          hidden_word = ["_"]*len(selected_word)
        if YourAnswer == 'No':
          print('Goodbye!!!')
          break
  

      