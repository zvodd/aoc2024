import re


bigbuf = ""
with open("d3.input") as infile:
    bigbuf = infile.read()

argsyntax = re.compile(r"(\d{1,3}),(\d{1,3})\)")


def scanner(buffer):
    eof = len(buffer)
    pos = 0
    while pos < eof:
        m_start_p = buffer.find("mul(", pos)
        rest_p = m_start_p + 4
        if m_start_p < 0:
            break
        else:
            max_next = eof - (rest_p)
            if max_next < 1:
                break
            rest_str = buffer[rest_p:rest_p+min(8, max_next)]
            mg = argsyntax.match(rest_str)

            if mg:
                x,y = int(mg.group(1)), int(mg.group(2))
                yield (x,y)
                pos = m_start_p + mg.endpos
            else:
                # pos = m_start_p + 4
                pos += 1

total = 0 
for x,y in scanner(bigbuf):
    print(f"{x} * {y} = {x*y}")
    total += x*y

print(f"Total: {total}")