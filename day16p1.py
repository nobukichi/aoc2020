
mn = 1e18
mx = -1e18

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

myticket = list(map(int, input().split(',')))
mx = max(mx, max(myticket))

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

valid = [False] * (mx+1)

for field in rule:
    for rng in rule[field]:
        for i in range(rng[0], rng[1]+1):
            valid[i] = True

ans = 0
for t in tickets:
    for v in t:
        if not valid[v]:
            ans += v
print(ans)


