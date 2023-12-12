
class SymbolTable:
    def __init__(self, symbol_table: dict):
        self.symbol_table = symbol_table

    def getter(self, variable):
        return self.symbol_table[variable]

    def setter(self, variable, value):
        self.symbol_table[variable]["value"] = value
    
    def create(self, variable, value, type):
        if variable in self.symbol_table:
            raise ValueError("\033[91mVariable already exists\033[0m")
        self.symbol_table[variable] = {"value": value, "type": type}