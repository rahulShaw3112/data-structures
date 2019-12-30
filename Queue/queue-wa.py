class Queue:
    def __init__(self, size):
        self.size = size
        self.qu = [None] * size
        self.startOfQueue = 0
        self.endOfQueue = 0
    
    def enque(self, value):
        if(self.endOfQueue == self.size):
            print('Size overflow, cant insert')
            return
        self.qu[self.endOfQueue] = value
        self.endOfQueue += 1
        print('inserted value ' + str(value) + ' into the queue' )
    
    def deQueue(self):
        if(self.endOfQueue == self.startOfQueue):
            print('size full, reset queue')
            return
        print('dequeued value ' + str(self.qu[self.startOfQueue]) + ' from the queue' )
        self.startOfQueue += 1

    def print(self):
        if((self.endOfQueue - self.startOfQueue) == 0):
            print('The queue is empty')
            return
        print('\ncurrent Queue')
        print('####################')
        for i in range(self.startOfQueue, self.endOfQueue):
            print(self.qu[i])
        print('####################\n')
    
    def reset(self):
        self.__init__(self.size)

if __name__ == "__main__":
    q = Queue(3)
    q.enque(10)
    q.enque(20)
    q.enque(30)
    q.enque(40)
    q.deQueue()
    q.print()
    q.deQueue()
    q.print()
    q.deQueue()
    q.print()
    q.deQueue()
    q.print()

    q.reset()
    q.enque(90)
    q.print()