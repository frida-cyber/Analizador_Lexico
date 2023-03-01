import sly
class Lexer(sly.Lexer):
    tokens = {
        #palabras resevadas
        IF,FOR,WHILE,FUNCTION,RETURN,END,NOT,BREAK,ELIF,OR,AND,
        CONTINUE,
        LET,READ,DATA,PRINT,GOTO,THEN,NEXT,TOS,STEP,STOP,DEF,GOSUB,
        DIM,REM,RUN,LIST,NEW,
        #OPERADORES
        PLUS,MINUS,TIMES,DIVIDED,POWER,

        #operadores
        EQ,NE,LT,GT,LE,GE,

        #identificadores
        ID,

        #constantes
        INTEGER,FLOAT,STRING,
        #NIL,NUMBER,TRUE,FALSE,STRING,BOOLEAN,INTEGER,FLOAT
    }
    literals = '+-*/^{(){}=.;,:'

    #DEFINICION DE TOKENS
    FLOAT = r'\d+\.?\d*'
    INTEGER = r'\d+'

    PLUS= r'\+'
    MINUS = r'\-'
    TIMES =r'\*'
    DIVIDED = r'\/'
    POWER = r'\^'


    #PATRONES A IGNORAR
    ignore = ' \t\r'
    ignore_newline =  '\n+'

    #PALABRAS RESERVADAS
    ID = r"[a-zA-Z_][a-zA-Z_\-0-9]*"
    ID["if"] = IF
    ID["for"] = FOR
    ID["while"] = WHILE
    ID["return"] = RETURN
    ID["end"] = END
    ID["not"] = NOT
    ID["break"] = BREAK
    ID["elif"] = ELIF
    ID["or"] = OR
    ID["and"] = AND
    ID["continue"] = CONTINUE
    ID["let"]= LET
    ID["read"]= READ
    ID["data"]= DATA
    ID["print"]= PRINT
    ID["goto"]= GOTO
    ID["then"]= THEN
    ID["next"]= NEXT
    ID["tos"]=TOS
    ID["step"]= STEP
    ID["stop"]= STOP
    ID["def"]= DEF
    ID["gosub"]= GOSUB
    ID["dim"]= DIM
    ID["rem"]= REM
    ID["run"]= RUN
    ID["list"]= LIST
    ID["new"]= NEW

    #OPERADORES
    LE = r"<="
    LT = r"<"
    EQ = r"=="
    GE = r">="
    GT = r">"
    NE = r"!="
    
    def INTEGER(self,t):
        t.value=int(t.value)
        return t

    def ignore_newline(self,t):
        self.lineno += t.value.count("\n")

    @_(r'\d+(\.\d+)?')
    def NUMBER(self,t):
        try:
            t.value = int(t.value)
        except ValueError:
            t.value = float(t.value)
        return t

    @_(r"'[^']*'",r'"[^"]"')
    def STRING(self,t):
        return t

def error(self,t):
        print(f" Caracter ilegal {t}")
        self.index += 1

def main():
    l = Lexer()
    while True:
        try:
            text = input("$ ")
            for tok in l.tokenize(text):
                print(tok)
        except EOFError:
            break
main()
