# creation of the node class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DblyLnkdLst:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def addFirst(self, element):
        node = Node(element)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def addLast(self, element):
        node = Node(element)
        if self.isEmpty():
            self.head = node 
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def removeFirst(self):
        if not self.isEmpty():
            if self.size == 1 :
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.size -= 1

    def removeLast(self):
        if not self.isEmpty():
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1

    def add(self,element ,index):
        if index < 0 or index > self.size:
            print("Please enter the valid index")
        elif index == 0:
            self.addFirst(element)
        elif index  == self.size:
            self.addLast(element)
        else:
            node = Node(element)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node
            self.size += 1
        
    def remove(self, index):
        if index < 0 or index >= self.size:
            print("Please enter the valid index")
        elif index == 0:
            self.removeFirst()
        elif index == self.size - 1:
            self.removeLast()
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1

    def display(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data)
            if current.next:
                result += " -> "
            current = current.next
        print(result)
        
    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next
        return result

    def __eq__(self, other):
        if not isinstance(other, DblyLnkdLst):
            return False
        current_self = self.head
        current_other = other.head
        while current_self and current_other:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return current_self is None and current_other is None

    def __add__(self, other):
        result = DblyLnkdLst()
        current_self = self.head
        current_other = other.head
        while current_self:
            result.addLast(current_self.data)
            current_self = current_self.next
        while current_other:
            result.addLast(current_other.data)
            current_other = current_other.next
        return result

    def __len__(self):
        return self.size
    

# dl1 = DblyLnkdLst()
# dl1.addFirst(10)

# print(dl1)

# dl1.addFirst(20)
# print(dl1)

# dl1.add(30, 1)
# print(dl1)

# dl1.add(50, 3)
# print(dl1)