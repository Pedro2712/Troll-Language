from abc import ABC, abstractmethod
from Tokenizer import *

def ErrorTipo():
    raise ValueError(f"\033[91mTipo inválido\033[0m")

class Node(ABC):
    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    @abstractmethod
    def evaluate(self, symbol_table: SymbolTable):
        pass

class BinOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def evaluate(self, symbol_table: SymbolTable):
        operators = {
            "+": lambda x, y: (x[0] + y[0], "int"),
            "-": lambda x, y: (x[0] - y[0], "int"),
            "*": lambda x, y: (x[0] * y[0], "int"),
            "//": lambda x, y: (x[0] // y[0], "int") if y != 0 else (0, "int"),
            "IGUAL?": lambda x, y: (int(x[0] == y[0]), "int") if x[1] == y[1] else ErrorTipo(),
            "NOPE?": lambda x, y: (int(x[0] != y[0]), "int") if x[1] == y[1] else ErrorTipo(),
            ">:": lambda x, y: (int(x[0] > y[0]), "int") if x[1] == y[1] else ErrorTipo(),
            "<:": lambda x, y: (int(x[0] < y[0]), "int") if x[1] == y[1] else ErrorTipo(),
            ">=": lambda x, y: (int(x[0] >= y[0]), "int") if x[1] == y[1] else ErrorTipo(),
            "<=": lambda x, y: (int(x[0] <= y[0]), "int") if x[1] == y[1] else ErrorTipo(),
            "or": lambda x, y: (int(x[0] or y[0]), "int"),
            "and": lambda x, y: (int(x[0] and y[0]), "int"),
            ".": lambda x, y: (str(x[0]) + str(y[0]), "string"),
        }
        
        # Verifica se o operador é válido
        if self.value in operators:
            left_value = self.children[0].evaluate(symbol_table)
            right_value = self.children[1].evaluate(symbol_table)
            
            # Executa a operação usando o operador correspondente
            return operators[self.value](left_value, right_value)
        else:
            raise ValueError(f"Operador inválido: {self.value}")

class IntVal(Node):
    def __init__(self, value, children=[]):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
       return (self.value, "int")

class NoOp(Node):
    def __init__(self):
        super().__init__(value=None, children=[])

    def evaluate(self, symbol_table: SymbolTable):
        pass

class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        operators = {
            "+OMG": lambda x: (x, "int"),
            "-OMG": lambda x: (-x, "int"),
            "NOPE": lambda x: (not x, "int"),
        }

        if self.value in operators:
            operand_value = self.children[0].evaluate(symbol_table)[0]
            return operators[self.value](operand_value)
        else:
            raise ValueError(f"\033[91mOperador unário não suportado: {self.value}\033[0m")

class Block(Node):
    def __init__(self, children, value=None):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        for child in self.children:
            child.evaluate(symbol_table)

class Iden(Node):
    def __init__(self, value):
        super().__init__(value, children=None)

    def evaluate(self, symbol_table: SymbolTable):
        return symbol_table.getter(self.value)["value"]

class Println(Node):
    def __init__(self, children, value = None):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        print(self.children[0].evaluate(symbol_table)[0])

class Assign(Node):
    def __init__(self, children, value=None):
        super().__init__(value, children)
        
    def evaluate(self, symbol_table: SymbolTable):
        variable = symbol_table.getter(self.children[0])
        value = self.children[1].evaluate(symbol_table)
        
        if value[1] != variable["type"]:
            raise ValueError("\033[91mThe type of variable must match\033[0m")
        
        symbol_table.setter(self.children[0], value)

class Scanln(Node):
    def __init__(self, children = None, value=None):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        return (int(input()), "int")

class If(Node):
    def __init__(self, children, value=None):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        if self.children[0].evaluate(symbol_table)[0]:
            return self.children[1].evaluate(symbol_table)
        elif len(self.children) > 2:
            return self.children[2].evaluate(symbol_table)

class For(Node):
    def __init__(self, children, value=None):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        self.children[0].evaluate(symbol_table)
        while self.children[1].evaluate(symbol_table)[0]:
            self.children[2].evaluate(symbol_table)
            self.children[3].evaluate(symbol_table)

class String(Node):
    def __init__(self, value, children=None):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        return (self.value, "string")

class VarDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, symbol_table: SymbolTable):
        if len(self.children) == 2:
            if self.children[1].evaluate(symbol_table)[1] != self.value:
                raise ValueError("\033[91mThe type of variable must match\033[0m")
            symbol_table.create(variable=self.children[0], value= self.children[1].evaluate(symbol_table), type=self.value)
        elif len(self.children) == 1:
            symbol_table.create(variable=self.children[0], value= None, type=self.value)