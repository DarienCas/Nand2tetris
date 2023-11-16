import sys
from Parser import *
from Code import *
from SymbolTable import *

class Assembler:
    
    def __init__(self, files):
        self.files = files
        self.table = SymbolTable()
        self.current_address = 16  # Initialize current_address

    def hasFile(self):
        return len(self.files) > 0

    def softPass(self):
        filename = self.files[0]
        p = Parser(filename)
        current_address = 0
        while p.hasMoreCommands():
            p.next()
            cmd_type = p.commandType()
            if cmd_type == A_COMMAND or cmd_type == C_COMMAND:
                current_address += 1
            elif cmd_type == L_COMMAND:
                self.table.addPair(p.symbol(), current_address)

    def getAddress(self, symbol):
        if symbol.isdigit():
            return symbol
        else:
            if not self.table.contains(symbol):
                self.table.addPair(symbol, self.current_address)
                self.current_address += 1
            return self.table.address(symbol)

    def translateFile(self):
        filename = self.files.pop(0)
        p = Parser(filename)
        if filename.endswith('.asm'):
            fileout = filename.replace('.asm', '.hack')
        else:
            fileout = filename + '.hack'
        with open(fileout, 'w') as f:
            print("Translating %s" % (filename))
            while p.hasMoreCommands():
                p.next()
                if p.commandType() == A_COMMAND:
                    address = self.getAddress(p.symbol())
                    instruction = '{0:016b}'.format(int(address))
                elif p.commandType() == C_COMMAND:  # dest=comp;jump
                    instruction = ''.join(['111', Code.comp(p.comp()),
                                           Code.dest(p.dest()), Code.jump(p.jump())])
                else:
                    continue
                print(instruction, end='\n', file=f)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 Assembler.py FILE")
        sys.exit(1)

    a = Assembler(sys.argv[1:])
    while a.hasFile():
        a.softPass()
        a.translateFile()


    a = Assembler(sys.argv[1:])
    while a.hasFile():
        a.softPass()
        a.translateFile()
