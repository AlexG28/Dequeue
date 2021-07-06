class Dequeue():
    def __init__(self):
        self.queue = []
        self.max = []
        self.min = []

    # functions to include:
    # append [yes]
    # appendleft [yes]
    # clear [yes]
    # copy 
    # count [yes]
    # index
    # insert
    # pop
    # popleft
    # remove (value)
    # reverse
    # rotate
    # maxlen
    # get max [yes]
    # get min [yes]

    def updateMaxMin(self, val):
        if len(self.queue) == 0:
            self.max.append(val)
            self.min.append(val)
        else:
            if val >= self.max[-1]: 
                self.max.append(val)
            elif val <= self.min[-1]:
                self.min.append(val) 

    def append(self, val):
        self.updateMaxMin(val)
        self.queue.append(val)

    def appendLeft(self, val):
        self.updateMaxMin(val)
        self.queue.insert(0, val)

    def print(self):
        print(*self.queue)
    
    def getMax(self):
        return self.max[-1]

    def getMin(self):
        return self.min[-1]

    def clear(self):
        self.min = []
        self.max = []
        self.queue = []

    def length(self):
        return len(self.queue)


def main():
    dequeue = Dequeue()
    
    while True:
        text = input()

        if text == 'stop':
            break
        
        text = text.split()

        if text[0] == 'print':
            dequeue.print()
        elif text[0] == 'max':
            print(dequeue.getMax())
        elif text[0] == 'min':
            print(dequeue.getMin())
        else:    
            number = int(text[1])

            if text[0] == 'append':
                dequeue.append(number)
            elif text[0] == 'appendLeft':
                dequeue.appendLeft(number)
            elif text[0] == 'print':
                dequeue.print()


if __name__ == '__main__':
    main()