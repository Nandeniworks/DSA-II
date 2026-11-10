
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def move(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def dequeue(self):
        self.move()
        self.stack2.pop()

    def front(self):
        self.move()
        return self.stack2[-1]


# main program
n = int(input())

q = MyQueue()

for i in range(n):
    query = input().split()

    if query[0] == '1':
        q.enqueue(int(query[1]))

    elif query[0] == '2':
        q.dequeue()

    elif query[0] == '3':
        print(q.front())
