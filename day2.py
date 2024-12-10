from pprint import pprint 
import sys

reps = []
with open(sys.argv[1]) as infile:
    for i, line in enumerate(infile.readlines()):
        reps.append([int(x) for x in line.strip().split(' ')])

#pprint([x for i,x in enumerate(reps) if i < 10])

safe_reports = 0
for rep in reps:
    prev = rep[0]
    is_asc = None
    is_highvariance = False
    is_dirswap = False
    is_stagnent = False
    for i,v in enumerate(rep[1:]):
        i+=1
        if not is_asc is None and not is_dirswap:
            if v > prev:
                if not is_asc:
                    is_dirswap = True
                is_asc = True
            elif v < prev:
                if is_asc:
                    is_dirswap = True
                is_asc = False
        else:
            is_asc = (v > prev)

        if v == prev:
                is_stagnent = True

        if abs(v - prev) > 3:
            is_highvariance = True

        prev = v
    if not is_dirswap and not is_highvariance and not is_stagnent:
        safe_reports +=1

print(f"Safe Reports: {safe_reports}")