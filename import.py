import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'IMPORT',
    'QUOTES',
    'FMT',
    'STRINGS',
    'BYTES'
)

t_ignore = ' \t\n'

def t_IMPORT(t):
    r'import'
    return t

def t_QUOTES(t):
    r'"'
    return t

def t_FMT(t):
    r'fmt'
    return t

def t_STRINGS(t):
    r'strings'
    return t

def t_BYTES(t):
    r'bytes'
    return t

def t_error(t):
    print("Illegal character: {t.value[0]}")
    t.lexer.skip(1)

def p_import_statement(p):
    'import_statement : IMPORT QUOTES packagename QUOTES'
    print('Valid Syntax!')

def p_packagename(p):
    '''packagename : FMT
                    | STRINGS
                    | BYTES'''
    pass

    
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF.")
    
lexer = lex.lex()
parser = yacc.yacc()

input_text = 'import "fmt"'
lexer.input(input_text)

for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")

s=input("Enter GOLANG code here: ")
parser.parse(s)
