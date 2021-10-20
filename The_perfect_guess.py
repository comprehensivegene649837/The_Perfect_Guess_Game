from math import e
import random

randnum =  random.randint(1,100)
q= None
userGuess =  None
guess = 3

print("***** Welcome to the THE PERFECT GUESS GAME!***** ")

while True:
    print("type 'q' to exit the game: ", "\n", "or enter the guess: " )
    userGuess = ((input("enter the number: ")))
    
    if userGuess == 'q':
        print("See you next time ;)")
        break

    try:
        
        userGuess = int(userGuess)  
    except Exception as e:
            print("error: ", e)
            continue
    if (userGuess)!=randnum:
        guess= guess -1 
        
    
    
    if (userGuess)==randnum:
        print("you guessed it right!")

    else:  
        if userGuess>randnum:
        
            print("hint: opps! you should have entered a lower number")
        
            print(f"now you have {guess} number of guesses left, be careful!")

        else:
                print("hint: ohh! you were supposed to enter a higher number")
        
                print(f"now you have {guess} number of guesses left, be careful!")


        
    if guess<= 0:
        
        
        print("you ran out of guesses! better luck next time, thanks for playing :)")

        
        break   
    

    
     
   
   
    

    
print("right number: ", randnum)


stop_excecution = input("Press any key to quit: ")
        
