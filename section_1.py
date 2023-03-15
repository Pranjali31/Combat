# section_1.py

# Pranjali Prajapati
# 1/12/2023

# this is the section 1 of the game, the first stage where the user start the journey

import section_2
import time

# Start with little info
def start():
    print("You are standing on the mixed edge of jungle near a small village.")
    time.sleep(2)
    print("your pet is lost")
    time.sleep(1)
    print("what would you do??")
    time.sleep(2)

# The use of multi line print
# Choose option 1 or 3 to further the game

    choice = float(input("""
    1. Shout out its name out loud  
    2. Ask near by village person  
    3. Go in jungle to find\n"""))


# This checks submitted answers and take appropriate action
    if (choice == 1):
        print("You shouted the name multiple times, and NOTHING\n")
        time.sleep(2)

        Second_choice = input("Would you like to try again? Y/N  (hint: keep trying helps in the whole game)")

        if Second_choice == "Y":

            section_2.start()

        elif Second_choice == "y":

            section_2.start()

        elif Second_choice == "N":

            Third_choice = input("are you sure? press any key ") # option of ending the game
            if Third_choice == 'Y':
              print("You end game. Try next time")
              exit()

            elif Third_choice == "N":
                from section_1 import start

            elif Third_choice== "n":
                from section_1 import start

            elif Second_choice == "n":

                Third_choice = input("are you sure? press any key to end game, or N/n to continue ")

                if Third_choice == 'y':
                    print("You end game. Try next time")
                    start.end()

                elif Third_choice == "N":
                    from section_1 import start

                elif Third_choice == "n":
                    from section_1 import start


# the choice to which ends the game
    elif (choice == 2):
        print("You ask a lot of People, NO one really knows anything...")
        time.sleep(2)

        print("YOU FAIL TO SAVE YOUR PET, SORRY!!!")
        time.sleep(2)

        print("Try next time...")
        exit()

        # choice 3 also takes you to the next section, a little win kind of game ;)
    elif (choice == 3):

     section_2.start()




