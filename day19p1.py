
rule = {}
messages = []
validMessages = {}


def getValidMessages(rid):
    print('getValidMessages', rid)
    if rid not in validMessages:
        if type(rule[rid]) is str:
            validMessages[rid] = set(rule[rid])
        else:
            validMessages[rid] = set()
            for candidate in rule[rid]:
                if len(candidate) == 1:
                    validMessages[rid] |= getValidMessages(candidate[0])
                elif len(candidate) == 2:
                    vm0 = getValidMessages(candidate[0])
                    vm1 = getValidMessages(candidate[1])
                    for m0 in vm0:
                        for m1 in vm1:
                            validMessages[rid].add(m0+m1)
                else:
                    print('Unexpected sub-rule length')
                    exit()
    return validMessages[rid]


# read rules and messages
while (True):
    try:
        line = input()
        if ':' in line:
            tokens = line.split(':')
            rid = int(tokens[0])
            if '"' in tokens[1]:
                rule[rid] = tokens[1].split('"')[1]
            else:
                rule[rid] = []
                for t in tokens[1].split('|'):
                    rule[rid].append(list(map(int, t.strip().split())))
        elif line != '':
            messages.append(line)
    except:
        break


# list all valid messages
getValidMessages(0)


ans = 0
for m in messages:
    if m in validMessages[0]:
        ans += 1
print(ans)
