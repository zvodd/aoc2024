def parse(lines):
    rules = []
    seqs = []
    state = 0
    for i,line in enumerate(lines):
        if line == "":
            state += 1
            continue
        if state == 0:
            x,y = line.split("|")
            rules.append((int(x), int(y)))
        elif state == 1:
            seqs.append([int(x) for x in line.split(',')])
    return (rules, seqs)


def main():
    lines = []
    with open("d5.input") as infile:
        lines = infile.readlines()
        lines = [l.strip() for l in lines]

    rules, print_seqs = parse(lines)
    rulemap = {}
    for i, r in enumerate(rules):
        if rulemap.get(r[0], None) is None:
            therest = [rules[j][1] for j in range(i,len(rules)) if rules[j][0] == r[0]]
            #therest.sort()
            rulemap[r[0]] = therest

    #print(rulemap)
    #print(print_seqs)
    

    ok_jobs = []
    for job in print_seqs:
        valid = True
        for i_pages, page_no in enumerate(job):
            prempts = rulemap.get(page_no, [])
            for item in job[:i_pages]:
                if item in rulemap.get(page_no, []):
                    valid = False
        if valid:
            ok_jobs.append(job)
    #print(ok_jobs)

    middle_values = [j[len(j) // 2] for j in ok_jobs]
    print(sum(middle_values))

if __name__ == "__main__":
    main()