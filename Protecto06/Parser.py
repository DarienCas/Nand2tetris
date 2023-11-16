import sys, re

A_COMMAND = 'A'
C_COMMAND = 'C'
L_COMMAND = 'L'

class Parser:
    

    def __init__(self, filepath):
        
        try:
            with open(filepath, 'r') as f:
                self.commands = list(filter(len,
                                            [re.sub('//.*$', '', l).strip() for l in f]))
        except FileNotFoundError:
            print("Could not find %s" % (filepath))

    def hasMoreCommands(self):
       
        return len(self.commands) > 0

    def next(self):
        
        self.command = self.commands.pop(0)

    def commandType(self):
       
        if self.command[0] == '@':
            return A_COMMAND
        elif self.command[0] == '(' and self.command[-1] == ')':
            return L_COMMAND
        return C_COMMAND

    def symbol(self):
       
        return self.command.strip('@()')

    def dest(self):
       
        if '=' not in self.command:
            return ''
        return self.command.split('=')[0]

    def comp(self):
       
        return self.command.split('=')[-1].split(';')[0]

    def jump(self):
       
        if ';' not in self.command:
            return ''
        return self.command.split('=')[-1].split(';')[-1]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python Parser.py ARCHIVO")
    else:
        print("Running parser")
    for arg in sys.argv[1:]:
        p = Parser(arg)
        while p.hasMoreCommands():
            p.next()
            print("Symbol: %s, instruction: %s, dest: %s, comp: %s, jump: %s"
                  % (p.symbol(), p.commandType(), p.dest(), p.comp(), p.jump()))