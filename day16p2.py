# min and max of values used in the rules and the tickets
mn = 1e18
mx = -1e18

# read rules
rule = {}
while True:
    line = input()
    if line == 'your ticket:':
        break
    tokens = line.split(':')
    if len(tokens) != 2:
        continue
    field = tokens[0]
    rule[field] = []
    tokens = tokens[1].split(' ')
    for t in tokens:
        minMax = t.split('-')
        if len(minMax) != 2:
            continue
        l, r = map(int, minMax)
        rule[field].append([l, r])
        mn = min(mn, l)
        mx = max(mx, r)

# read my ticket
myticket = list(map(int, input().split(',')))
mx = max(mx, max(myticket))

# read near by tickets
while True:
    if input() == 'nearby tickets:':
        break
tickets = []
while True:
    try:
        t = list(map(int, input().split(',')))
        mx = max(mx, max(t))
        tickets.append(t)
    except:
        break

# setup invalid ticket filter
valid = [False] * (mx + 1)
for field in rule:
    for rng in rule[field]:
        for i in range(rng[0], rng[1] + 1):
            valid[i] = True

# validate tickets
validtickets = []
for t in tickets:
    isvalid = True
    for v in t:
        if not valid[v]:
            isvalid = False
            break
    if isvalid:
        validtickets.append(t)

# find the valid fields for each item on the ticket
numfields = len(myticket)
candidates = []
for i in range(numfields):
    candidates.append(set(rule.keys()))
for t in validtickets:
    for i in range(numfields):
        for c in list(candidates[i]):
            ok = False
            for rng in rule[c]:
                if rng[0] <= t[i] <= rng[1]:
                    ok = True
                    break
            if not ok:
                candidates[i].remove(c)

# identify the index of each field
fieldmap = {}
while True:
    progress = False
    for field in rule:
        if field in fieldmap:
            continue
        cnt = 0
        fieldat = -1
        for i in range(numfields):
            if field in candidates[i]:
                fieldat = i
                cnt += 1
        if cnt == 1:
            fieldmap[field] = fieldat
            candidates[fieldat] = {}
            progress = True
            break
    if not progress:
        break

print(fieldmap) # check if all fields can be identified with this logic. seems ok

# calculate the answer
ans = 1
for field in rule:
    if field.startswith('departure'):
        ans *= myticket[fieldmap[field]]
print(ans)
