# implementation of part 02 question 01 solution
class Node:
    def __init__(self, name, type, size = 0):
        self.name = name
        self.type = type
        self.size = size
        self.childern = []

class FileExplorerTree:
    def __init__(self, node):
        self.root = node

    def insertFolder(self, insertLocation, node):
        insertLocation.childern.append(node)

    def insertFile(self, insertLocation, node):
        insertLocation.childern.append(node)

    def calculateFolder(self, node, size =0 ):
        
        for item in node.childern:
            size +=item.size
            self.calculateFolder(item,size)
        
        if node.type == "FOLDER":
            node.size = size
            
        
    def calculateTree(self, node, root):

        for item in node.childern:
            
            if item.type == "FOLDER":
                print("********")
                print("FOLDER:", item.name)
                self.calculateFolder(item,0)
            self.calculateTree(item, root)

        if node is root:
            s = 0
            for item in node.childern:
               s += item.size
            node.size = s

        print(node.name, node.size)
            

#Main
# Creation of the root folder
folder1 = Node("/usr/rt/courses/", "FOLDER", 0)
ft = FileExplorerTree(folder1) 

#  insertion on the root folder, folder 2 and 3 are inside folder 1
folder2 = Node("/cs016/", "FOLDER", 0)
ft.insertFolder(folder1,folder2)

folder3 = Node("/cs252/", "FOLDER", 0)
ft.insertFolder(folder1,folder3)

# insertion of folder 4 and 5 inside forlder 2
folder4 = Node("/homeworks/", "FOLDER", 1)
ft.insertFolder(folder2,folder4)

folder5 = Node("/programs/", "FOLDER", 1)
ft.insertFolder(folder2,folder5)

# file inside folder 2
file = Node("grades", "FILE", 8)
ft.insertFile(folder2,file)

# files inside folder 4 i.e homeworks
file2 = Node("hw1", "FILE", 3)
file3 = Node("hw2", "FILE", 2)
file4 = Node("hw3", "FILE", 4)
ft.insertFile(folder4,file2)
ft.insertFile(folder4,file3)
ft.insertFile(folder4,file4)

# files inside folder 5 i.e programs
file5 = Node("pr1", "FILE", 57)
file6 = Node("pr2", "FILE", 97)
file7 = Node("pr3", "FILE", 74)
ft.insertFile(folder5,file5)
ft.insertFile(folder5,file6)
ft.insertFile(folder5,file7)

# insertion into folder 3 i.e 252
file8 = Node("grades", "FILE", 3)
ft.insertFile(folder3,file8)
folder6 = Node("/projects/", "FOLDER", 1)
ft.insertFolder(folder3,folder6)

# insertion into projects folder
folder7 = Node("/papers/", "FOLDER", 1)
folder8 = Node("/demos/", "FOLDER", 1)

ft.insertFolder(folder6,folder7)
ft.insertFolder(folder6,folder8)

#insertion int0 papers
file9 = Node("buylow", "FILE", 26)
file10 = Node("sellhigh", "FILE", 55)
ft.insertFile(folder7, file9)
ft.insertFile(folder7, file10)

# insertion into demos
file11 = Node("market", "FILE",4786)
ft.insertFile(folder8, file11)


ft.calculateTree(ft.root, ft.root)
print(ft.root.size)
