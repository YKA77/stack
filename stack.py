class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        print(self.items.pop())

    def show(self):
        print(self.items)

    def isEmpty(self):
        if len(self.items) < 1:
            print("stack is empty")
        else:
            print("stack is not empty")

    def size(self):
        print("stack is", len(self.items), "elements long")

    def peek(self):
        print(self.items[-1])

myStack = Stack()

myStack.push('a')
myStack.push('b')
myStack.push('c')
myStack.push('d')

myStack.show()
myStack.isEmpty()

myStack.pop()
myStack.show()

myStack.size()
myStack.peek()

