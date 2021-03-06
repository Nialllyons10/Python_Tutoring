from Stack import Stack

class Queue:
	def __init__(self):
		self.enq_stack = Stack()
		self.deq_stack = Stack()
	
	def isempty(self):
		return self.enq_stack.isempty() and self.deq_stack.isempty()
	
	def enqueue(self, item):
		self.enq_stack.push(item)
	
	def dequeue(self):
		if not self.deq_stack.isempty():
			return self.deq_stack.pop()
	
		# Reverse the enqueue stack onto the dequeue stack
		while not self.enq_stack.isempty():
			self.deq_stack.push(self.enq_stack.pop())
			
		return self.deq_stack.pop()

def main():
	q = Queue()
	
	for letter in "abcdef":
		q.enqueue(letter)

	x = q.dequeue()
	y = q.dequeue()
	
	q.enqueue(x)
	
	while not q.isempty():
		print(q.dequeue())
	
	
	
if __name__ == "__main__":
   main()