import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'VAR', 'IDENTIFIER', 'COMMA', 'INT', 'BOOL', 'STRING', 'FLOAT'
)

reserved_words = {
    'int': 'INT',
    'bool': 'BOOL',
    'string': 'STRING',
    'float': 'FLOAT'
}

t_ignore = ' \t\n'


def t_VAR(t):
    r'var'
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved_words.get(t.value, 'IDENTIFIER')
    return t

def t_INT(t):
    r'int'
    return t

def t_BOOL(t):
    r'bool'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_STRING(t):
    r'string'
    return t

def t_COMMA(t):
    r','
    return t


def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)


def p_declaration(p):
    '''declaration : VAR list
                    | VAR list type'''
    print("Valid syntax!")


def p_list(p):
    '''list : IDENTIFIER
            | IDENTIFIER COMMA list'''
            
            
def p_type(p):
    '''type : INT
            | BOOL
            | FLOAT
            | STRING'''

def p_error(p):
    print(f"Syntax error at '{p.value}'")


lexer = lex.lex()
parser = yacc.yacc()

example_input = '''
var i,j
var i int
var k bool
var j,n string
var k,l float
'''

lexer.input(example_input)

for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")

s=input("Enter GOLANG code here: ")
parser.parse(s)
