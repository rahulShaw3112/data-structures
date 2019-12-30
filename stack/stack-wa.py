class Stack:
    def __init__(self, size):
        self.size = size
        self.st = [None] * size
        self.topOfStack = 0
    
    def push(self, value):
        if(self.topOfStack == self.size):
            print('Size overflow, cant insert')
            return
        self.st[self.topOfStack] = value
        self.topOfStack += 1
        print('inserted value ' + str(value) + ' into the stack' )
    
    def pop(self):
        if(self.topOfStack == 0):
            print('stack is empty')
            return
        self.topOfStack -= 1
        print('poped value ' + str(self.st[self.topOfStack]) + ' from the stack' )

    def print(self):
        if(self.topOfStack == 0):
            print('The stack is empty')
            return
        print('\ncurrent Stack')
        print('####################')
        for i in range(self.topOfStack - 1, -1, -1):
            print(self.st[i])
        print('####################\n')
    
    def reset(self):
        self.__init__(self.size)

if __name__ == "__main__":
    s = Stack(3)
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.print()
    s.pop()
    s.print()
    s.pop()
    s.print()
    s.pop()
    s.print()
    s.pop()
    s.print()