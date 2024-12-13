
def guard_dance(lines):
    map_w = len(lines[0])
    map_h = len(lines)

    obs_x = []
    obs_y = []
    start_pos = None
    start_dir = ""
    for ypos, line in enumerate(lines):
        for xpos, sym in enumerate(line):
            match sym:
                case ".":
                    continue
                case "#":
                    obs_x.append(xpos)
                    obs_y.append(ypos)
                case _:
                    start_pos = (xpos,ypos)
                    start_dir = sym
                    if not sym in ["<",">","V","^"]:
                        raise Exception(f'Bad symbol "{sym}" at {xpos},{ypos}')

    obs = [*zip(obs_x, obs_y)]
    pdir = start_dir
    pos = start_pos

    visited = []
    is_end = False
    while not is_end:
        blk_ix = []
        if pdir in ["<", ">"]:
            blk_ix = indexs_of_list(pos[1], obs_y)
            if pdir == "<":
                blk_ix = filter(lambda x: obs_x[x] < pos[0], blk_ix)
            else:
                blk_ix = filter(lambda x: obs_x[x] > pos[0], blk_ix)
        else:
            blk_ix = indexs_of_list(pos[0], obs_x)
            if pdir == "^":
                blk_ix = filter(lambda y: obs_y[y] < pos[1], blk_ix)
            else:
                blk_ix = filter(lambda y: obs_y[y] > pos[1], blk_ix)

        blocks = [obs[i] for i in blk_ix]
        # print(blocks)
        
        # Positions are already spacially sorted.
        #blocks.sort(key=lambda w: abs(w[0] - pos[0]) )

        start_pos = pos

        is_end = len(blocks) == 0
        if is_end:
            match pdir:
                case "^":
                    blocks = [(pos[0], -1)]
                case "V":
                    blocks = [(pos[0], map_h+1)]
                case "<":
                    blocks = [(-1, pos[1])]
                case ">":
                    blocks = [(map_w+1, pos[1])]

        match pdir:
            case "^":
                closest = blocks[-1]
                pos = (pos[0], closest[1] + 1 )
                visited += [(pos[0], y) for y in range(closest[1] + 1, start_pos[1])]
                pdir = ">"
            case "V":
                closest = blocks[0]
                pos = (pos[0], closest[1] - 1)
                visited += [(pos[0], y) for y in range(start_pos[1], closest[1])]
                pdir = "<"
            case "<":
                closest = blocks[-1]
                pos = (closest[0] + 1, pos[1])
                visited += [(x, pos[1]) for x in range(closest[0] + 1, start_pos[0])]
                pdir = "^"
            case ">":
                closest = blocks[0]
                pos = (closest[0] - 1, pos[1])
                visited += [(x, pos[1]) for x in range(start_pos[0], closest[0])]
                pdir = "V"

        #render(map_w, map_h, obs, visited, pos, pdir)
    print(f"Total: {len(set(visited))}")

        

def indexs_of_list(value, lst):
    return [i for i, x in enumerate(lst) if x == value]


def render(w, h, obs, filled, pos, pdir):
    field = [["." for _ in range(w)] for _ in range(h)]
    for x,y in obs:
        field[y][x] = "0"
    for x,y in filled:
        if in_field((x,y), w, h):
            field[y][x] = "x"
    if pos and in_field(pos, w, h):
        field[pos[1]][pos[0]] = pdir
    for y in range(h):
        for x in range(w):
            print(field[y][x], end="")
        print("")

def in_field(pos, w, h):
    return pos[0] >= 0 and pos[0] < w and pos[1] >= 0 and pos[1] < h

def main():
    lines = []
    with open("d6.input") as infile:
        lines = infile.readlines()
        lines = [l.strip() for l in lines]

    guard_dance(lines)

if __name__ == "__main__":
    main()