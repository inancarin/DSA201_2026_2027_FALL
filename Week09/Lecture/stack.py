class Stack:
    def __init__(self):
        self.stack = [] # initially empty list
    
    def push(self, elem):
        self.stack.append(elem)
    
    def isEmpty(self):
        """
        if len(self.stack) == 0:
            return True
        else:
            return False
        """
        return len(self.stack) == 0
    
    def pop(self):
        #if len(self.stack) == 0:
        if self.isEmpty():
            return None
        return self.stack.pop()
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None

    def printStack(self):
        print(self.stack)