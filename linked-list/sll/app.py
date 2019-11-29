class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Sll():
    def __init__(self): 
        self.head = None
        self.len = 0
    
    def insert(self, value, index):
        if(index > self.len):
            print('Not possible')
            return
        newNode = Node(value)
        #insert at first position
        if(index == 0):
            newNode.next = self.head
            self.head = newNode
        #insert in betweeen
        else:
            temp = self.traverse(index)
            newNode.next = temp.next
            temp.next = newNode
        self.len += 1
        print('node inserted with value '+ str(newNode.value) + ' at index ' + str(index))
    
    def delete(self, index):
        if(index >= self.len):
            print('Not possible')
            return
        temp = self.head
        #for first node
        if(index == 0):
            print('deleted node: ' + str(self.head.value))
            self.head = self.head.next
        else:
            #for in between
            temp = self.traverse(index)
            print('deleted node with value ' + str(temp.next.value) + ' at index ' + str(index))
            temp.next = temp.next.next
        self.len -= 1
    
    def traverse(self, index):
        i = 0
        temp = self.head
        while(i < index - 1):
            i += 1
            temp = temp.next
        return temp

    def search(self, value):
        i = 0
        temp = self.head
        while (temp):
            if(temp.value == value):
                print('Found ' + str(value) + ' at index ' + str(i))
                return True
            i += 1
            temp = temp.next
        print(str(value) + ' not found')
        return False

    def print(self):
        temp = self.head
        print('\ncurrent linked list')
        print('####################')
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        if(self.head):
            print('\nhead: ' + str(self.head.value))
        else:
            print('\nhead: none')
        print('length: ', self.len)
        print('####################\n')

if __name__=='__main__': 
    ll = Sll()
    ll.insert(10,0)
    ll.insert(20,0)
    ll.insert(30,2)
    ll.insert(40,0)
    ll.insert(50,0)
    ll.insert(60,0)
    ll.insert(70,0)
    ll.insert(80,0)
    ll.insert(90,1)
    ll.insert(100,2)
    ll.insert(120,3)
    ll.delete(1)
    ll.search(155)
    ll.print()