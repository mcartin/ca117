from math import sqrt

class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)
    

binops = {'+': float.__add__,
    '-': float.__sub__,
    '*': float.__mul__,
    '/': float.__truediv__}

uniops = {'n': float.__neg__,
        'r': sqrt}
    

def calculator(line):
    s = Stack()


    for ch in line.split():
        if ch in binops:
            n2 = s.pop()
            n1 = s.pop()
            s.push(binops[ch](n1, n2))
        elif ch in uniops:
            s.push(uniops[ch](s.pop()))
        else:
            s.push(float(ch))

    return s.pop()
    #return s.top()