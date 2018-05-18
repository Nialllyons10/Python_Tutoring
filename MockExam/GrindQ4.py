'''Write a program with a function that accepts a string as an a
argument and returns the number of vowels that the string contains. The application should have 
another function that accepts a string as an argument and returns the number of consonants that the 
string contains. The application should let the user enter a string and should display the number of 
vowels and the number of consonants it contains. '''


def main():     
	# Local variables     
	vowels = 0     
	consonants = 0 
 
    # Get the string as input from the user.     
	user_string = input('Enter a string: ') 
 
    # Call the vowel_counter function, storing the result.     
	vowels = vowel_counter(user_string)          
	
	# Call the consonant_counter function, storing the result.     
	consonants = consonant_counter(user_string) 
 
	uni = unique_counter(user_string)
    # Display the results.     
	print('The string you entered includes', vowels, 'vowels and', consonants, 'consonants.')
	print('Uniques is: ',uni)
 
# The vowel_counter method receives a string and # returns the number of vowels in the string. 
def vowel_counter(string):     
	# Set up local variables     
	count = 0     
	vowels = 'aeiou' 
 
    # For each character, determine if it is a vowel.     
	for x in string:         
		if vowels.find(x) >= 0:  #find determines whether or not the letter occurs in the vowels string. If not found it will be -1 so thats why we need >= 0           
			count = count + 1 
 
    # Return the number of vowels in the string.     
	return count          
	
# The consonant_counter method receives a string and returns the number of consonants in the string. 
def consonant_counter(string):     
	# Set up local variables     
	count = 0     
	consonants = 'bcdfghjklmnpqrstvwxyz' 
 
    # For each character, determine if it is a consonant.     
	for x in string:         
		if consonants.find(x) >= 0:             
			count = count + 1 
 
    # Return the number of consonants in the string.     
	return count 

def unique_counter(string): 
	unique = []
	for char in string[::]:
		if char not in unique:
			unique.append(char)
			
	count = len(unique)		
	return count
 
# Call the main function. 
main() 


