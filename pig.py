def main():
	words = str(input("Input Sentence:")).split()
	print(words)
	
	for word in words:
		print(word[1:] + word[0] + "ay")
	

main()