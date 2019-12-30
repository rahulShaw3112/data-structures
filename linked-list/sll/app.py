class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Sll():
    def __init__(self): 
        self.head = None
        self.tail = None
        self.len = 0
    
    def insert(self, value, index):
        if(index > self.len or index < 0):
            print('Not possible')
            return
        newNode = Node(value)
        # insert with no node inserted.
        if(not self.head):
            self.head = newNode
            self.tail = newNode
            
        # insert at beginning of list.
        elif(index == 0): 
            newNode.next = self.head
            self.head = newNode

        # insert at end of list.
        elif(index == self.len):
            self.tail.next = newNode
            self.tail = newNode

        #insert in between
        else:
            temp = self.traverseTill(index)
            newNode.next = temp.next
            temp.next = newNode 
        self.len += 1
        print('node inserted with value '+ str(newNode.value) + ' at index ' + str(index))
    
    def delete(self, index):
        if(index >= self.len or index < 0):
            print('Not possible')
            return
        temp = self.head

        # if only node left
        if(self.len == 1):
            self.head = None
            self.tail = None
        
        #for first node
        elif(index == 0):
            print('deleted node with value ' + str(self.head.value) + ' at index ' + str(index))
            self.head = self.head.next
            
        #for in between and last
        else:
            temp = self.traverseTill(index)
            print('deleted node with value ' + str(temp.next.value) + ' at index ' + str(index))
            temp.next = temp.next.next
            # if last element
            if(index == (self.len - 1)):
                self.tail = temp

        self.len -= 1 
        
    def traverseTill(self, index):
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
        if(self.tail):
            print('tail: ' + str(self.tail.value))
        else:
            print('tail: none')
        print('length: ', self.len)
        print('####################\n')

if __name__=='__main__': 
    ll = Sll()
    ll.insert(10,0)
    ll.insert(20,1)
    ll.insert(30,2)
    ll.insert(40,3)
    ll.insert(50,4)
    ll.print()
    ll.delete(0)
    ll.print()
    ll.delete(3)
    ll.print()
    ll.delete(1)
    ll.print()
    ll.delete(1)
    ll.print()
    ll.delete(0)
    ll.print()