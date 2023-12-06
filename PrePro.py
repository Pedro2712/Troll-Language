import re

class PrePro:    
    @staticmethod
    def filter(code):
        # Remove comentários de linha (// ...)
        code = re.sub(r'//.*', '', code)

        # Verifica se há números separados por espaços
        if re.search(r'\d\s+\d', code):
            raise ValueError("\033[91mErro: Dois números estão separados por espaço\033[0m")
        
        # Divide o código em linhas e remove tabs do início de cada linha
        lines = code.split('\n')
        code = '\n'.join([line.lstrip('\t') for line in lines])

        # Remove espaços em branco
        code = code.replace(" ", "")
        
        return code
