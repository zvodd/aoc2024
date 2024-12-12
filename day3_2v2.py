
bigbuf = ""
with open("d3.input") as infile:
    bigbuf = infile.read()


def gen_match(seq)
    for x in seq
        yield x

def parse_data(data):
    do_state = True
    state = 'Initial'
    current_token = ''
    mul_args = []

    m_map = {"do":gen_match("do()"), "dont":gen_match("don't()"), "mul":gen_match("mul(")}
    matchers = {"do":p_do, "dont":p_dont, "mul":p_mul}
    def reset_matchers(key)

    for i in 

    for char in data:
        if state == 'Initial':
            if char == 'd':
                state = 'Keyword'
                current_token += char
            elif char == 'm' and do_state:
                state = 'Mul Function'
                current_token += char
            else:
                pass
        elif state == 'Keyword':
            if char == 'o':
                current_token += char
                if current_token == 'do':
                    do_state = True
                    state = 'Initial'
                elif current_token == 'don\'t':
                    do_state = False
                    state = 'Initial'
            else:
                # Handle unexpected characters
                state = 'Initial'
        elif state == 'Mul Function':
            if char.isdigit():
                current_token += char
            elif char == '(':
                state = 'Mul Argument'
            else:
                # Handle unexpected characters
                state = 'Initial'

        elif state == 'Mul Argument':
            if char.isdigit():
                current_token += char
            elif char == ',':
                mul_args.append(current_token)
                current_token = ''
            elif char == ')':
                mul_args.append(current_token)
                if do_state:
                    # Process the mul operation with args
                    print(f"Multiplying: {mul_args[0]} * {mul_args[1]}")
                mul_args = []
                state = 'Initial'
            else:
                # Handle unexpected characters
                state = 'Initial'


parse_data(bigbuf)