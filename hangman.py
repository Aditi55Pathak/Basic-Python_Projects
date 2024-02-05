import random

Fruits = ["Apple", "Banana", "Orange", "Lichi", "Chikoo", "Mango", "Dragon Fruit"]
Vegies = [
    "Cabbage",
    "Flowers",
    "Brocolies",
    "Drumstick",
    "Capsicum",
    "Chilli",
    "Brinjal",
]
Animals = ["Cat", "Dog", "Racoon", "Cow", "Lion", "Cheetah", "Giraffe"]
streetFood = [
    "Pani Puri",
    "Dabeli",
    "VadaPav",
    "Pavbhaji",
    "Springroll",
    "Magiee",
    "Pasta",
]

print("---------------Welcome to hangman game---------------------")
print()

print("Enter your choice to play : Fruits, Vegies, Animals or streetFood")
user = str(input("--> "))
if (
    user.lower() == "fruits"
    or user.upper() == "FRUITS"
    or user.capitalize() == "Fruits"
):
    print("You have chosen fruits")
    Word = random.choice(Fruits)
    l = len(Word)
    for i in range(4, -1, -1):
        guess = str(input(f"Guess an fruit of lenght {l} :- "))
        if guess == Word:
            print(f"you guessed right one {Word}")
            break
        else:
            print(f"Wrong try again...{i} chance remaining")

elif (
    user.lower() == "vegies"
    or user.upper() == "VEGIES"
    or user.capitalize() == "Vegies"
):
    print("You have chosen Vegies")
    Word = random.choice(Vegies)
    l = len(Word)
    for i in range(4, -1, -1):
        guess = str(input(f"Guess an Vegies of length {l} :- "))
        if guess == Word:
            print(f"you guessed right one {Word}")
            break
        else:
            print(f"Wrong try again...{i} chance remaining")

elif (
    user.lower() == "animals"
    or user.upper() == "ANIMALS"
    or user.capitalize() == "Animals"
):
    print("You have chosen Animals")
    Word = random.choice(Animals)
    l = len(Word)
    for i in range(4, -1, -1):
        guess = str(input(f"Guess an Animals of length {l} :- "))
        if guess == Word:
            print(f"you guessed right one {Word}")
            break
        else:
            print(f"Wrong try again...{i} chance remaining")

elif (
    user.lower() == "streetfood"
    or user.upper() == "STREETFOOD"
    or user.capitalize() == "streetFood"
):
    print("You have chosen streetFood")
    Word = random.choice(streetFood)
    l = len(Word)

    for i in range(4, -1, -1):
        guess = str(input(f"Guess an streetFood of length {l} :- "))
        if guess == Word:
            print(f"you guessed right one {Word}")
            break
        else:
            print(f"Wrong try again...{i} chance remaining")

print()
print("---------------Thankyou for playing hangman game---------------------")
