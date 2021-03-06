"""
File: tokens.py

Authors: Laurie Jones, Harry Pinkerton, James Lawson
Project: 11

Tokens for processing expressions.
"""

class Token(object):

    UNKNOWN  = 0        # unknown
    EOE      = 1        # end-of-expression
    L_PAR    = 2        # left parenthesis
    R_PAR    = 3        # right parenthesis
    
    INT      = 4        # integer
            
    MINUS    = 5        # minus    operator
    PLUS     = 6        # plus     operator
    MUL      = 7        # multiply operator
    DIV      = 8        # divide   operator
    MOD      = 11       # modulo
    EXP      = 12       # exponent

    FIRST_OP = 5        # first operator code

    def __init__(self, value):
        if type(value) == int:
            self._type = Token.INT
        else:
            self._type = self.makeType(value)
        self._value = value

    def isOperator(self):
        return self._type >= Token.FIRST_OP

    def __str__(self):
        return str(self._value)
    
    def getType(self):
       return self._type
    
    def getValue(self):
       return self._value

    def makeType(self, ch):
        if   ch == '*': return Token.MUL
        elif ch == '/': return Token.DIV
        elif ch == '+': return Token.PLUS
        elif ch == '-': return Token.MINUS
        elif ch == "%": return Token.MOD
        elif ch == "^": return Token.EXP
        elif ch == '(': return Token.L_PAR
        elif ch == ')': return Token.R_PAR
        elif ch == ';': return Token.EOE
        else:           return Token.UNKNOWN

