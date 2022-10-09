#Intern'spedia
#Intern'spedia Task 1 - Guessing game
import math
import random

#Taking inputs to guess here 

lower =  int(input("Enter the Lower Number :"))

upper = int(input("Enter the Bigger Number :"))

#Now we will generate random number here 

y = random.randint(lower,upper)
print("\nYou  have only ", round(math.log(upper - lower + 1 , 2)),
'''few chances to guess the correct number''')

#Initialize the number of guesses

count = 0

#Calculation of minimum number of edges depending upon range 

while count<math.log(upper-lower + 1, 2):
    count+=1

#Now here we will take guess number as a input here 

    guess = int(input("Enter the number you liked to guess : "))

#And now lets test the condition 

    if y==guess:
        print("Congratulations! folks you did it in ",count,"attempts")
        break #once guessed loop will break here 
    elif y>guess:
        print("The number you guessed is to small")
    elif y<guess:
        print("The number you guessed is to big")

#if guessing goes more than required guesses then this will be shown 

if count>= math.log(upper-lower + 1, 2):
    print("The number is %d " %y)
    print("Better luck next time")
    


