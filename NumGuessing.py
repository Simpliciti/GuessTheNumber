#Random Number Gens and You gotta guess. Yeah!
import random


print(r"________  ___  ___  _______   ________   ________           _________  ___  ___  _______          ")
print(r"|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\         |\___   ___\\  \|\  \|\  ___ \         ")
print(r"\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_        \|___ \  \_\ \  \\\  \ \   __/|        ")
print(r" \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \            \ \  \ \ \   __  \ \  \_|/__      ")
print(r"  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \            \ \  \ \ \  \ \  \ \  \_|\ \     ")
print(r"   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \            \ \__\ \ \__\ \__\ \_______\    ")
print(r"    \|_______|\|_______|\|_______|\_________\\_________\            \|__|  \|__|\|__|\|_______|    ")
print(r"                                 \|_________\|_________|                                           ")
print("\n\n")                                                                                                                                                                                         
print(r" ________   ___  ___  _____ ______   ________  _______   ________  ___                             ")
print(r"|\   ___  \|\  \|\  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \|\  \                            ")
print(r"\ \  \\ \  \ \  \\\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \ \  \                           ")
print(r" \ \  \\ \  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\ \  \                          ")
print(r"  \ \  \\ \  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \\ \__\                         ")
print(r"   \ \__\\ \__\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\\|__|                         ")
print(r"    \|__| \|__|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|   ___                       ")
print(r"                                                                        |\__\                      ")
print(r"                                                                        \|__|                      ")
print(r"                                                                                                   ")
print("Tis a simple game. Dont expect much outta it.")
a = int(input("Enter the minimum value of range: "))
b = int(input("Enter the maximum value of range: "))
i=random.randint(a,b)
chances = 1
def Inputting():
    global a
    global b
    print("A number has been generated between",a,"and",b)
    print("Let the GUessing begin!")
    countable = str(i)
    print("Hot Tip! The number has:",len(countable),"digits. Lol.")
    global chances
    chances = 1
    while True:
        choiice = int(input("Guess the number: "))
        if choiice == i:
            print("You Won, You SOB!")
            print("Congo. bye")
            Endprompt()
        elif choiice < a or choiice > b:
            print("DId you really just go out of range dude. \nAfter defining it like a few seconds ago. T_T")
            continue
        elif choiice > i and choiice > a and choiice < b:
            print("The number's smaller than this dude!")
            print("The range changes accordingly... AGAIN!")
            b = choiice
            chances +=1
            continue
        elif choiice < i and choiice > a and choiice < b:
            print("The number's bigger bruh. T_T")
            print("Range Updated. ~ Off you go!")
            a = choiice
            chances+=1
            continue
        else:
            print("I didnt predict this error dude. seriously. GG.")
            print("Now focus on the game, faggot")
            continue        

Inputting()

def Endprompt():
    global chances
    print("Thanks for playing. This was a fun project completely made at 2:16 a.m. \nBtw, you took",chances,"chances...")
    print("I dont know why I defined a function just for this particular sentence. ")
    print("~ Terminated.")
    SystemExit()
