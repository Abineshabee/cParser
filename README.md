# cParser
#cParser in Python

(py-run) abinesh@abinesh-Lenovo-E41-25:~/Programs/c\>> cd ToyLanguage

(py-run) abinesh@abinesh-Lenovo-E41-25:~/Programs/c/ToyLanguage\>> ls

cParser.py  Lexer  Lexer.c

          (py-run) abinesh@abinesh-Lenovo-E41-25:~/Programs/c/ToyLanguage\>> python cParser.py
FileAST: 

    FuncDef: 
  
    Decl: main, [], [], [], []
    
      FuncDecl: 
      
        TypeDecl: main, [], None
        
          IdentifierType: ['int']
    
    Compound: 
    
      Decl: x, [], [], [], []
      
        TypeDecl: x, [], None
        
          IdentifierType: ['int']
        
        Constant: int, 5
      
      Decl: y, [], [], [], []
      
        TypeDecl: y, [], None
        
          IdentifierType: ['int']
        
        Constant: int, 10
      
      If: 
      
        BinaryOp: <
        
          ID: x
          
          ID: y
        
        Compound: 
        
          FuncCall: 
          
            ID: printf
            
            ExprList: 
            
              Constant: string, "x is less than y"
       
        Compound: 
        
          FuncCall: 
          
            ID: printf
            
            ExprList: 
            
              Constant: string, "x is not less than y"
      
      For: 
      
        DeclList: 
        
          Decl: i, [], [], [], []
          
            TypeDecl: i, [], None
            
              IdentifierType: ['int']
            
            Constant: int, 0
        
        BinaryOp: <
        
          ID: i
          
          Constant: int, 10
        
        UnaryOp: p++
        
          ID: i
        
        Compound: 
        
          FuncCall: 
          
            ID: printf
            
            ExprList: 
            
              Constant: string, "i: %d"
              
              ID: i
      
      Return: 
      
        Constant: int, 0

Syntax is correct.


Checking syntax of various code snippets:

Correct code syntax: Correct

Incorrect code syntax: InCorrect

(py-run) abinesh@abinesh-Lenovo-E41-25:~/Programs/c/ToyLanguage\>> 
