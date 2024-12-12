import re


bigbuf = ""
with open("d3.input") as infile:
    bigbuf = infile.read()



def p_gen(seq):
    is_match = None
    pos = 0
    while True:
        nc = yield is_match
        if pos >= len(seq):
            break
        is_match = (seq[pos] == nc)
        pos += 1

def p_do():
    return p_gen("do()")

def p_dont():
    return p_gen("don't()")

def p_mul():
    return p_gen("mul(")

def _p_noop():
    _ = yield None


def p_noop():
    return _p_noop()


nmap = {"do":p_do, "dont":p_dont, "mul":p_mul}

# parsers = {"do":pdo, "dont":pdont, "mul":pmul}
parsers = dict([(name, gen()) for name,gen in nmap.items()])

[next(x) for x in parsers.values()]


no_parse = False
for index,c in enumerate(bigbuf):
    matches = []
    complete = []
    for k,g in parsers.items():
        rv = None
        try:
            rv = g.send(c)
        except StopIteration:
            complete.append(k)
        matches.append((k, rv))

    if 'dont' in complete:
        no_parse = True
    elif 'do' in complete:
        no_parse = False

    if no_parse:
        g = p_noop()
        next(g)
        parsers["mul"] = g

    for k,r in matches:
        if not r:
            if k == "mul" and no_parse:
                pass
            else:
                parsers[k] = nmap[k]()
                next(parsers[k])
        # elif k in complete:
            # print(k)
        else:
            print(f"{index}: {k}  - {complete}")




# total = 0 
# for x,y in scanner(bigbuf):
#     print(f"{x} * {y} = {x*y}")
#     total += x*y

# print(f"Total: {total}")