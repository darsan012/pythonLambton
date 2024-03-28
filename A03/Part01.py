# Implementing the binary tree
class Node:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree():
  def __init__(self):
    self.root = None

  #complexity of insert worst case is O(n)
  #amortized/avg run-time is O(lgN)
  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
      return
    
    precursor = None
    cursor = self.root
    while cursor is not None:
      precursor = cursor
      if cursor.data > data:
        cursor = cursor.left
      else:
        cursor = cursor.right

    if precursor.data > data:
      precursor.left = Node(data)
    else:
      precursor.right = Node(data)

  #Big-O Complexity: O(n)
  def print_preorder(self,node):
    print(node.data)
    if node.left is not None:
      self.print_preorder(node.left)
    if node.right is not None:
      self.print_preorder(node.right)

  #Big-O Complexity: O(n)
  def print_postorder(self,node):
    if node.left is not None:
      self.print_postorder(node.left)
    if node.right is not None:
     self.print_postorder(node.right)
    print(node.data)

  #Big-O Complexity: O(n)
  def print_inorder(self, node):
    if node.left is not None:
      self.print_postorder(node.left)
    print(node.data)
    if node.right is not None:
     self.print_postorder(node.right)
  
  # time complexity is O(h) where h is the height of the tree
  # For binary balanced tree it is O(lon(n))
  # for binary unbalanced tree it is O(n) where n is the number of elements
  def search(self, data):
    num = 1
    cursor = self.root

    while cursor is not None:
      if cursor.data == data:
        return num
      if cursor.data > data:
        cursor = cursor.left
      else:
        cursor = cursor.right
      num += 1

    return 0
  
# initialize sequenceA
sequenceADatas = [1,5,4,6,7,2,3]
sequenceA = BinarySearchTree() # creating the sequence tree
# inserting the values through loop to the tree
for i in sequenceADatas:
    sequenceA.insert(i)
print("Inserted Sequence A: ", sequenceADatas)

# initializing sequence B datas
sequenceBDatas =[150,125,175,166,163,123,108,116,117,184,165,137,141,111,138,122,
109,194,143,178,173,139,126,170,190,140,188,120,195,113,104,193,181,185,198,103,182,
136,115,191,144,145,155,153,151,112,129,199,135,146,157,176,159,196,121,105,131,154,
107,110,158,187,134,132,179,133,102,172,106,177,171,156,168,161,149,124,189,167,174,
147,148,197,160,130,164,152,142,162,118,186,169,127,114,192,180,101,119,128,100]

sequenceB = BinarySearchTree()
# inserting the values through loop to the tree
for i in sequenceBDatas:
  sequenceB.insert(i)
print("\nInserted Sequence B:", sequenceBDatas)

# searching through sequenceA
print("\nSearching 1,4,2 in Sequence A")
print("Returns 0 if there is no value else returns the number of nodes visisted")

for i in [1,4,2,233]:
  print(sequenceA.search(i))

print("\nSearching 42, 142, 102, 190  in Sequence B")
print("Returns 0 if there is no value else returns the number of nodes visisted")

#searching through sequenceB
for i in [42, 142, 102, 190 ]:
  print(sequenceB.search(i))


# traversing through sequence A
print("\n Traversing throught sequence A")
print("Pre-order Traversal")
sequenceA.print_preorder(sequenceA.root)
print("\nPost-order Traversal")
sequenceA.print_postorder(sequenceA.root)
print("\nIn-order Traversal")
sequenceA.print_inorder(sequenceA.root)

# traversing through sequence B
print("\n Traversing throught sequence B")
print("Pre-order Traversal")
sequenceB.print_preorder(sequenceB.root)
print("\nPost-order Traversal")
sequenceB.print_postorder(sequenceB.root)
print("\nIn-order Traversal")
sequenceB.print_inorder(sequenceB.root)

