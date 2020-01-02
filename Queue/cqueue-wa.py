class CQueue:
    def __init__(self, size):
        self.size = size
        self.qu = [None] * size
        self.startOfQueue = -1
        self.endOfQueue = -1
    
    def enque(self, value):
        if(self.isQueueFull()):
            print('Size overflow, cant insert')
            return
        if(self.startOfQueue == -1):
            self.startOfQueue = self.endOfQueue = 0
        else:
            self.endOfQueue = (self.endOfQueue + 1) % self.size 
        self.qu[self.endOfQueue] = value
        print('inserted value ' + str(value) + ' into the queue' )
    
    def deQueue(self):
        if(self.isQueueEmpty()):
            print('size full, reset queue')
            return
        print('dequeued value ' + str(self.qu[self.startOfQueue]) + ' from the queue' )
        if(self.startOfQueue == self.endOfQueue):
            self.startOfQueue = self.endOfQueue = -1
            return
        self.startOfQueue = (self.startOfQueue + 1) % self.size

    def isQueueFull(self):
        if(((self.endOfQueue + 1) % self.size) == self.startOfQueue):
            return True
        return False

    def isQueueEmpty(self):
        if (self.startOfQueue == -1):
            return True

    def print(self):
        if(self.isQueueEmpty()):
            print('The queue is empty')
            return
        print('\ncurrent Queue')
        print('####################')
        if(self.startOfQueue <= self.endOfQueue):
            for i in range(self.startOfQueue, self.endOfQueue + 1):
                print(self.qu[i])
        else:
            for i in range(self.startOfQueue, self.size):
                print(self.qu[i])
            for i in range(0, self.endOfQueue + 1):
                print(self.qu[i])
        print('####################\n')
    
    def reset(self):
        self.__init__(self.size)

if __name__ == "__main__":
    q = CQueue(3)
    q.enque(10)
    q.enque(20)
    q.enque(30)
    q.deQueue()
    q.enque(50)
    q.deQueue()
    q.deQueue()
    q.print()
    q.enque(60)
    q.print()
    q.enque(70)
    q.print()