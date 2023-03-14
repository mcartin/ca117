class Student(object):

    def __init__(self, sid, name, modlist=None):
        self.sid = sid
        self.name = name
        if modlist is None:
            modlist = []
        self.modlist = modlist

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)

    def __str__(self):
        output = []
        output.append(f'ID: {self.sid}')
        output.append(f'Name: {self.name}')
        output.append(f'Modules: {", ".join(sorted(self.modlist))}')
        return "\n".join(output)