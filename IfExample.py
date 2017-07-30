def main(): 
	print("\n")
	
	print("This will print the result of exampleOne:" "\n")
	print(exampleOne())
	
	print("\n")
	
	print("This will print the result of exampleTwo:" "\n")
	print(exampleTwo())


def exampleTwo():
	age = int(input("Enter your age: "))
	if age >= 13:
		print("You are old enough to have a paper round")
	else:
		print("You are too young to have a paper round")



def exampleOne(): 
	mark = int(input("What is your mark: "))
	if mark >= 50:
		print("Pass")
	elif mark <= 10:
		print("V Bad")
	else: 
		print("Fail")
		
main()