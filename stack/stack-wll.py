class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def push(self, value):
        print('Pushed value ' + str(value) + ' into the stack.')
        newNode = Node(value)
        if(not self.head):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def pop(self):
        if(not self.head):
            print('The stack is empty')
            return
        print('poped value ' + str(self.head.value) + ' from the stack')
        self.head = self.head.next
        if(not self.head):
            self.tail = None

    def peek(self):
        if(self.head):
            print('The value on top is ' + str(self.head.value))
        else:
            print('the stack is empty')

    def print(self):
        temp = self.head
        print('\ncurrent Stack')
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

if __name__=='__main__': 
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    st.push(40)
    st.push(50)
    st.peek()
    st.pop()
    st.peek()
    # st.pop()
    # st.print()
    # st.pop()
    # st.print()
    # st.pop()
    # st.print()
    # st.pop()
    # st.print()
    # st.pop()
    # st.print()