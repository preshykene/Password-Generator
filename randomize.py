import random

class MustNotLessThanSixOrEqualToZero():
    pass

class MustNotBeMoreThanTwentyOrEqualToZero():
    pass


def RandomPass():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    symbol = str("!@#$%^&*()_+-}{:>][<,<./")
    output = lower + upper + symbol
    length = int(input("What password length you prefer?: "))

    password  = "".join(random.sample(output, length))
    if length <= 6:
        try:
            print("Raising exception")
            raise MustNotLessThanSixOrEqualToZero
        except:
            print("Password should not be less than Six!!!")
    elif length >= 20:
        try:
            print("Raising exception")
            raise MustNotBeMoreThanTwentyOrEqualToZero
        except:
            print("Password should not be more than Twenty")
    else:
            print("Your password is: ", password)

RandomPass()