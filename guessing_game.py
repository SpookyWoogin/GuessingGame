import time
from msvcrt import getch
import random

while True:
    print("""Lets play a guessing game!
    What's your difficulty?
    1) Easy
    2) Normal
    3) Hard""")
    char_catch = getch()
    difficulty = 0
    while difficulty == 0:
        if b'1' in char_catch:
            print("You've selected: Easy Mode")
            difficulty = 1
        elif b'2' in char_catch:
            print("You've selected: Normal Mode")
            difficulty = 2
        elif b'3' in char_catch:
            print("You've selected: Hard Mode")
            difficulty = 3
        else:
            print("Invalid Mode")
            break
    #"Easy" Mode
    #Programming this hurt my soul ;-;
    if difficulty == 1:
        print("""The computer will select 2 numbers between 1 and 10.
    Your job will be to guess the number that falls between the numbers the computer picked.
    There will be 5 turns.
    If you select the correct number, you will move on to the next turn. If you pass all 5 turns, you win!""")
        time.sleep(3)
        stages = 5
        stages_won = 0
        for x in range(stages):
            comp_num1 = random.randint(1,10)
            comp_num2 = random.randint(1,10)
            user_num = int(input("What number do you choose? (Must be between 1 and 10) "))
            if 1 <= user_num <= 10:
                complarge = 0
                compsmall = 0
                if comp_num1 >= comp_num2:
                    complarge = comp_num1
                if comp_num1 <= comp_num2:
                    compsmall = comp_num1
                if comp_num2 >= comp_num1:
                    complarge = comp_num2
                if comp_num2 <= comp_num1:
                    compsmall = comp_num2
                
                if compsmall <= user_num <= complarge:
                    print(f"""Congrats! You move onto the next stage!
    You chose {user_num}
    The computer chose {comp_num1} and {comp_num2}""")
                    time.sleep(1)
                    stages_won = stages_won + 1
                else:
                    print(f"""Ouch! You lost!
    You chose {user_num}
    The computer chose {comp_num1} and {comp_num2}""")
                    break
            else:
                print("Invalid Number")

    #"Normal" Mode
    if difficulty == 2:
        print("""The computer will select 2 numbers between 1 and 100.
    Your job will be to guess the number that falls between the numbers the computer picked.
    There will be 5 turns.
    If you select the correct number, you will move on to the next turn. If you pass all 5 turns, you win!""")
        time.sleep(3)
        stages = 5
        stages_won = 0
        for x in range(stages):
            comp_num1 = random.randint(1,100)
            comp_num2 = random.randint(1,100)
            user_num = int(input("What number do you choose? (Must be between 1 and 100) "))
            if 1 <= user_num <= 100:
                complarge = 0
                compsmall = 0
                if comp_num1 >= comp_num2:
                    complarge = comp_num1
                if comp_num1 <= comp_num2:
                    compsmall = comp_num1
                if comp_num2 >= comp_num1:
                    complarge = comp_num2
                if comp_num2 <= comp_num1:
                    compsmall = comp_num2
                
                if compsmall <= user_num <= complarge:
                    print(f"""Congrats! You move onto the next stage!
    You chose {user_num}
    The computer chose {comp_num1} and {comp_num2}""")
                    time.sleep(1)
                    stages_won = stages_won + 1
                else:
                    print(f"""Ouch! You lost!
    You chose {user_num}
    The computer chose {comp_num1} and {comp_num2}""")
                    break
            else:
                print("Invalid Number")
    
    #"Hard" Mode
    if difficulty == 3:
        print("""The computer will select 2 numbers between 1 and 1000.
    Your job will be to guess the number that falls between the numbers the computer picked.
    There will be 5 turns.
    If you select the correct number, you will move on to the next turn. If you pass all 5 turns, you win!""")
        time.sleep(3)
        stages = 5
        stages_won = 0
        for x in range(stages):
            comp_num1 = random.randint(1,1000)
            comp_num2 = random.randint(1,1000)
            user_num = int(input("What number do you choose? (Must be between 1 and 1000) "))
            if 1 <= user_num <= 1000:
                complarge = 0
                compsmall = 0
                if comp_num1 >= comp_num2:
                    complarge = comp_num1
                if comp_num1 <= comp_num2:
                    compsmall = comp_num1
                if comp_num2 >= comp_num1:
                    complarge = comp_num2
                if comp_num2 <= comp_num1:
                    compsmall = comp_num2
                
                if compsmall <= user_num <= complarge:
                    print(f"""Congrats! You move onto the next stage!
    You chose {user_num}
    The computer chose {comp_num1} and {comp_num2}""")
                    time.sleep(1)
                    stages_won = stages_won + 1
                else:
                    print(f"""Ouch! You lost!
    You chose {user_num}
    The computer chose {comp_num1} and {comp_num2}""")
                    break
            else:
                print("Invalid Number")
    
    if stages_won == 5:
        print("""Congradulations! You win!

 '._==_==_=_.'
 .-\:      /-.
| (|:.     |) |
 '-|:.     |-'
   \::.    /
    '::. .'
      ) (
    _.' '._
   `"""""""`""")

    print("Would you like to keep playing? Press enter to continue or q to quit")
    char_catch  = getch()
    if b'q' in char_catch:
        exit("Goodbye!")
    elif b'Q' in char_catch:
        exit("Goodbye!")