def parse(lines):
    rules = []
    seqs = []
    state = 0
    for i,line in enumerate(lines):
        if line.lstrip().startswith("#"):
            continue
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
            rulemap[r[0]] = therest

    #print(rulemap)
    #print(print_seqs)

    ok_jobs = []
    nok_jobs = []
    for job in print_seqs:
        valid = True
        for page_index, page in enumerate(job):
            prempts = rulemap.get(page, [])
            for item in job[:page_index]:
                if item in rulemap.get(page, []):
                    valid = False
                    break
        if valid:
            ok_jobs.append(job)
        else:
            nok_jobs.append(job)
    
    fixed_jobs = []
    for seq in nok_jobs:
        page_index = 0
        sorted_seq = seq.copy()
    
        while page_index < len(sorted_seq):
            page = sorted_seq[page_index]

            sentinal_index = len(seq) + 1
            earliest_index = sentinal_index

            # Find the earliest index of post_page
            for post_page in rulemap.get(page, []):
                try:
                    found = sorted_seq.index(post_page)
                    if found < earliest_index:   
                        earliest_index = found
                except ValueError:
                    continue
            
            # If a valid earlier index is found
            if earliest_index != sentinal_index:
                current_page = sorted_seq.pop(page_index)
                sorted_seq.insert(earliest_index, current_page)
            else:
                page_index += 1
        
        fixed_jobs.append(sorted_seq)

    print("rulemap:".ljust(15, " ") + f"{rulemap}")
    print("#---------------------#")
    print("nok_jobs:".ljust(15, " ") + f"{nok_jobs}")
    print("fixed_jobs:".ljust(15, " ") + f"{fixed_jobs}")
    # print("ok_jobs:".ljust(15, " ") + f"{ok_jobs}")

    print("#---------------------#\n")

    middle_values = [j[len(j) // 2] for j in fixed_jobs]
    print(sum(middle_values))

if __name__ == "__main__":
    main()