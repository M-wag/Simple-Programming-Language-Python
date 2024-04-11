import lark
from lark import Lark

grammar = """
    start:     vardecl
    vardecl:   "var" ID "=" exp ";"
    ?exp:       exp OP2 exp_hipr        
                | exp_hipr

    ?exp_hipr:    ID
                | INT
                | OP1 exp           
                | "(" exp ")"       

    OP2:        "+" | "-" | "*" | "/" | "%"
                | "==" | "<" | ">" | "<=" | ">=" | "!="
                | "&&" | "||"

    OP1:        "!" | "-"
    INT:        /-?\\d+/
    BOOL:       "False" | "True"
    ID:         /[a-zA-Z_][a-zA-Z0-9_]*/


    %ignore /\\s/ 
            | /\\/\\/.*/

"""

spl_parser = Lark(grammar, parser='lalr', debug=True)

