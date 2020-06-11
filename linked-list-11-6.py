#linked-list-11-6.py
#linked list to push data at front, at specific index, and at the end

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def append(self, new_data):
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node

	def insertAfter(self, prev_node, new_data):
		if prev_node is None:
			print('Not')
			return
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

if __name__ == '__main__':
	lists = LinkedList()
	lists.append(2)
	lists.push(9)
	lists.push(1)
	lists.insertAfter(lists.head.next, 4)
	lists.append(12)
	lists.printList()