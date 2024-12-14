

def read_map(lines):
    w, h = len(lines[0]), len(lines)
    obs, pos, facing = [], None, ""
    
    for y, line in enumerate(lines):
        for x, sym in enumerate(line):
            match sym:
                case "." | " ":
                    continue
                case "#":
                    obs.append((x,y))
                case sym if sym in ["<", ">", "V", "^"]:
                    pos, facing = (x,y), sym
                case _:
                    raise ValueError(f'Invalid symbol "{sym}" at Line {y+1}, Col {x+1}')
    
    return (w, h, obs, pos, facing)


def gen_final_block(pos, facing, w, h):
    return {
        "^": (pos[0], -1),
        "V": (pos[0], h + 1),
        "<": (-1, pos[1]),
        ">": (w + 1, pos[1])
    }[facing]


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


def get_intermediate_vectors(start, end):
    """Generate intermediate points between start and end in Manhattan distance."""
    x1, y1 = start
    x2, y2 = end
    
    if x1 == x2:
        return [(x1, y) for y in range(min(y1, y2) + 1, max(y1, y2))]
    elif y1 == y2:
        return [(x, y1) for x in range(min(x1, x2) + 1, max(x1, x2))]
    return []

def next_player_direction(facing):
    DIRS = ["^", ">", "V", "<"]
    return DIRS[(DIRS.index(facing) + 1) % len(DIRS)]

def guard_dance(lines):
    w, h, obs, pos, pdir = read_map(lines)

    print(f"Step: 0")
    render(w, h, obs, [], pos, pdir)


    visited = []
    step = 0
    finished = False
    while not finished:
        blocks = get_blocking_obstacles(pos, pdir, obs)
        
        if not blocks:
            blocks = [gen_final_block(pos, pdir, w, h)]
            finished = True

        # find closest obstacle
        if pdir in ["^","<"]:
            closest = blocks[-1]
        else:
            closest = blocks[0]

        # determine next position
        match pdir:
            case "^":
                next_pos = (pos[0], closest[1] + 1)
            case "V":
                next_pos = (pos[0], closest[1] - 1)
            case "<":
                next_pos = (closest[0] + 1, pos[1])
            case ">":
                next_pos = (closest[0] - 1, pos[1])

        visited += [pos]
        visited += get_intermediate_vectors(pos, next_pos)
        visited += [next_pos]

        pdir = next_player_direction(pdir)
        pos = next_pos
        step += 1

        print(f"Step: {step}")
        render(w, h, obs, visited, pos, pdir)

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