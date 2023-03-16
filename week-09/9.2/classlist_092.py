class Student(object):

    def __init__(self, name, sid, modlist=None):
        self.name = name
        self.sid = sid
        if modlist is None:
            modlist = []
        self.modlist = modlist

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)

    def average_mark(self):
        return round(sum([int(n[1]) for n in self.modlist]) / len(self.modlist))
    
    def __gt__(self, other):
        return self.average_mark() > other.average_mark()
    
    def __lt__(self, other):
        return self.average_mark() < other.average_mark()
    
    def __eq__(self, other):
        return self.average_mark() == other.average_mark()
    
    def __str__(self):
        output = []
        output.append(f'Name: {self.name}')
        output.append(f'ID: {self.sid}')
        output.append(f'Modules: {", ".join(sorted([s[0] for s in self.modlist]))}')
        output.append(f'Average mark: {self.average_mark()}')
        return "\n".join(output)
    

class Classlist(object):

    def __init__(self, d=None):
        self.d = {} if d is None else d

    def add(self, student):
        self.d[student.sid] = student


    def __str__(self):
        output = []
        for k, v in sorted(self.d.items(), reverse=True):
            output.append(f'{v}')
        return "\n".join(output)
    