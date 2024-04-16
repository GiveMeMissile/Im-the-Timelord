import time
import random
def asked(b):
    input("You must rewrite the entire sentence below as quickley as possible. You will be timed and should try to type it as fast as possible with as little errors as possible. Press enter when you are ready. good luck.")
    print(b)
    start = time.time()
    typed = input("Type the sentence above here: ")
    end = time.time()
    total = end - start
    print(total)
def sentence(a):
    match a:
        case 1:
            b = "The Placeholder"
        case 2:
            b = "Placeholder"
        case 3:
            b = "Another Placeholder"
        case 4:
            b = "Placeholder 2.0"
    return b
a = random.randint(1, 4)
b = sentence(a)
asked(b)
