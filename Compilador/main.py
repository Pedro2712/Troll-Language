import sys
from Parser import *
from SymbolTable import *

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    input = f.read()


def main():
    Parser().run(input, SymbolTable({}))

if __name__ == "__main__":
    main()