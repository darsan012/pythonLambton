# Darshan Gautam
# c0916788
# 8 Feb 2024

# declearation of the node class to store data, next and previous value
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def removeFirst(self):
        if not self.isEmpty():
            if self.size == 1:
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

    def add(self, element, index):
        if index < 0 or index > self.size:
            print("Please enter a valid index")
        elif index == 0:
            self.addFirst(element)
        elif index == self.size:
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
            print("Please enter a valid index")
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

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next
        return result

    def __eq__(self, other):
        if not isinstance(other, DoublyLinkedList):
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
        result = DoublyLinkedList()
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

class Stack:
    def __init__(self):
        self.__stk = DoublyLinkedList()
        self.__size = 0

    def isEmpty(self):
        return self.__size == 0

    def push(self, element):
        self.__stk.addLast(element)
        self.__size += 1

    def pop(self):
        if not self.isEmpty():
            self.__stk.removeLast()
            self.__size -= 1

    def peek(self):
        if not self.isEmpty():
            return self.__stk.tail.data
        return None

    def __str__(self):
        top_element = self.peek()
        return f"__size: {self.__size}\nTop: {top_element}"

    def __len__(self):
        return self.__size

    def __add__(self, other):
        result = Stack()
        result.__stk = self.__stk + other.__stk
        result.__size = len(result.__stk)
        return result

def is_palindrome(word):
    stack = Stack()

    # Pushing the first half of the word onto the stack
    for i in range(len(word) // 2):
        stack.push(word[i])

    # Skipping the middle character for odd length words
    start_index = len(word) // 2 if len(word) % 2 == 0 else len(word) // 2 + 1

    # Comparing the second half of the word with the stack
    for i in range(start_index, len(word)):
        if word[i] != stack.peek():
            return False
        stack.pop()

    return True

userInput = input("Please enter a word: ")
if is_palindrome(userInput):
    print(f"{userInput} is a palindrome!")
else:
    print(f"{userInput} is not a palindrome!")
