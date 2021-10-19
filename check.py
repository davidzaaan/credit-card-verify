import re
import sys

'''This program is based in the Luhn algorithm to check the truthness of a card number'''

aux_variable = 0  # this one too...
# this variable will help us to keep track of the even and odd values...
tracking_var = 1
even_sum = 0
odd_sum = 0
# cards available for checking...
mstr = False
visa = False
amx = False

# User prompting to type the credit card number...
num = input("Enter a number: ").strip()


def check_number(number: str):
    # with the help of regular expressions we can quit all non-numeric values...
    aux_var = re.split("[^0-9]", number)
    str = "".join(aux_var)
    # if the number card length is valid...
    if len(str) < 13 or len(str) > 16:
        print("INVALID")
        sys.exit(1)

    return int(str)


card_number = check_number(num)

while True:
    aux_number = card_number % 10
    aux_variable = 0
    factor = 0
    # aux_number = int(aux_number)  # cast it...

    # Two-spaces counting...
    if tracking_var % 2 == 0:
        aux_number *= 2
        # if the digit doubled is greater than or equals to ten...
        if aux_number >= 10:
            aux_variable = aux_number % 10
            aux_number /= 10
            aux_number = int(aux_number)
            factor = aux_variable + aux_number
            even_sum = even_sum + factor
        else:
            even_sum = even_sum + aux_number
    else:
        odd_sum += aux_number

    # reducing the main number...
    card_number /= 10
    card_number = int(card_number)  # casting it to avoid decimal numbers...

    # Card checking...
    if card_number in [51, 52, 53, 54, 55]:
        mstr = True
    elif card_number == 4:
        visa = True
    elif card_number == 34 or card_number == 37:
        amx = True

    # Loop condition...
    if card_number <= 0:
        break

    tracking_var += 1

# if the module of 10 of the sum of all numbers is equal to zero then...
if (even_sum + odd_sum) % 10 == 0:
    if mstr:
        print("MASTERCARD")
    elif visa:
        print("VISA")
    elif amx:
        print("AMEX")
    else:
        print("VALID BUT NOT IDENTIFIED")
else:
    print("NOT VALID")
