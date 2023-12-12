from Tokenizer import *
from PrePro import *
from Node import *

class Parser:
    def __init__(self):
        self.tokenizer = None
    
    def parseProgram(self):
        children = []
        while self.tokenizer.next.type != "EOF":
            children.append(self.Statement())
                
        return children

    def parseBlock(self):
        if self.tokenizer.next.type == "key":
            self.tokenizer.selectNext()

            if self.tokenizer.next.type == "enter":
                self.tokenizer.selectNext()
            else:
                raise ValueError("\033[91mBloco não possui enter depois da abre chaves\033[0m") 
            
            children_block = []
            while (self.tokenizer.next.type != "key" and self.tokenizer.next.type != "EOF"):
                children_block.append(self.Statement())
            
            if self.tokenizer.next.type != "EOF":
                self.tokenizer.selectNext()
                return Block(children=children_block)
            
            else:
                raise ValueError("\033[91mBloco não possui chave de fechamento\033[0m")
        else:
            raise ValueError("\033[91mBloco não possui chave de abertura\033[0m")

    def parseBoolExpression(self):
        root = self.parseBoolTerm()
        while self.tokenizer.next.type == "or":
            self.tokenizer.selectNext()
            root = BinOp("or", [root, self.parseBoolTerm()])

        return root
    
    def parseBoolTerm(self):
        root = self.parseRelExpression()
        
        while self.tokenizer.next.type == "and":
            self.tokenizer.selectNext()
            root = BinOp("and", [root, self.parseRelExpression()])

        return root
    
    def parseRelExpression(self):
        root = self.parseExpression()
        if self.tokenizer.next.type in ["greater", "less", "equalEqual", "notEqual", "greaterEqual", "lessEqual"]:
            operator = self.tokenizer.next.value
            self.tokenizer.selectNext()
            root = BinOp(operator, [root, self.parseExpression()])

        return root
    
    def Statement(self):
        root = NoOp()
        
        if self.tokenizer.next.type == "Println":
            self.tokenizer.selectNext()

            if self.tokenizer.next.type == "paren":
                self.tokenizer.selectNext()
                root_println = self.parseBoolExpression()
                
                if self.tokenizer.next.type == "paren":
                    self.tokenizer.selectNext()
                    root = Println(children=[root_println])
                else:
                    raise ValueError("\033[91m'println' não possui parênteses de fechamento\033[0m")
            else:
                raise ValueError("\033[91m'println' não possui parênteses de abertura\033[0m")

        elif self.tokenizer.next.type == "if":
            self.tokenizer.selectNext()
            root_if = self.parseBoolExpression()
            root_block = self.parseBlock()
            
            if self.tokenizer.next.type == "else":
                self.tokenizer.selectNext()
                root_else = self.parseBlock()
                root = If(children=[root_if, root_block, root_else])
            else:
                root = If(children=[root_if, root_block])
        
        elif self.tokenizer.next.type == "for":
            self.tokenizer.selectNext()
            root_init = self.tokenizer.next.value
            self.tokenizer.selectNext()
            
            
            if self.tokenizer.next.type == "equal":
                self.tokenizer.selectNext()
                root_init = Assign(children=[root_init, self.parseBoolExpression()])
                if self.tokenizer.next.type == "semicolon":
                    self.tokenizer.selectNext()
                    root_cond = self.parseBoolExpression()
                    if self.tokenizer.next.type == "semicolon":
                        self.tokenizer.selectNext()
                        
                        if self.tokenizer.next.type == "id":
                            root_inc = self.tokenizer.next.value
                            self.tokenizer.selectNext()
                            if self.tokenizer.next.type == "equal":
                                self.tokenizer.selectNext()
                                root_inc = Assign(children=[root_inc, self.parseBoolExpression()])
                                root_block = self.parseBlock()
                                root = For(children=[root_init, root_cond, root_block, root_inc])
                            else:
                                raise ValueError("\033[91m'for' não possui sinal de igualdade\033[0m")
                        else:
                            raise ValueError("\033[91mNão possui ID\033[0m")
                    else:
                        raise ValueError("\033[91m'for' não possui ponto e vírgula\033[0m")
                else:
                    raise ValueError("\033[91m'for' não possui ponto e vírgula\033[0m")
            else:
                raise ValueError("\033[91mNão possui igualdade\033[0m")
        
        elif self.tokenizer.next.type == "id":
            root_id = self.tokenizer.next.value
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "equal":
                self.tokenizer.selectNext()
                root = Assign(children=[root_id, self.parseBoolExpression()])
            else:
                raise ValueError("\033[91mIdentificador não possui sinal de igualdade\033[0m")

        elif self.tokenizer.next.type == "var":
            self.tokenizer.selectNext()
            if self.tokenizer.next.type != "id":
                raise ValueError("\033[91mMissing name of variable\033[0m")
            
            root_id = self.tokenizer.next.value
            self.tokenizer.selectNext()
            
            if self.tokenizer.next.type != "type":
                raise ValueError("\033[91mMissing type of variable\033[0m")
            
            type_var = self.tokenizer.next.value
            self.tokenizer.selectNext()
            
            if self.tokenizer.next.type == "equal":
                self.tokenizer.selectNext()
                root = VarDec(type_var, [root_id, self.parseBoolExpression()])
            else:
                root = VarDec(type_var, [root_id])
        
        if self.tokenizer.next.type in ["enter", "EOF"]:
            self.tokenizer.selectNext()
            return root
        
        raise ValueError("\033[91mStatement inválido\033[0m")
    
    def parseExpression(self):
        root = self.parseTerm()

        while self.tokenizer.next.type in ["plus", "minus", "."]:
            if self.tokenizer.next.type == "plus":
                self.tokenizer.selectNext()
                root = BinOp("+", [root, self.parseTerm()])
            elif self.tokenizer.next.type == "minus":
                self.tokenizer.selectNext()
                root = BinOp("-", [root, self.parseTerm()])
            elif self.tokenizer.next.type == ".":
                self.tokenizer.selectNext()
                root = BinOp(".", [root, self.parseTerm()])

        return root

    
    def parseTerm(self):
        root = self.parseFactor()

        while self.tokenizer.next.type in ["mult", "div"]:
            if self.tokenizer.next.type == "mult":
                self.tokenizer.selectNext()
                root = BinOp("*", [root, self.parseFactor()])
                
            elif self.tokenizer.next.type == "div":
                self.tokenizer.selectNext()
                # divisor = self.parseFactor()
                # if divisor == 0:
                #     raise ValueError("Divisão por zero")
                root = BinOp("//", [root, self.parseFactor()])

        return root

    
    def parseFactor(self):
        if self.tokenizer.next.type == "int":
            root = IntVal(value=self.tokenizer.next.value)
            self.tokenizer.selectNext()
            
            # Verifica se há outro número após um número, o que é inválido
            if self.tokenizer.next.type == "int":
                raise ValueError("\033[91mOperador inválido\033[0m")
        
        elif self.tokenizer.next.type == "string":
            root = String(value=self.tokenizer.next.value)
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "string":
                raise ValueError("\033[91mInvalid operator\033[0m")

        elif self.tokenizer.next.type == "id":
            root = Iden(value=self.tokenizer.next.value)
            self.tokenizer.selectNext()
        
        elif self.tokenizer.next.type in ["plus", "minus", "not"]:
            operator = self.tokenizer.next.value
            self.tokenizer.selectNext()
            root = UnOp(value=operator, children=[self.parseFactor()])

        elif self.tokenizer.next.type == "paren":
            self.tokenizer.selectNext()
            root = self.parseBoolExpression()
            
            # Verifica se o parêntese de fechamento está presente
            if self.tokenizer.next.type != "paren":
                raise ValueError("\033[91mParêntese não fechado\033[0m")
            
            self.tokenizer.selectNext()
        
        elif self.tokenizer.next.type == "Scanln":
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == "paren":
                self.tokenizer.selectNext()
                root = Scanln()
                if self.tokenizer.next.type != "paren":
                    raise ValueError("Parêntese não fechado")
                self.tokenizer.selectNext()
                
        else:
            raise ValueError("\033[91mToken inválido\033[0m")

        return root

    def run(self, code, symbol_table):
        self.tokenizer = Tokenizer(PrePro.filter(code))
        self.tokenizer.selectNext()
        
        for root in self.parseProgram():
            root.evaluate(symbol_table)