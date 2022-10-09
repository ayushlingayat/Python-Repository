#Intern'spedia 
#Intern'spedia Task 2 - Text Based Adventure Game 

answer_yes = ["Yes" , "Y" , "yes" , "y"]
answer_no = ["No" , "N" , "no" , "n"]

print('''Welcome lets start the adventure ! 
If a stranger wants some urgent cash would you help the stranger
or not ? (Yes/No)''')

ans_1 = input(">>")

if ans_1 in answer_yes :
    print('''Would you ask the stranger why would you want the cash 
    urgently? (Yes/No)''')

    ans_2 = input(">>")

    if ans_2 in answer_yes:
        print("You won it because you helped the person in need and used your brain \nWON !")

    elif ans_2 in answer_no:
        print("\nYou cannot give anyone Cash Without Knowing the reason.\nGAME OVER !")

    else:
        print("You typed the wrong input you are disqualified from the game \nDISQUALIFIED")

elif ans_1 in answer_no:
    print("Now he is trying to kill would you fight back (Yes/No)")

    ans_3 = input(">>")

    if ans_3 in answer_yes:
        print("Congrats you saved your life and safety is first priority \nWON!")

    elif ans_3 in answer_no:
        print("Sorry you are dead because you dont block the attack \nGAME OVER !")
    
    else:
        print("You typed the wrong input you are disqualified from the game \nDISQUALIFIED")


else:
    print("You typed the wrong input disqualified \nDISQUALIFIED")