
def parse(lines):
    width = len(lines[0])
    height = len(lines)

    for ypos, line in enumerate(lines):
        for xpos, c in enumerate(line):
            if c != "A":
                continue

            left_lim = xpos > 0
            right_lim = xpos < width - 1
            up_lim = ypos > 0
            down_lim = ypos < height - 1

            if not ( left_lim and right_lim and down_lim and up_lim):
                continue

            ul = lines[ypos -1][xpos -1]
            ur = lines[ypos -1][xpos +1]
            dl = lines[ypos +1][xpos -1]
            dr = lines[ypos +1][xpos +1]

            fw = ul + dr in ["MS", "SM"]
            bw = ur + dl in ["MS", "SM"]
            if fw and bw:
                yield ('', xpos, ypos)


def main():
    lines = []
    with open("d4.input") as infile:
        lines = infile.readlines()

    total = 0
    for d, x,y in parse(lines):
        print(f"{x+1},{y+1}  <{d}>")
        total +=1

    print(f"Total: {total}")

if __name__ == "__main__":
    main()