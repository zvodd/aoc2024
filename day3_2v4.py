import re

mul_args_syn = re.compile(r"(\d{1,3}),(\d{1,3})\)")


class FunctionTokenizer:
    def __init__(self, allowed_functions):
        self.allowed_functions = allowed_functions
    
    def tokenize(self, text):
        tokens = []
        
        # Iterate through allowed functions
        for func_name, arg_patterns in self.allowed_functions.items():
            # Create a pattern to match function calls
            # This handles zero or more arguments with optional commas
            pattern = rf'({re.escape(func_name)})(\()([^)]*)\)'
            
            # Find all matches
            matches = re.finditer(pattern, text)
            
            for match in matches:
                endpos = match.lastindex
                length = len(match.group(0))
                token = match.group(1).strip()
                args = match.group(3).strip()
                tokens.append((token, args, endpos, length))
        
        return tokens


def main():
    allowed_funcs = {
        'do': {0},      # do() is allowed
        'don\'t': {0},  # don't() is allowed
        'mul': {2}      # mul(a,b) is allowed with exactly 2 arguments
    }
    
    tokenizer = FunctionTokenizer(allowed_funcs)
    
    test_text = "Here are some function calls: do(), don't(), mul(x,y), invalid(a,b,c)"
    
    with open("d3.input") as infile:
        test_text = infile.read()

    
    # Tokenize
    tokens = tokenizer.tokenize(test_text)

    #print("Matched function calls:", tokens)

    tokens.sort(key=lambda x: x[2])

    print("Matched function calls:")
    for _,_,e,l in tokens:
        print(f"{l}, {e}")

    # total = 0
    # do_state = True
    # for t in tokens:
    #     if t == 'do()':
    #         do_state = True
    #     elif t == 'don\'t()':
    #         do_state = False
    #     elif t.startswith("mul(") and do_state:
    #         mg = mul_args_syn.match(t[4:])
    #         if mg:
    #             x,y = int(mg.group(1)), int(mg.group(2))
    #             total += x*y

    # print("Total:", total)
    
    

if __name__ == "__main__":
    main()