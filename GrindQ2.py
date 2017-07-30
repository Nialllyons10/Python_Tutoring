'''Write a program that lets the user play the game of Rock, Paper, Scissors against the computer. The program should work as follows: 

1. When the program begins, a random number in the range of 1 through 3 is generated. If the number is 1, then the computer has chosen rock. 
   If the number is 2, then the computer has chosen paper. If the number is 3, then the computer has chosen scissors. 
   (Don’t display the computer’s choice yet.)

2. The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.

3. The computer’s choice is displayed. 

4. A winner is selected according to the following rules: • If one player chooses rock and the other player chooses scissors, 
   then rock wins. (The rock smashes the scissors.) • If one player chooses scissors and the other player chooses paper, 
   then scissors wins. (Scissors cuts paper.) • If one player chooses paper and the other player chooses rock, then paper wins. (
   Paper wraps rock.) • If both players make the same choice, the game must be played again to determine the winner. '''
   
import random 
 
# Global constants 
COMPUTER_WINS = 1 
PLAYER_WINS = 2 
TIE = 0 
INVALID = 3 
ROCK = 1 
PAPER = 2 
SCISSORS = 3 
	
def main(): 
	result = TIE 
 
	while result == TIE:
		# Get computer number         
		computer = random.randint(1, 3) 
 
        # Get player number         
		player = int(input('Enter 1 for rock, 2 for paper, 3 for scissors: ')) 
 
		print ('Computer chose', choiceString(computer))         
		print ('You chose', choiceString(player))                  
		result = rockPaperScissors(computer, player)                  
		
		if result == TIE:             
			print('You made the same choice as the computer. Starting over') 
 
		if (result == COMPUTER_WINS):         
			print ('The computer wins the game')     
		elif result == PLAYER_WINS:         
			print ('You win the game')     
		else:         
			print ('You made an invalid choice. No winner') 
 
		# The rockPaperScissors function receives numbers representing the 
		# computer and player's choices. 
		# It returns 0 if there is a tie, 1 if the computer won, 2 if the  
		# player won, or 3 if the player made an invalid choice. 
		
def rockPaperScissors(computer, player): 
	if(computer == player):         
		return TIE 
		
	if computer == ROCK:          
		if player == PAPER:              
			return PLAYER_WINS         
		elif player == SCISSORS:              
			return COMPUTER_WINS         
		else: 
			return INVALID     
	elif computer == PAPER:          
		if player == ROCK:              
			return COMPUTER_WINS         
		elif player == SCISSORS:              
			return PLAYER_WINS         
		else:             
			return INVALID
	else: #computer chose scissors         
		if player == ROCK:              
			return PLAYER_WINS         
		elif player == PAPER:              
			return COMPUTER_WINS         
		else:             
			return INVALID 

# The choiceString function displays a choice in string format 
def choiceString(choice):     
	if choice == ROCK:         
		return 'rock'     
	elif choice == PAPER:         
		return 'paper'     
	elif choice == SCISSORS:         
		return 'scissors'     
	else:         
		return 'something went wrong' 
		
# Call the main function. 
main() 


