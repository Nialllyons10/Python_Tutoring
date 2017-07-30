def example():
	values = []

	while True:
		x = int(input('Enter your numbers, please press -1 when you want to stop!' '\n'))
		print()
		if x == -1:
			break
			
		values.append(x)

	print(str(values))
	
	print(min(values))
	print(max(values))
	print(sum(values))
	
def main():
	example()
	
if __name__ == "__main__":
   main()