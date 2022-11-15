# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: november 2022
# ICS3U-Unit4-04.py File, learning break statement in python.

import random


def main():

    # input and variables
    random_number = random.randint(0, 9)
    input_number = input("Guess the number from 0 to 9: ")

    # process and output
    print("")
    try:
        input_number_asint = int(input_number)
        while True:
            if int(input_number_asint) == random_number:
                print("You guessed right.")
                break
            elif input_number_asint < 0 or input_number_asint > 9:
                print("Please enter a number between 0 and 9.")
            input_number_asint = int(input("You guessed wrong, please try again: "))
    except ValueError:
        print(
            'invalid input, "{0}" does not fit the requirements.'.format(input_number)
        )
        print("Please try again and input a whole number between 0 and 9.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
