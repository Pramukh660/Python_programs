import random
import sys
print("\n \t\t\t\t ****** Rock Paper Scissors *****")

# Trck win, loss and tie.
win = 0
loss = 0
tie = 0
print("""Enter:\n r - rock\n p - paper\n s - scissor\n q - quit\n""")

#Main game loop
while True:
    
    #take user input
    user_in = input()
    if user_in == 'r':
        user_out = "You : rock"
    elif user_in == 'p':
        user_out = "You : paper"
    elif user_in == 's':
        user_out = "You : scissor"
    else:
        print(f"Win : {win}\n Loss : {loss}\n Tie : {tie}\n")
        input("Press any key to exit")
        sys.exit()
    
    #take system input
    system_in = random.randint(1, 3)
    if system_in == 1:
        computer_out = "Computer : rock"
    elif system_in == 2:
        computer_out = "Computer : paper"
    else :
        computer_out = "Computer : scissor"

    if user_in == 'r' and system_in == 3:
        print(user_out)
        print(computer_out)
        win += 1
        print("you won\n")
    elif user_in == 'r' and system_in == 2:
        print(user_out)
        print(computer_out)
        loss += 1
        print("Computer won\n")
    elif user_in == 'p' and system_in == 1:
        print(user_out)
        print(computer_out)
        win += 1
        print("You won\n")
    elif user_in == 'p' and system_in == 3:
        print(user_out)
        print(computer_out)
        loss += 1
        print("Computer won\n")
    elif user_in == 's' and system_in == 2:
        print(user_out)
        print(computer_out)
        win += 1
        print("You won\n")
    elif user_in == 's' and system_in == 1:
        print(user_out)
        print(computer_out)
        loss += 1
        print("Computer won\n")
    elif (user_in == 'r' and system_in == 1) or (user_in == 'p' and system_in == 2) or (user_in == 's' and system_in == 3):
        print(user_out)
        print(computer_out)
        tie += 1
        print("Its a tie\n")


   
    
