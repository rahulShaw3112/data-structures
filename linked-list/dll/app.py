class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Dll():
    def __init__(self): 
        self.head = None
        self.len = 0
    
    def insert(self, value, index):
        if(index > self.len or index < 0):
            print('Not possible')
            return
        newNode = Node(value)
        #insert at first position
        if(index == 0):
            if(self.head):
                self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        #insert in betweeen
        else:
            temp = self.traverseTill(index)
            newNode.next = temp.next
            newNode.prev = temp
            if(not (index == self.len)):
                temp.next.prev = newNode
            temp.next = newNode
        self.len += 1
        print('node inserted with value '+ str(newNode.value) + ' at index ' + str(index))
    
    def delete(self, index):
        if(index >= self.len or index < 0 or not self.head):
            print('Not possible')
            return
        temp = self.head
        #for first node
        if(index == 0):
            print('deleted node with value ' + str(self.head.value) + ' at index ' + str(index))
            if(not self.len == 1):
                self.head.next.prev = None
            self.head = self.head.next
        else:
            #for in between
            temp = self.traverseTill(index)
            print('deleted node with value ' + str(temp.next.value) + ' at index ' + str(index))
            temp.next.next.prev = temp
            temp.next = temp.next.next
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
        print('length: ', self.len)
        print('####################\n')

    def reverse(self):
        temp = self.head
        print('\ncurrent linked list in reverse')
        print('################################')
        if(temp):
            while temp.next is not None:
                temp = temp.next
        else:
            print('\nhead: none',end='')
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.prev
        print('\nlength: ', self.len)
        print('################################\n')
        
if __name__=='__main__': 
    ll = Dll()
    ll.insert(10,0)
    ll.insert(20,1)
    ll.insert(30,2)
    ll.insert(40,3)
    ll.delete(2)
    ll.delete(1)
    ll.delete(2)
    ll.print()
    ll.reverse()