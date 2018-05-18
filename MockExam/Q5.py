def main(): 

	my_string = input('Enter a string: ') 

	new_string = convert(my_string)
	print(new_string)
	
	
	
def convert(string):	
	i = 0
	result = ""
	for c in string:
		if c.isupper() and i > 0:
			result = result +  " "
			result = result + c.lower()
		else:
			result = result + c
		i = i + 1

	print(result)

main()
