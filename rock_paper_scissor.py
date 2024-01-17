import os
import random


def rock_sign():
    
    rockk='''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣷⡄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⠙⠻⠿⠋⣰⣿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣶⣤⣌⡙⠻⡿⢃⣾⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⡿⢿⣿⣿⣿⠃⠘⣠⣾⣿⣿⠟⢁⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣧⣄⡈⠡⣄⠀⢼⣿⣿⡿⠋⣰⣿⣿⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⡄⢹⣿⣦⣉⠛⢁⣾⣿⣿⡟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣷⣄⠙⠿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⡀⢻⣿⣿⣿⣿⣦⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣷⣤⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
    print(rockk)
    


def scissor_sign():
    signn='''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠉⠉⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣤⡶⠶⢶⣤⣄⣀⠘⠛⠶⣴⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣾⡇⠀⠀⠀⠈⠙⢿⣿⣷⣶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢷⣄⡀⠀⠀⢀⣸⡟⠉⠙⠻⣿⣿⣿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠛⠛⠛⠛⠉⠀⠀⢸⣦⣄⡉⠛⠿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣆⠀⠀⠙⠻⢿⣿⣿⣿⣿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣦⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠓⠀⠀⠀⠀⠀⠀⠀⠀'''
    print(signn)


def paper_sign():
    papaerr='''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣿⣿⡿⠋⣀⣀⣀⣀⣀⣤⣤⣤⣶⣶⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡏⢀⣶⣿⣿⣿⣿⡿⠿⠿⠛⠛⠋⠁⠀⠀⠀
⠀⠀⣾⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣯⣁⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⢉⣁⣴⣿⣿⣿⣿⣉⣉⣉⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠉⠉⠉⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⢿⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⢿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
    print(papaerr)
    
outcomes_dict = {"1": rock_sign, "2": paper_sign, "3": scissor_sign}

outcomes = [1, 2, 3]
print("Welcome to Rock Paper Scissor Game")
flag = 1
temp = 1
while flag:
    game = int(input("Enter 1 to Start the Game and 0 to Exit: "))

    if game == 0:
        break
    while temp:
        game_type = int(input("1) vs Player / 2) vs Robot: "))

        if game_type == 1:
            name_1 = input("Enter User 1 Name: ")
            name_2 = input("Enter User 2 Name: ")

            print("Let's Start the Game: ")

            input_1 = input(f"Enter {name_1}\n (1)ROCK \n (2)PAPER \n (3)SCISSOR): ")
            user1_input = outcomes_dict[input_1]
            user1_input()
            os.system("clear")

            input_2 = input(f"Enter {name_2}\n (1)ROCK \n (2)PAPER \n (3)SCISSOR): ")
            user2_input = outcomes_dict[input_2]
            user2_input()
            os.system("clear")

            print(f"{name_1} Inputs: ")
            user1_input()

            print(f"{name_2} input: ")
            user2_input()

            if input_1 == input_2:
                print("TIE")

            elif input_1 == "1" and input_2 == "3":
                print(f"{name_1} Win")

            elif input_1 == "1" and input_2 == "2":
                print(f"{name_2} Win")

            elif input_1 == "2" and input_2 == "3":
                print(f"{name_2} Win")

            elif input_1 == "2" and input_2 == "1":
                print(f"{name_1} Win")

            elif input_1 == "3" and input_2 == "2":
                print(f"{name_1} Win")

            elif input_1 == "3" and input_2 == "1":
                print(f"{name_2} Win")

            else:
                print("Invalid Input!")
            break

        elif game_type == 2:
            name_1 = input("Enter User 1 Name: ")

            print("Let's Start the Game: ")

            input_1 = input(f"Enter {name_1}\n (1)ROCK \n (2)PAPER \n (3)SCISSOR): ")
            user1_input = outcomes_dict[input_1]
            user1_input()
            os.system("clear")

            input_2 = random.choice(outcomes)
            user2_input = outcomes_dict[str(input_2)]
            user2_input()
            os.system("clear")

            print(f"{name_1} Inputs: ")
            user1_input()

            print("Robot input: ")
            user2_input()

            if input_1 == str(input_2):
                print("TIE")

            elif input_1 == "1" and str(input_2) == "3":
                print(f"{name_1} Win")

            elif input_1 == "1" and str(input_2) == "2":
                print("Robot Win")

            elif input_1 == "2" and str(input_2) == "3":
                print("Robot Win")

            elif input_1 == "2" and str(input_2) == "1":
                print(f"{name_1} Win")

            elif input_1 == "3" and str(input_2) == "2":
                print(f"{name_1} Win")

            elif input_1 == "3" and str(input_2) == "1":
                print("Robot Win")

            else:
                print("Invalid Input!")
            break

        else:
            print("Invalid Input")
            temp = 1