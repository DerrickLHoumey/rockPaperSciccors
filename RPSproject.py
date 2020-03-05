'''
Created on Feb 1, 2020

@author: ITAUser
'''

#set variable keepPlaying to true
keepPlaying = True

#While keepPlaying is true:
while keepPlaying == True:
    
    #print statement welcoming players to the game
    print("Welcome to Rock Paper Scissors!")
    #print statement stating the rules (best 2 out of 3 Press 'q' to quit)
    print("The first to win 2 out of 3 wins, Press 'q' if you want to quit")
    #make a key that assigns a number to each choice for the computer
    key = ["rock","paper","scissors"]
    #(rock is 1, scissors is 2, paper is 3)

    #import the random function - the computer makes its choice randomly from this function
    import random;    
    #set computer's score to 0
    computerScore = 0
    #set player's score to 0
    playerScore = 0
    #while player's score is less than 2 and computer's score is less than 2: - this means that the game is still on
    while((playerScore < 2) or (computerScore < 2)):
        #computer's choice = random number between 1 and 3 (random function gets used here)
        computerChoice = key[random.randint(0,2)]
        #player's choice = input(as player to select Rock, Paper, or Scissors)
        #start checking user options
        #userChoice = useChoice.lower()
        playerChoice = input("Choose a Move")
        playerChoice = playerChoice.lower()
        #if player inputs 'q': --player wants to end the game
        if playerChoice == "q" or "Q":
            # set keepPlaying to False
        # stop the loop
            keepPlaying = False
            break
        
        #else if(player inputs rock and computer chooses rock) or 
        #(plater inputs paper and computer chooses paper) or 
        #(player inputs scissors and computer chooses paper) or
        elif playerChoice == computerChoice:
            #print out DRAW
            #print out player's score and computer's score
            print("It's a draw!")
            print("Your score is: " + playerScore)
            print("The computer's score is: " + computerScore)
            
    #else if(player inputs rock and computer scissors) or
    #(player inputs scissors and computer chooses paper) or
    #(plater inputs paper and computer inputs rock)
        elif (playerChoice == "rock" and computerChoice == "scissors") or (playerChoice == "scissors" and computerChoice == "paper") or (playerChoice == "paper" and computerChoice == "rock"):
    #   add one to the player;s score
    #   print our player's score and computer's score
            playerScore= playerScore + 1
            print("Your score is: " + playerScore)
            print("The computer's score is: " + computerScore)
    #else if(player inputs rock and computer paper) or
    #(player inputs scissors and computer chooses rock) or
    #(plater inputs paper and computer inputs scissors)
        elif (playerChoice == "rock" and computerChoice == "scissors") or (playerChoice == "scissors" and computerChoice == "paper") or (playerChoice == "paper" and computerChoice == "rock"):
    #   add one to the computer's score
    #   print our player's score and computer's score  
            computerScore= computerScore + 1
            print("Your score is: " + playerScore)
            print("The computer's score is: " + computerScore)
    #else:
    #   tell the user their input was not valid
        else:
            print("That input was not valid.")
    
    
    #print statement thanking the players for playing
    #if plater's score is 2:
    if(playerScore == 2):      
        #print statement letting player know they win
        print("Congratulations, You Win!")
    #if computer's score is 2
    if(playerScore == 2):      
    #   print statement letting player know the computer win
        print("OH NO, You Lose!")
    #print out plater's score and computer's score  