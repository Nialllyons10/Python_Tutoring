'''Write a program that asks the user to enter a number of seconds and works as follows: 

• There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60, the 
  program should display the number of minutes in that many seconds. 
  
• There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600, the 
  program should display the number of hours in that many seconds. 
  
• There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400, the program 
  should display the number of days in that many seconds. '''
 
def getDays():
	# Local variables 
	days = 0 
	hours = 0 
	minutes = 0 
	seconds = 0  
	dayRemainder = 0 
	hourRemainder = 0 
	minuteRemainder = 0 
	 
	# Get the number of seconds from the user. 
	seconds = int(input('Enter the number of seconds: ')) 
	 
	# Calculate the number of days. 
	if seconds >= 86400:     
		days = seconds // 86400     
		dayRemainder = seconds % 86400      

	# Calculate the hours.
	if seconds >= 3600:     
		hours = seconds // 3600     	
		hourRemainder = seconds % 3600          
	 
	 # Calculate the minutes. 
	if seconds >= 60:     
		minutes = seconds // 60     
		minuteRemainder = seconds % 60    

	# Display days, hours, minutes, seconds. 
	if minutes == 0:     
		print('The number of seconds is less than one minute.') 
	else:     
		print(seconds, 'seconds are equal to:')     
		print (minutes, 'full minute(s) and', minuteRemainder, 'seconds.')     
		
		if hours != 0:         
			print (hours, 'full hour(s) and', hourRemainder, 'seconds.')     
		
		if days != 0:         
			print (days, 'full day(s) and', hours, 'hours and dayRemainder ', seconds) 
	 
 
def main():
	print(getDays())
	
if __name__ == "__main__":
   main()