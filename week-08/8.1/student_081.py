class Student(object):

    def set_attributes(self, sid, name, modlist):
        self.sid = sid
        self.name = name
        self.modlist = modlist

    def print_attributes(self):
        print(f'ID: {self.sid}')
        print(f'Name: {self.name}')
        print(f'Modules: {", ".join(self.modlist)}')

    def add_module(self, new_module):
        if new_module not in self.modlist:
            self.modlist.append(new_module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)