

def read_map(lines):
    w = len(lines[0])
    h = len(lines)

    obs = []
    pos = None
    facing = ""
    for y, line in enumerate(lines):
        for x, sym in enumerate(line):
            match sym:
                case ".":
                    continue
                case "#":
                    obs.append((x,y))
                case sym if sym in ["<",">","V","^"]:
                    pos = (x,y)
                    facing = sym
                case _:
                    raise Exception(f'Bad symbol "{sym}" at Line {y+1}, Col :{x+1}')
    return (w, h, obs, pos, facing)


def gen_final_block(pos, facing, w, h):
    match facing:
        case "^":
            return (pos[0], -1)
        case "V":
            return (pos[0], h + 1)
        case "<":
            return (-1, pos[1])
        case ">":
            return (w + 1, pos[1])


def get_blocking_obstacles(pos, facing, obs):
    x,y = pos
    match facing:
        case"<":
            return [bar for bar in obs if bar[1] == y and bar[0] < pos[0]]
        case ">":
            return [bar for bar in obs if bar[1] == y and bar[0] > pos[0]]
        case "^":
            return [bar for bar in obs if bar[0] == x and bar[1] < pos[1]]
        case "V":
            return [bar for bar in obs if bar[0] == x and bar[1] > pos[1]]
        case _:
            return []



def guard_dance(lines):
    w, h, obs, pos, pdir = read_map(lines)

    print(f"Step: 0")
    render(w, h, obs, [], pos, pdir)

    DIRS = ["^",">","V","<"]
    visited = []
    final_step = False
    step = 1
    while not final_step:
        blocks = get_blocking_obstacles(pos, pdir, obs)

        if not blocks:
            final_step = True
            blocks = [gen_final_block(pos, pdir, w, h)]

        match pdir:
            case "^":
                closest = blocks[-1]
                next_pos = (pos[0], closest[1] + 1 )
                visited += [(next_pos[0], y) for y in range(closest[1] + 1, pos[1])]
            case "V":
                closest = blocks[0]
                next_pos = (pos[0], closest[1] - 1)
                visited += [(next_pos[0], y) for y in range(pos[1], closest[1])]
            case "<":
                closest = blocks[-1]
                next_pos = (closest[0] + 1, pos[1])
                visited += [(x, next_pos[1]) for x in range(closest[0] + 1, pos[0])]
            case ">":
                closest = blocks[0]
                next_pos = (closest[0] - 1, pos[1])
                visited += [(x, next_pos[1]) for x in range(pos[0], closest[0])]
        
        pdir = DIRS[(DIRS.index(pdir) + 1) % len(DIRS)]

        pos = next_pos

        print(f"Step: {step}")
        render(w, h, obs, visited, pos, pdir)
        step += 1
    print(f"Total: {len(set(visited))}")



def render(w, h, obs, filled, pos, facing):

    def in_field(pos, w, h):
        return pos[0] >= 0 and pos[0] < w and pos[1] >= 0 and pos[1] < h

    field = [["." for _ in range(w)] for _ in range(h)]

    for x,y in obs:
        field[y][x] = "I"

    for x,y in filled:
        if in_field((x,y), w, h):
            field[y][x] = "X"

    if pos and in_field(pos, w, h):
        field[pos[1]][pos[0]] = facing

    for y in range(h):
        for x in range(w):
            print(field[y][x], end=" ")
        print(f" -{y}")

    print(("  "*w)+" \n" + ("| " * w) + " \\")
    print(' '.join([str(i) for i in range(w)]) + "\n")


def main():
    lines = []
    with open("d6.input2") as infile:
        lines = infile.readlines()
        lines = [l.strip() for l in lines]

    guard_dance(lines)

if __name__ == "__main__":
    main()