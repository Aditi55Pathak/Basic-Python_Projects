import random
import string

print("**** Hey User Welcome generate the password **** ")


while True:
    print("Do you want ro generate passowrd? (y or n)")
    user = input("-> ")
    if user == "y":
        user = int(input("Enter the desired length dear user :- "))

        gen = "".join(
            random.choices(
                string.punctuation
                + string.ascii_uppercase
                + string.ascii_lowercase
                + string.digits,
                k=user,
            )
        )

        print(gen)
    else:
        break

print(" *** Thankyou for using me ***")
