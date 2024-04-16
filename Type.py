import time
import random
def ask(a):
    match a:
        case 1:
            print("s1")
        case 2:
            print("s2")
        case 3:
            print("s3")
        case 4:
            print("s4")
a = random.randint(1, 4)
ask(a)
