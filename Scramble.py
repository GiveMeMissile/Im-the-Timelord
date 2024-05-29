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
    elif(num == 3):
      word1 = input("Enter your first word: ")
      word2 = input("Enter your second word: ")
      word3 = input("Enter your third word: ")
    elif(num == 5):
      word1 = input("Enter your first word: ")
      word2 = input("Enter your second word: ")
      word3 = input("Enter your third word: ")
      word4 = input("Enter your fourth word: ")
      word5 = input("Enter your fifth word: ")
    elif(num == 7):
      word1 = input("Enter your first word: ")
      word2 = input("Enter your second word: ")
      word3 = input("Enter your third word: ")
      word4 = input("Enter your fourth word: ")
      word5 = input("Enter your fifth word: ")
      word6 = input("Enter your sixth word: ")
      word7 = input("Enter your seventh word: ")
  else:
    start = input("Would you like to start the game?: ")
    return start
c = intro()
