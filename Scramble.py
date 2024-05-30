import random
import time
def intro():
  print("Hello and welcome to this fun word scrambling game. You will be given a word and you will have to unscramble it. You will be given points for every word you unscramble correctly. You will have to unscramble the word in under 10 seconds. You will be able to add your own words to the list. You must get 10 points to win. Good luck!")
  print(" ")
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
      print(" ")
      print("Please enter yes or no")
      print(" ")
def custom(c):
  word1 = "The"
  word2 = "Power"
  word3 = "Everlasting"
  word4 = "Capitulation"
  word5 = "Eldritch"
  word6 = "Parasitic"
  word7 = "Containment"
  if c == 1:
    print(" ")
    print("You will begin to add your own words to the list. You will be asked how many words you wanna add. It can either be 1, 3, 5, or 7 words.")
    t = 0
    while t == 0:
      print(" ")
      try:    
        num = int(input("How many words would you like to add?: "))
        if num == 1 or num == 3 or num == 5 or num == 7:
          t += 1
        else:
          print(" ")
          print("The number must be 1, 3, 5, or 7")
      except:
        print(" ")
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
  def chose(w1, w2, w3, w4, w5, w6, w7):
    x = random.randint(1, 7)
    match x:
      case 1:
        word = w1
      case 2:
        word = w2
      case 3:
        word = w3
      case 4:
        word = w4
      case 5:
        word = w5
      case 6:
        word = w6
      case 7:
        word = w7
    return word
  def rand(word):
    lword = list(word)
    random.shuffle(lword)
    raword = ''.join(lword)
    return raword
  print(" ")
  input("Click enter to start. When you start the timer will start on the first word. All of the words are %s, %s, %s, %s, %s, %s, and %s. Make sure to unscramble the word in under 10 seconds. Good luck!" % (w1, w2, w3, w4, w5, w6, w7))
  points = 0
  attempts = 0
  while(points < 10):
    print(" ")
    attempts += 1
    word = chose(w1, w2, w3, w4, w5, w6, w7)
    raword = rand(word)
    begin = time.time()
    answer = input("Unscramble the word: %s : " % (raword))
    end = time.time()
    total = end - begin
    if(total > 10):
      print(" ")
      input("You took too long to unscramble the word. You have %d points): Press enter to continue" % (points))
    elif(answer == word):
      points += 1
      print(" ")
      input("Correct the word was %s.You have %d points Press enter to continue" % (word, points))
    else:
      print(" ")
      input("Incorrect the word was %s.You have %d points Press enter to continue" % (word, points))
  return attempts
c = intro()
w1, w2, w3, w4, w5, w6, w7 = custom(c)
attempts = game(w1, w2, w3, w4, w5, w6, w7)
print(" ")
print("You took %d attempts to get 10 points. Thank you for playing this game and have a WONDERFUL rest of your day :)." % (attempts))
