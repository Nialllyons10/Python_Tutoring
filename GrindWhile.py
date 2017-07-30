''' Example showing a boolean variable being used to control the loop. This is very common with while loops. In this case, the 
boolean variable is named Invalid. Invalid is initially 
set to be True. The code within the loop is executed until Invalid is set to False. This is a good method for validating 
any input that needs to be within a certain range.'''

def main():
	invalid = True
	while invalid:
		number = int(input("Please enter a number in the range 10 to 20: "))
		if number >= 10 and number <= 20:
			invalid = False
		else:
			print("Sorry number must be between 10 and 20")
			print("Please try again")
			
main()