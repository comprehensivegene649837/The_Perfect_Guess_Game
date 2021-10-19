import random
randnum =  random.randint(1,100)

userGuess =  None
guess = 3
print("****Welcome to the THE_PERFECT_GUESS_GAME*****")
while True: #(userGuess!=randnum):
    userGuess = int(input("guess the number: "))
    
    if userGuess!=randnum:
        guess= guess -1 
        
    
    
    if userGuess==randnum:
        print("you guessed it right!")
    else:    
        if userGuess>randnum:
        
            print("hint: opps! you should have entered a lower number")
        
        
#if userGuess<randnum:
        else:
            print("hint: ohh! you were supposed to enter a higher number")
        
        

        
    if guess == 0:
        #if guess ==1:
            #print("LAST CHANCE!")
        
        print("you ran out of guesses! better luck next time")
        break
    print(f"now you have {guess} number of guesses left, be careful!")
    
print("right number: ", randnum)
