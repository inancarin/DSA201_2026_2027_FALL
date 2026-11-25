from stack import Stack
from collections import deque

def checkExpression_v2(exp):
    stack = deque()

    openingBrackets = set("({[")
    d = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    for ch in exp: 
        #if ch in d.values():
        if ch in openingBrackets:
            stack.append(ch)
        elif ch in d: # check whether ch is a closing bracket
            if not stack:
                return False
            topElem = stack[-1]
            if d[ch] == topElem:
                removedElem = stack.pop()
            else:
                return False
        else:
            return False
    
    if not stack:
        return True
    return False

def checkExpression(exp):
    stack = Stack()

    openingBrackets = set("({[")
    d = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    for ch in exp: 
        #if ch in d.values():
        if ch in openingBrackets:
            stack.push(ch)
        elif ch in d: # check whether ch is a closing bracket
            if stack.isEmpty():
                return False
            topElem = stack.peek()
            if d[ch] == topElem:
                removedElem = stack.pop()
            else:
                return False
        else:
            return False
    
    if stack.isEmpty():
        return True
    return False


exp = input("Enter an expression: ") # "{([])}[]", "{([])})[]", "(([([({{}})])])){{[()]}}"
print(checkExpression(exp))
print(checkExpression_v2(exp))
"""
myStack = Stack()
myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.printStack()
print(myStack.peek())
lastValue = myStack.pop()
print("Last value:", lastValue)
myStack.printStack()
"""


