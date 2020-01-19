import queue

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if (not self.root):
            print('Inserted ' + str(newNode.value) + ' into the tree.')
            self.root = newNode
            return
        qu = queue.Queue()
        qu.put(self.root)
        while(not qu.empty()):
            temp = qu.get()
            if (not temp.left):
                temp.left = newNode
                print('Inserted ' + str(newNode.value) + ' into the tree.')
                break
            elif (not temp.right):
                temp.right = newNode
                print('Inserted ' + str(newNode.value) + ' into the tree.')
                break
            else:
                qu.put(temp.left)
                qu.put(temp.right)

    def delete(self, value):
        qu = queue.Queue()
        qu.put(self.root)
        searchedValue = None
        lastValue = None
        while(not qu.empty()):
            temp = qu.get()
            if(temp.value == value):
                searchedValue = temp
            if(temp.left):
                qu.put(temp.left)
            if(temp.right):
                qu.put(temp.right)
            if(qu._qsize() == 1):
                lastValue = qu.get()
        
        if(searchedValue):
            temp = lastValue.value
            print('Deleted value ' + str(searchedValue.value) + ' from tree.')
            self.deleteLastNode(lastValue.value)
            searchedValue.value = temp
    
    def deleteLastNode(self, value):
        qu = queue.Queue()
        qu.put(self.root)
        while(not qu.empty()):
            temp = qu.get()
            if(temp.left.value == value):
                temp.left = None
                break
            if(temp.right.value == value):
                temp.right = None
                break
            if(temp.left):
                qu.put(temp.left)
            if(temp.right):
                qu.put(temp.right)
            
        
            
    def printTree(self): 
        i = 0
        j = 1
        qu = queue.Queue()
        qu.put(self.root)
        print('\n#################################')
        print('current tree')
        print('#################################')
        while(not qu.empty()):
            temp = qu.get()
            print(temp.value, end=' ')
            if (i % j == 0):
                j *= 2
                i = 0
                print('')
            if(temp.left):
                qu.put(temp.left)
            if(temp.right):
                qu.put(temp.right)
            i += 1
        print('\n#################################')
        print('preorder: ', end= ' ')
        self.printPreorder(self.root)
        print('')
        print('inorder: ', end= ' ')
        self.printInorder(self.root)
        print('')
        print('postorder: ', end= ' ')
        self.printPostorder(self.root)
        print('')
        print('\n#################################')

    
    def printPreorder(self, root):
        if(not root):
            return
        print(root.value, end=' ')
        self.printPreorder(root.left)
        self.printPreorder(root.right)
    
    def printInorder(self, root):
        if(not root):
            return
        self.printInorder(root.left)
        print(root.value, end=' ')
        self.printInorder(root.right)
    
    def printPostorder(self, root):
        if(not root):
            return
        self.printPostorder(root.left)
        self.printPostorder(root.right)
        print(root.value, end=' ')
        

if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(20)
    bt.insert(30)
    bt.insert(40)
    bt.insert(50)
    bt.insert(60)
    bt.insert(70)
    bt.printTree()
    bt.delete(70)
    bt.printTree()