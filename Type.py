import time
import random
def results(Error, total):
    total_time = round(total)
    e = 1234567890
    while e == 1234567890:
        end = input("You took %d seconds and had a total of %d Errors. Would you like to try again?(yes or no): " % (total_time, Error))
        if(end == "yes"):
            print("Ok lets try again!")
            e = 0
            return e
        elif(end == "no"):
            print("Ok, Thank you for using this program and have a WONDERFUL day (:")
            return e
        else:
            print("You must put in a yes or no (No capital letters).")
def collect(typed, sent):
    typ = len(typed)
    sen = len(sent)
    if(typ != sen):
        if(typ > sen):
            Error = typ - sen
        elif(sen > typ):
            Error = sen - typ
    else:
        Error = 0
    typeded = list(typed)
    sented = list(sent)
    for typededs, senteds in zip(typeded, sented):
        if(typededs != senteds):
            Error += 1
    return Error
def asked(sent):
    input("You must rewrite the entire sentence below as quickley as possible. You will be timed and should try to type it as fast as possible with as little errors as possible. Press enter when you are ready. good luck.")
    print(sent)
    start = time.time()
    print("Type the sentence above. Write it below this sentence")
    typed = input("")
    end = time.time()
    total = end - start
    return typed, total
def sentence(a):
    match a:
        case 1:
            sent = "The game Bad Piggies is the best game of all time. It is a work of art with its amazing soundtrack and fun puzzels. Its a game that challenges your mind and makes you think. While also being very fun. It is a true nostalgic masterpiece and will be remembered for the rest of time."
        case 2:
            sent = "The word Capitulation is the most fun word to say ever (In my opinion). The word means the collpase of a building or some other thing. Its a word that fits its meaning. Whenever you say Capitulation it makes you feel like something just broke and is collapsing. It is truley one of if not the best word in history."
        case 3:
            sent = "Do you know what is in the center of a black hole. Well it is theorized to be something known as a Singularity. A Singularity is a thing that has no volume and is infinitly dense. Singularities are insane being able to warp reality and bend space time. Though for better or worse chances are these thing dont really exist. They are most likely just flaws in our currect theories and we will need to make better theories to really find out what is in the center of a black hole."
        case 4:
            sent = "There are many creatures in this universe. But the most strange and unusual of these creatures would be humans. Humans are strange beings. They make some strange things like memes and art. They will spend hours every day on these meaningless thing for some reason. Its almost endering in a strange way. Hm."
    return sent
e = 0
while e == 0:
    a = random.randint(1, 4)
    sent = sentence(a)
    typed, total = asked(sent)
    Error = collect(typed, sent)
    e = results(Error, total)
