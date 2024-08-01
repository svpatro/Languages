from stack import *
s = Stack()
s.pop()

for x in range(10):
    s.push(x)

print(s.peak())

for x in range(len(s)):
    print(s.pop())