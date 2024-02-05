import random

print("**** Hey User Welcome to our guess game **** ")

comp = random.randint(0, 100)
# print(comp)

while True:
    print("Enter your guessed number :- ")
    user = int(input())
    if user > comp:
        print("Number is too high guess smaller")
    elif user < comp:
        print("Number is too low guess Higher ")
    else:
        print(f"You gotta the correct one {comp} and {user} # You won")
        break

print("*** End of game ***")
