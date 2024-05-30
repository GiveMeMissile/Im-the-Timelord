import random
import time
def intro():
  print("Hello and welcome to this fun word scrambling game. You will be given a word and you will have to unscramble it. You will be given points for every word you unscramble correctly. You will have to unscramble the word in under 10 seconds. You will be able to add your own words to the list. You must get 10 points to win. Good luck!")
  c = 0
  while(c == 0):
    custom = input("Would you like to add your own words to the list?: ")
    if custom == "yes":
      c = 1
      return c
    elif custom == "no":
      c = 2
      return c
    else:
      print("Please enter yes or no")
def custom(c):
  word1 = "The"
  word2 = "Power"
  word3 = "Infinite"
  word4 = "Capitulation"
  word5 = "Dictator"
  word6 = "Parasitic"
  word7 = "Relations"
  if c == 1:
    print("You will begin to add your own words to the list. You will be asked how many words you wanna add. It can either be 1, 3, 5, or 7 words.")
    t = 0
    while t == 0:
      try:    
        num = int(input("How many words would you like to add?: "))
        if num == 1 or num == 3 or num == 5 or num == 7:
          t += 1
        else:
          print("The number must be 1, 3, 5, or 7")
      except:
        print("Please enter a number")
    if(num == 1):
      word1 = input("Enter your first word: ")
      return word1, word2, word3, word4, word5, word6, word7
    elif(num == 3):
      word1 = input("Enter your first word: ")
      word2 = input("Enter your second word: ")
      word3 = input("Enter your third word: ")
      return word1, word2, word3, word4, word5, word6, word7
    elif(num == 5):
      word1 = input("Enter your first word: ")
      word2 = input("Enter your second word: ")
      word3 = input("Enter your third word: ")
      word4 = input("Enter your fourth word: ")
      word5 = input("Enter your fifth word: ")
      return word1, word2, word3, word4, word5, word6, word7
    elif(num == 7):
      word1 = input("Enter your first word: ")
      word2 = input("Enter your second word: ")
      word3 = input("Enter your third word: ")
      word4 = input("Enter your fourth word: ")
      word5 = input("Enter your fifth word: ")
      word6 = input("Enter your sixth word: ")
      word7 = input("Enter your seventh word: ")
  else:
    return word1, word2, word3, word4, word5, word6, word7
def game(w1, w2, w3, w4, w5, w6, w7):
  def scramble(word1, word2, word3, word4, word5, word6, word7):
    x = random.randint(1, 7)
    match x:
      case 1:
        word = word1
      case 2:
        word = word2
      case 3:
        word = word3
      case 4:
        word = word4
      case 5:
        word = word5
      case 6:
        word = word6
      case 7:
        word = word7
    random.shuffle(word)
    return word
  v = input("Click enter to start. One you start the timer will start on the first word. All of the words are %s, %s, %s, %s, %s, %s, and %s. Make sure to unscramble the word in under 10 seconds. Good luck!" % (w1, w2, w3, w4, w5, w6, w7))
  word1 = list(w1)
  word2 = list(w2)
  word3 = list(w3)
  word4 = list(w4)
  word5 = list(w5)
  word6 = list(w6)
  word7 = list(w7)
  points = 0
  while(points < 10):
    word = scramble(word1, word2, word3, word4, word5, word6, word7)
    
c = intro()
w1, w2, w3, w4, w5, w6, w7 = custom(c)
