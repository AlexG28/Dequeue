class Dequeue():
    def __init__(self):
        self.queue = []
        self.max = []
        self.min = []

    # functions to include:
    # append
    # appendleft
    # clear
    # copy
    # count
    # index
    # insert
    # pop
    # popleft
    # remove (value)
    # reverse
    # rotate
    # maxlen

    def append(self, val):
        self.queue.append(val)

    def appendLeft(self, val):
        self.queue.insert(0, val)

    def print(self):
        print(*self.queue)


def main():
    dequeue = Dequeue()
    
    while True:
        text = input()

        if text == 'stop':
            break
        
        text = text.split()


        if text[0] == 'append':
            dequeue.append(text[1])
        elif text[0] == 'appendLeft':
            dequeue.appendLeft(text[1])
        elif text[0] == 'print':
            dequeue.print()


if __name__ == '__main__':
    main()