class Node:
	def __init__(self, left, right, data, visited=None):
		self.left = left or None
		self.right = right or None
		self.data = data or None
		self.visited = visited

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def getData(self):
		return self.data

	def wasVisited(self):
		return self.visited 

	def getChildren(self):
		return [self.getLeft(), self.getRight()]

	def hasChildren(self):
		return len([self.getLeft(), self.getRight()])



def DFS(root, value):
	if root.getData() == value:
		return True
	else:
		left = DFS(root.getLeft(), value) if root.getLeft() is not None else False
		right = DFS(root.getRight(), value) if root.getRight() is not None else False
		return left or right

	return False


def getDFSPath(root, visitedlst):

	if root == None: 
		return

	if not root.wasVisited():
		root.visited = True
		visitedlst.append(root.getData())
		getDFSPath(root.getLeft(), visitedlst)
		getDFSPath(root.getRight(), visitedlst)
	return visitedlst


if __name__ == "__main__":
	seven = Node(None, None, 7)
	five = Node(None, None, 5)
	six = Node(None, None, 6)
	four = Node(None, None, 4)
	three = Node(five, seven, 3)
	two = Node(four, six, 2)
	one = Node(two, three, 1)

	print(DFS(one, 12))

	print(getDFSPath(one, []))
