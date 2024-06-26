import lark
from lark import Lark

grammar = """
    start:      decl+
    decl:       vardecl | fundecl
    vardecl:    ("var" | type) ID "=" exp ";"
    fundecl:    ID "(" [fargs] ")" [ ":" rettype ] "{" body "}"
    body:       (vardecl | stmt)* stmt (vardecl | stmt)*
    rettype:    type 
                | "Void"
                | "(" [ rettype ","] rettype ")"
    type:       basictype
                | "[" type "]"
                | ID
    basictype:  "Int"                                                           
                | "Bool"
    fargs:      [ fargs ","] ID [ ":" type]                                 
    stmt:       "if" "(" exp ")" "{" stmt* "}" [ "else" "{" stmt* "}" ]  -> ifelse
                | ID "=" exp ";"
                | funcall ";"
                | return_stmt 
    return_stmt: "return" exp [ "," exp ] ";"
                | "return" ["(" exp [ "," exp ] ")"] ";"

    ?exp:       exp OP2 exp_hipr        
                | exp_hipr
    ?exp_hipr:  funcall
                | ID
                | INT
                | OP1 exp           
                | "(" exp ")"

    
    funcall:    ID "(" [actargs] ")"
    actargs:    exp [ "," actargs]
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

