class Node:
	def __init__(self, item, next):
		self.item = item
		self.next = next
	
class LinkedList:
	def __init__(self):
		self.head = None
	
	def add(self, item):
		self.head = Node(item, self.head)
	
	def remove(self):
		if self.is_empty():
			return None
		else:
			item = self.head.item
			self.head = self.head.next
		return item
	
	def is_empty(self):
		return self.head == None
		
	def remove_last(self, ptr):
		if self.is_empty():
			return
		else:
			ptr = self.head
			while ptr != None:
				ptr = ptr.next
				
			remove(ptr)
			
	def printOut(self,ptr):
		ptr = self.head
		while ptr != None:
			print(item)
			ptr = ptr.next
		
	
			
	