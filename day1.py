from pprint import pprint 
import sys

va,vb = [],[]
with open(sys.argv[1]) as infile:
    for i, line in enumerate(infile.readlines()):
        a,_,_,b = line.strip().split(' ')
        va.append(int(a))
        vb.append(int(b))
        
# va.sort()
# vb.sort()

# diffs = []
# for a,b in zip(va,vb):
#     diffs.append(abs(a - b))

#pprint(dict(zip([*zip(va,vb)], diffs)))
#print(sum(diffs))

### part 2

tallys = [vb.count(lv) for lv in va]
#pprint(dict(zip(va, tallys)))

score = 0
for v,m in zip(va, tallys):
    score += v * m

print(score)