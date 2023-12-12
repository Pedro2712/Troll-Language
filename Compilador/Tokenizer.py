from SymbolTable import *


def testa(dicionario, palavra, booleano = True):
    
    for key in dicionario.keys():
        if key in palavra:
            if booleano:
                return True
            return key
        
    return False
    

class Token:
    
    def __init__ (self, type: str, value: int):
        self.type = type
        self.value = value

class Tokenizer:
    
    def __init__ (self, source):
        self.source = source
        self.position = 0
        self.next = Token(type(source), source)
        self.reserved_words = {
                                "YELL": "Println",
                                "Scanln": "Scanln",
                                "LOL": "if",
                                "ROFL": "else",
                                "EPICFAIL": "for",
                                "MAGIC": "var",
                                "InTiGeR": "int",
                                "StRiNg": "string",
                                "IGUAL": "equal",
                                "NOPE": "not",
                            }
        self.token_map = {
                            "+OMG": "plus",
                            "-OMG": "minus",
                            "IGUAL?": "equalEqual",
                            "•": "mult",
                            "÷": "div",
                            "ʕ•ᴥ•ʔ": "paren",
                            "\n": "enter",
                            "🐶": "or",
                            "🐱": "and",
                            ">:": "greater",
                            "<:": "less",
                            "<=": "lessEqual",
                            ">=": "greaterEqual",
                            "NOPE?": "notEqual",
                            "<3": "semicolon",
                            "ಠ_ಠ": "key",
                            ".": ".",
                            '"': "quote",
                        }
    
    def selectNext(self):    
        if self.position < len(self.source):
            char = self.source[self.position]
            char2 = self.source[self.position: self.position+2]
            char3 = self.source[self.position: self.position+3]
            char4 = self.source[self.position: self.position+4]
            char5 = self.source[self.position: self.position+5]
            char6 = self.source[self.position: self.position+6]
            
            if char.isdigit():
                number = ""
                while self.position < len(self.source) and self.source[self.position].isdigit():
                    number += self.source[self.position]
                    self.position += 1
                self.next = Token("int", int(number))  
            
            
            elif char2 in self.token_map:
                self.next = Token(self.token_map[char2], char2)
                self.position += 2
            
            elif char3 in self.token_map:
                self.next = Token(self.token_map[char3], char3)
                self.position += 3
                
            elif char4 in self.token_map:
                self.next = Token(self.token_map[char4], char4)
                self.position += 4
            
            elif char5 in self.token_map:
                self.next = Token(self.token_map[char5], char5)
                self.position += 5
            
            elif char6 in self.token_map:
                self.next = Token(self.token_map[char6], char6)
                self.position += 6
                
            elif char in self.token_map:
                if char == '"':
                    self.position += 1
                    string = ""
                    while self.source[self.position] != '"':
                        if self.source[self.position] == "\n":
                            raise ValueError("\033[91mMissing quotes\033[0m")
                        string += self.source[self.position]
                        self.position += 1
                        
                    self.next = Token(type="string", value=string)
                    self.position += 1
                else:          
                    self.next = Token(self.token_map[char], char)
                    self.position += 1
            
            else:
                # Verifique se é uma palavra-chave ou identificador
                word = ""
                while self.position < len(self.source) \
                        and (self.source[self.position].isalnum() or self.source[self.position] == "_") \
                        and not testa(self.reserved_words, word):
                    word += self.source[self.position]
                    self.position += 1
                
                existe = testa(self.reserved_words, word, False)
                    
                    
                if word in self.reserved_words:
                    if word == "InTiGeR":
                        self.next = Token("type", "int")
                    elif word == "StRiNg":
                        self.next = Token("type", "string")
                    else:
                        self.next = Token(self.reserved_words[word], word)  # Palavra reservada
                else:
                    if existe:
                        word = word.replace(existe, "")
                        self.next = Token("id", word)  # Identificador
                        self.position -= len(existe)
                    
                    else:
                        try:
                            
                            if word[-1] in ["ʕ"]:
                                word = word[:-1]
                                self.position -= 1
                            
                            self.next = Token("id", word)
                        except:
                            print("Erro")
                            pass
        else:
            self.next = Token("EOF", 0)