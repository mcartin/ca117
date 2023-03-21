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


def matcher(line):
    d = {')': '(',
     '}': '{',
     ']': '['}

    s = Stack()
    for c in line:
        if c in d.values():
            s.push(c)
        elif c in d.keys():
            if s.is_empty() or s.pop() != d[c]:
                return False
    return s.is_empty()