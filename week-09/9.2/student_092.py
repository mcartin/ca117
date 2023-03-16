class Student(object):

    def __init__(self, name, sid, modlist=None):
        self.name = name
        self.sid = sid
        if modlist is None:
            modlist = []
        self.modlist = modlist

    def average_mark(self):
        return round(sum([int(n[1]) for n in self.modlist]) / len(self.modlist))
    
    def __str__(self):
        output = []
        output.append(f'Name: {self.name}')
        output.append(f'ID: {self.sid}')
        output.append(f'Modules: {", ".join(sorted([s[0] for s in self.modlist]))}')
        output.append(f'Average mark: {self.average_mark()}')
        return "\n".join(output)