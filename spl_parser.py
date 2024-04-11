import lark
from lark import Lark

grammar = """
    start:      decl+
    decl:       vardecl | fundecl
    vardecl:    "var" ID "=" exp ";"
    fundecl:    ID "(" [fargs] ")" [ ":" rettype ] "{" vardecl* stmt+ "}"
    rettype:    type 
                | "Void"
                | "(" [ rettype ","] rettype ")"
    type:       "Int"
                | "Bool"
                | "[" type "]"
                | ID
    fargs:      [ fargs ","] ID [ ":" type]
    stmt:       ID "=" exp ";"
                | funcall ";"
                | "return" [ [exp "," ] exp] ";" | "return" "(" [ [exp "," ] exp] ")" ";" 


    ?exp:       exp OP2 exp_hipr        
                | exp_hipr
    ?exp_hipr:    ID
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

