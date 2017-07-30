from LinkedList import LinkedList

def count(self):
	ptr = self.head
	count = 0
	
	while ptr != None:
		count += 1
		ptr = ptr.next
		
	return count

def odd_check(self): 
	return self.r_count(self.root)
	
def r_count(self, ptr):
	if ptr == None:
		return 0
	
	if ptr.item % 2 == 1:
		return self.r_count(ptr.left) + self.r_count(ptr.right)
		

def main(): 			
	lst = LinkedList()
	lst.add(1)
	lst.add(2)
	lst.add(3)
	lst.add(66)
	print('The amount of items in the list are: ' + str(count(lst)))
	print(odd_check(lst))
	
if __name__ == "__main__":
   main()
