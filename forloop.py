import ply.lex as lex
import ply.yacc as yacc

keywords = {'for': 'FOR', 'return': 'RETURN', 'println': 'PRINTLN'}

tokens = (
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'IDENTIFIER',
    'GREATER',
    'LESS',
    'PLUS',
    'MINUS',
    'STAR',
    'SLASH',
    'NUMBER',
    'EQUALS',
    'AND',
    'OR',
    'NOT',
    'LPAREN', 
    'RPAREN',
    'QUOTES',
    'COLON') + tuple(keywords.values())

t_ignore = ' \t\n'

t_COLON = r'\:'
t_QUOTES = r'\"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_GREATER = r'>'
t_LESS = r'<'
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_EQUALS = r'='
t_AND= r'\&\&'
t_OR=r'\|\|'
t_NOT=r'!'


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
start="for"


def p_for(p):
    '''
    for : FOR IDENTIFIER COLON EQUALS NUMBER SEMICOLON expression SEMICOLON IDENTIFIER PLUS PLUS statement_or_block
        | FOR IDENTIFIER COLON EQUALS NUMBER SEMICOLON expression SEMICOLON IDENTIFIER MINUS MINUS statement_or_block
    '''
    print('Valid Syntax!')



def p_expression(p):
    '''
    expression : expression GREATER expression
               | expression LESS expression
               | expression GREATER EQUALS expression
               | expression LESS EQUALS expression
               | expression EQUALS EQUALS expression
               | expression AND expression
               | expression OR expression
               | expression NOT EQUALS expression
               | IDENTIFIER
               | NUMBER
               | NOT expression
               | expression PLUS expression
               | expression MINUS expression
               | expression STAR expression
               | expression SLASH expression
               | IDENTIFIER EQUALS expression
    '''





def p_statement_or_block(p):
    '''
    statement_or_block : LBRACE statements RBRACE
                       | statements
    '''

def p_assignment_expression(p):
    '''
    assignment_expression : IDENTIFIER EQUALS expression SEMICOLON
                         | IDENTIFIER PLUS EQUALS expression SEMICOLON
                         | IDENTIFIER MINUS EQUALS expression SEMICOLON
    '''


def p_statements(p):
    '''statements : expression
                | print_statement
                | assignment_statement
                | return_statement
                | assignment_expression
    '''


def p_print_statement(p):
    '''print_statement : PRINTLN LPAREN IDENTIFIER RPAREN 
                        | PRINTLN LPAREN QUOTES IDENTIFIER QUOTES RPAREN'''

def p_assignment_statement(p):
    '''assignment_statement : IDENTIFIER COLON EQUALS expression'''


def p_return_statement(p):
    '''
    return_statement : RETURN IDENTIFIER SEMICOLON
                    | RETURN NUMBER SEMICOLON
                    | RETURN IDENTIFIER
                    | RETURN NUMBER
    '''

 
def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, token={p.value}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

code = "for i:=0;i<9;i++ { return 4;}"

lexer.input(code)
for token in lexer:
    print(f"Token Type: {token.type}, Value: {token.value}")

s=input("Enter GOLANG code here: ")
parser.parse(s)


