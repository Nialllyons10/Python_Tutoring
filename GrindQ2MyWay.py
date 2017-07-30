#Rock Paper Scissors Game
import random

def main():

	#Ask user for their choice and check for invalid choice
	choice = input("Rock, Paper, or Scissors: ").upper()

	#Create Computers choice
	comp = random.randint(0,3)
	if comp == 0:
		comp = "Rock"
	elif comp == 1:
		comp = "Paper"
	else:
		comp = "Scissors"
	print("The computer picked " + comp + ".")

	#Compare users choice to computers choice to determine winner
	if choice == comp.upper():
		print("It's a tie!")
	elif choice == "ROCK":
		if comp == "Paper":
			print("The Computer Wins!")
		elif comp == "Scissors":
			print("You Win!!")
	elif choice == "PAPER":
		if comp == "Scissors":
			print("The Computer Wins!")
		elif comp == "Rock":
			print("You Win!!")
	else: #scissors
		if comp == "Rock":
			print("The Computer Win!")
		elif comp == "Paper":
			print("You Win!!")

main()