# This code is a Dice Rollng Game  deigned to allow the user to roll 2 dice for a set amount of turns
# The game will add the value each die and whoever has the hghest amount of points at the end wins. 
# A count will be kept of the number of times each player won, the user will also choose the number of faces for
# the die, and a bonus round will be played in the event that the number of games won is a tie. The 
# bonus round will continue until a winner is declared. 

#Random is used to simulate rolling die and randomly receiving numbers
import random

#create a function to determine the face (number of sides) on the dice
def numSides(faces):
    return random.randint(1, faces), random.randint(1, faces)


# Function(s) to simulate rolling the dice for each player
def play_turn1(player1, faces):
    die1, die2 = numSides(faces)
    total = die1 + die2
    print(f"{player1} rolled: {die1} and {die2} \nTotal: ")
    return total

    
def play_turn2(player2, faces):
    die1, die2 = numSides(faces)
    total = die1 + die2
    print(f"{player2} rolled: {die1} and {die2} \nTotal: ")
    return total
    
#main method and statment to welcome the players to the game
def main():
    print("Welcome to the Dice Rolling Game.")

    # Variable to store the players name
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")

    #varaible to allow the player to determine how many faces (sides) die to use
    faces = int(input("Enter the number of faces on the dice: "))

    #variable to determine how many times the players will roll the dice (the number of round in the game)
    turns = int(input("Enter the number of turns: "))

    #variable(s) used to keeping track of the games played
    count = 1

   #variable(s) used to keeping track of the number of rounds won
    pw1=0
    pw2=0

    # Created a while loop to enusre that asl long as the the variable count is less than or equal to the 
    # number of turns (turns), the code inside the loop will keep running. Each time the loop runs, it 
    # simulates one round of the game where both players roll their dice
    while count <= turns:
        print(f"\nRound {count} ")
        pscore1=(play_turn1(player1, faces))
        print(pscore1)
        pscore2=(play_turn2(player2, faces))
        print(pscore2)
        
        count+=1
    
    #used a If statement to determine if player1 has more wins that player2. IF so, print the players name
    #and and a statement that indicates player1 is the winner.
        if pscore1 > pscore2:
            print(f"{player1} wins this game!")
            pw1 += 1

        #use an elif statement to determine if player2 has more wins that player1. IF so, print the players name
        #and and a statement that indicates player2 is the winner.
        elif pscore1 < pscore2:
            print(f"{player2} wins this game!")
            pw2 += 1

        #use an else statement to determine if the game is a tie and print out, It's a tie!
        else:
            print("It's a tie!")

        
    #show final count and game winner or if the game is a tie and the introduction of a bonus roundl
    print("\nGame Over")
    if pw1 > pw2:
        print(f"{player1} is the winner, with {pw1} rounds won! ")
    elif pw2 > pw1:
        print(f"{player2} is the winner, with {pw2} rounds won! ")
    else:
        print("\nIt's a tie game!\nWe will play a bonus round until there is a winner!")

    #code to trigger bonus round IF the game is a tie
        while pw1 == pw2:
            print(f"\nBouns Round ")
            pscore1=(play_turn1(player1, faces))
            print(pscore1)
            pscore2=(play_turn2(player2, faces))
            print(pscore2)
            

    #IF player1 wins the bonus round.
            if pscore1 > pscore2:
                print(f"\nGAME OVER!!\n{player1} wins the game!")
                pw1 += 1

    #IF player2 winS the bonus round.
            elif pscore2 > pscore1:  
                print(f"\nGAME OVER!!\n{player2} wins the game!")
                pw2 += 1
        
main()
