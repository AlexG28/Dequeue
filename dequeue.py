class Dequeue():
    def __init__(self):
        self.queue = []
        self.max = []
        self.min = []

    # functions to include:
    # append [yes]
    # appendleft [yes]
    # clear [yes]
    # copy [????]
    # count [yes]
    # index
    # pop [yes with issues]
    # popleft [yes with issues]
    # remove (value)
    # get max [yes]
    # get min [yes]

    # known issues:
    # if you pop too much and then call min or max, its gonna break

    def appendMaxMin(self, val):
        if len(self.queue) == 0:
            self.max.append(val)
            self.min.append(val)
        else:
            if val >= self.max[-1]: 
                self.max.append(val)
            elif val <= self.min[-1]:
                self.min.append(val) 

    def popMaxMin(self, val):
        if val == self.max[-1]:
            self.max.pop()
        elif val == self.min[-1]:
            self.min.pop()

    def append(self, val):
        self.appendMaxMin(val)
        self.queue.append(val)

    def appendLeft(self, val):
        self.appendMaxMin(val)
        self.queue.insert(0, val)
    
    
    def pop(self):
        if len(self.queue) == 0:
            return 'empty queue'
        
        temp = self.queue.pop()
        self.popMaxMin(temp)
        return temp
        
    
    def popLeft(self):
        if len(self.queue) == 0:
            return 'empty queue'
        temp = self.queue.pop(0)
        self.popMaxMin(temp)
        return temp


    def print(self):
        if len(self.queue) == 0:
            print('empty queue')
        return self.queue
    
    def getMax(self):
        if len(self.queue) == 0:
            return 'empty queue'
        return self.max[-1]

    def getMin(self):
        if len(self.queue) == 0:
            return 'empty queue'
        return self.min[-1]

    def clear(self):
        self.min = []
        self.max = []
        self.queue = []

    def length(self):
        return len(self.queue)

    def index(self, val):
        if len(self.queue) == 0:
            return 'empty queue'
        for i in range(len(self.queue)):
            if val == self.queue[i]:
                return i
        return 'not in queue'

def main():
    dequeue = Dequeue()
    
    while True:
        text = input()

        if text == 'stop':
            break
        
        text = text.split()

        if text[0] == 'print':
            print(*dequeue.print())
        elif text[0] == 'max':
            print(dequeue.getMax())
        elif text[0] == 'min':
            print(dequeue.getMin())
        elif text[0] == 'pop':
            dequeue.pop()
        elif text[0] == 'popleft':
            dequeue.popLeft()
        
        else:    
            number = int(text[1])
            if text[0] == 'append':
                dequeue.append(number)
            elif text[0] == 'appendleft':
                dequeue.appendLeft(number)
            elif text[0] == 'index':
                print(dequeue.index(number))
            elif text[0] == 'print':
                dequeue.print()


if __name__ == '__main__':
    main()