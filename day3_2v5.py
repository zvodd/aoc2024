

allowed_funcs = {
    'do': (0),      # do() is allowed
    'don\'t': (0),  # don't() is allowed
    'mul': (2)      # mul(a,b) is allowed with exactly 2 arguments
}

def parse(text):
    delim = "("
    eof = len(text)
    do_state = True

    dcount = 0 
    for i,c in enumerate(text):

        limit_back = min(i, 5) #len("don't")
        limit_forward = min(eof - i, 8) #len("123,123)")

        if c == delim:
            prev = text[i - limit_back:i]
            ahead = text[i+1 : i+1+limit_forward]
            
            found = [*filter(lambda a: prev.endswith(a),  allowed_funcs.keys())]

            if not found:
                #print(f'rejected "{prev}" @ {i}')
                continue

            found = found.pop()
            closing = ahead.startswith(")")

            if found == "don't" and closing:
                do_state = False
            elif found == "do" and closing:
                do_state = True
            elif found == "mul" and do_state:
                result = validate_mul_args(ahead)
                if result:
                    yield result

            # print(f'"{prev}" ( "{ahead}"')
            # dcount += 1
            # if dcount > 10:
            #     break

def validate_mul_args(text):
    ab = text.split(",")
    if len(ab) < 2:
        return False

    a = ab[0]
    _b = ab[1]

    _b = _b.split(")")
    if len(_b) < 2:
        return False

    b = _b[0]

    if a.isdigit() and b.isdigit():
        return (int(a), int(b))
    else:
        return False

def main():
    text = ""
    with open("d3.input") as infile:
        text = infile.read()

    total = 0
    for x,y in parse(text):
        print(f"{x} * {y} = {x*y}")
        total += x*y

    print(f"Total: {total}")

if __name__ == "__main__":
    main()