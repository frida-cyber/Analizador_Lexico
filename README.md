# Analizador_Lexico
Analizador lexico Compiladores
import sly: Importa el módulo sly que contiene la clase Lexer que se utilizará más adelante en el código.

class Lexer(sly.Lexer):: Define una clase llamada Lexer que hereda de la clase sly.Lexer.

tokens = {...}: Define un diccionario de tokens que contiene todas las palabras reservadas, operadores, identificadores y constantes del lenguaje que se va a analizar.

literals = '+-*/^{(){}=.;,:': Define una cadena de caracteres que serán considerados literales en el código, es decir, caracteres que no serán tratados como tokens.

FLOAT = r'\d+\.?\d*': Define una expresión regular para reconocer números en punto flotante en el código fuente.

INTEGER = r'\d+': Define una expresión regular para reconocer números enteros en el código fuente.

PLUS= r'\+', MINUS = r'\-', TIMES =r'\*', DIVIDED = r'\/', POWER = r'\^': Define expresiones regulares para reconocer los operadores matemáticos básicos en el código fuente.

ignore = ' \t\r': Define una cadena de caracteres que serán ignorados por el lexer.

ignore_newline = '\n+': Define una expresión regular para ignorar saltos de línea.

ID = r"[a-zA-Z_][a-zA-Z_\-0-9]*": Define una expresión regular para reconocer identificadores en el código fuente.

ID["if"] = IF, ID["for"] = FOR, ID["while"] = WHILE, y así sucesivamente: Asigna a cada palabra reservada del lenguaje su correspondiente token.

LE = r"<=", LT = r"<", EQ = r"==", GE = r">=", GT = r">", NE = r"!=": Define expresiones regulares para reconocer operadores de comparación en el código fuente.

def INTEGER(self,t):: Define un método de la clase Lexer para convertir el valor de los tokens INTEGER de tipo string a tipo entero.

def ignore_newline(self,t):: Define un método de la clase Lexer para contar el número de saltos de línea que se encuentran en el código fuente.

@_(r'\d+(\.\d+)?'): Define un decorador para el método NUMBER de la clase Lexer. Este decorador indica que el método reconocerá números en punto flotante y los convertirá a int o float dependiendo de su valor.

@_(r"'[^']*'",r'"[^"]"'): Define un decorador para el método STRING de la clase Lexer. Este decorador indica que el método reconocerá cadenas de caracteres delimitadas por comillas simples o dobles.

def error(self,t):: Define un método de la clase Lexer para manejar errores en el código fuente.

l = Lexer(): Crea una instancia de la clase Lexer.

while True:: Inicia un ciclo infinito.

text = input("$ "): Pide al usuario que ingrese una línea de código.
