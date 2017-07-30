stack = []

def view(): 
	for x in range(len(stack)): 
		print(stack[x])
		
def push(): 
	item = input('Enter a number to put on the stack')
	stack.append(item)
	
def pop(): 
	item = stack.pop(-1)
	print('You popped: ' , item)
	
	
while True: 
	print('Enter a number, 1 to view, 2 to push or 3 to pop ')
	menu_choice = int(input('Enter a number: ')
	
	if menu_choice == 1 :
		view()
	elif menu_choice == 2 :
		push()
	elif menu_choice == 3 :
		pop()
		
	