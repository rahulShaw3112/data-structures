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
        self.insertNode(self.root, newNode)
        print('Inserted ' + str(newNode.value) + ' into the tree.')

    def insertNode(self, root, newNode):
        if(root.value > newNode.value):
            if(root.left is None):
                root.left = newNode
                return
            else:
                self.insertNode(root.left, newNode)
        else:
            if(root.right is None):
                root.right = newNode
                return
            else:
                self.insertNode(root.right, newNode)

    def delete(self, value):
        if(self.root is None):
            print('The tree is empty')
            return
        else:
            self.root = self.deleteNode(self.root, value)
    
    def deleteNode(self, root, value):
        if(root.value == value):
            if(root.left is None and root.right is None):
                root = None
            elif(not root.left):
                root = root.right
            elif(not root.right):
                root = root.left
            else:
                succ = self.findMin(root.right)
                root.value = succ.value
                root.right = self.deleteNode(root.right, succ.value)
        else:
            if(root.value > value):
                root.left = self.deleteNode(root.left, value)
            else:
                root.right = self.deleteNode(root.right, value)
        return root

    def findMin(self, root):
        if(root.left):
            return self.findMin(root.left)
        else:
            return root
            
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
    bt.insert(8)
    bt.insert(3)
    bt.insert(10)
    bt.insert(1)
    bt.insert(6)
    bt.insert(14)
    bt.insert(4)
    bt.insert(7)
    bt.insert(13)
    bt.delete(8)
    bt.printTree()
    # print('\nInorder: ')
    # bt.printInorder(bt.root)
    # print('\npre order: ')
    # bt.printPreorder(bt.root)
    # print('\npost order: ')
    # bt.printPostorder(bt.root)