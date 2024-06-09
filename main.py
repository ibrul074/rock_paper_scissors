import random

#npc choose a number between 1 and 3
npc_choice_int = random.randint(1,3)

user_choice_str = input("choose 1 for rock, 2 for paper and 3 for scissors: ")

while user_choice_str != "1" and user_choice_str != "2" and user_choice_str != "3":
    print("Sorry I didn't understand. Choose 1 for rock, 2 for paper or 3 for scissors")
    user_choice_str = input("choose 1 for rock, 2 for paper and 3 for scissors: ")

user_choice_int = int(user_choice_str)

#convert choice integers in words (rock, paper or scissors)
#create a function that convert 1 for rock...
def convert_in_str(choice):
    if choice == 1:
        return "rock"
    elif choice == 2:
        return "paper"
    else:
        return "scissors"

user_choice_name = convert_in_str(user_choice_int)
npc_choice_name = convert_in_str(npc_choice_int)

#who won
def who_won(npc_choice,user_choice):
    if npc_choice == 1 and user_choice == 2:
        return "user"
    elif npc_choice == 1 and user_choice == 3:
        return "npc"
    elif npc_choice == 2 and user_choice == 1:
        return "npc"
    elif npc_choice == 2 and user_choice == 3:
        return "user"
    elif npc_choice == 3 and user_choice == 1:
        return "user"
    else:
        return "npc"
    
winner = who_won(npc_choice_int,user_choice_int)
        
#determine if its the user or the npc who won
if winner == "user":
    print("You won!")
    print(f"you chose {user_choice_name} and the computer chose {npc_choice_name}")

elif winner == "npc":
    print("You lose!")
    print(f"you chose {user_choice_name} and the computer chose {npc_choice_name}")

else:
    print("It's a tie!")
    print(f"you chose {user_choice_name} and the computer chose {npc_choice_name}")


if __name__ == '__main__':
    pass

