from pycparser import c_parser, c_ast, parse_file
import sys

class FuncCallVisitor(c_ast.NodeVisitor):
    def visit_FuncCall(self, node):
        print(f'Function called: {node.name.name}')
        if node.args:
            print('Arguments:')
            for arg in node.args.exprs:
                if isinstance(arg, c_ast.Constant):
                    print(f'  {arg.type}: {arg.value}')
                elif isinstance(arg, c_ast.ID):
                    print(f'  Variable: {arg.name}')

def show_func_calls(filename):
    try:
        ast = parse_file(filename, use_cpp=True)
        v = FuncCallVisitor()
        v.visit(ast)
        print("Syntax is correct.")
    except Exception as e:
        print(f"Syntax error: {str(e)}")

def parse_and_print_ast(code):
    parser = c_parser.CParser()
    try:
        ast = parser.parse(code)
        ast.show()
        print("Syntax is correct.")
    except c_parser.ParseError as e:
        print(f"Syntax error: {str(e)}")

def check_syntax(code):
    parser = c_parser.CParser()
    try:
        parser.parse(code)
        return True
    except c_parser.ParseError:
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        show_func_calls(sys.argv[1])
    else:
        code = '''
        int main() {
            int x = 5;
            int y = 10;
            if (x < y) {
                printf("x is less than y");
            } else {
                printf("x is not less than y");
            }
            for (int i = 0; i < 10; i++) {
                printf("i: %d", i);
            }
            return 0;
        }
        '''
        parse_and_print_ast(code)
        
        # Example of syntax checking
        print("\nChecking syntax of various code snippets:")
        
        correct_code = code
        print("Correct code syntax:", "Correct" if check_syntax(correct_code)  else "Incorrect")
        
        incorrect_code = code
        print("Incorrect code syntax:", "InCorrect" if check_syntax(incorrect_code) else "Correct")
