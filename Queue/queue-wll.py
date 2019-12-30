class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def enQueue(self, value):
        print('Pushed value ' + str(value) + ' into the queue.')
        newNode = Node(value)
        if(not self.head):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def deQueue(self):
        if(not self.head):
            print('The quque is empty')
            return
        print('dequeued value ' + str(self.head.value) + ' from the queue')
        self.head = self.head.next
        if(not self.head):
            self.head = None
            self.tail = None

    def peek(self):
        if(self.head):
            print('The value on top is ' + str(self.head.value))
        else:
            print('the queue is empty')
    
    def print(self):
        temp = self.head
        print('\ncurrent Queue')
        print('####################')
        while temp is not None:
            print(temp.value)
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

if __name__ == "__main__":
    qu = Queue()
    qu.enQueue(10)
    qu.enQueue(20)
    qu.enQueue(30)
    qu.enQueue(40)
    qu.enQueue(50)
    qu.deQueue()
    qu.peek()
    qu.deQueue()
    qu.peek()
    qu.deQueue()
    qu.peek()
    qu.deQueue()
    qu.peek()
    qu.deQueue()
    qu.peek()
    qu.deQueue()
    qu.peek()
