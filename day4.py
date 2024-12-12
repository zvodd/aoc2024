
def parse(lines):
    width = len(lines[0])
    height = len(lines)

    for ypos, line in enumerate(lines):
        for xpos, c in enumerate(line):
            if c != "X":
                continue

            left_lim = xpos > 2
            right_lim = xpos < width - 3
            up_lim = ypos > 2
            down_lim = ypos < height - 3
            up_left_lim = left_lim and up_lim
            up_right_lim = right_lim and up_lim
            down_left_lim = left_lim and down_lim
            down_right_lim = right_lim and down_lim

            if line[xpos+1 : xpos+4] == "MAS" and right_lim:
                yield ("forward", ypos, xpos)
        
            # Check backward by checking the previous 3 characters
            if line[xpos-3 : xpos] == "SAM" and left_lim:
                yield ("back", ypos, xpos)

            if up_lim:
                up_check = [lines[ypos-i][xpos] for i in range(1, 4)]
                if up_check == list("MAS"):
                    yield ("up", ypos, xpos)
        
            # Vertical checks (down)
            if down_lim:
                down_check = [lines[ypos+i][xpos] for i in range(1, 4)]
                if down_check == list("MAS"):
                    yield ("down", ypos, xpos)
            
            
            # Up-Left diagonal check
            if up_left_lim:
                up_left_check = [lines[ypos-i][xpos-i] for i in range(1, 4)]
                if up_left_check == list("MAS"):
                    yield ("up-left", ypos, xpos)
            
            # Up-Right diagonal check
            if up_right_lim:
                up_right_check = [lines[ypos-i][xpos+i] for i in range(1, 4)]
                if up_right_check == list("MAS"):
                    yield ("up-right", ypos, xpos)
            
            # Down-Left diagonal check
            if down_left_lim:
                down_left_check = [lines[ypos+i][xpos-i] for i in range(1, 4)]
                if down_left_check == list("MAS"):
                    yield ("down-left", ypos, xpos)
            
            # Down-Right diagonal check
            if down_right_lim:
                down_right_check = [lines[ypos+i][xpos+i] for i in range(1, 4)]
                if down_right_check == list("MAS"):
                    yield ("down-right", ypos, xpos)


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