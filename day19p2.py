
rule = {}
messages = []
validMessages = {}


def getValidMessages(rid):
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


# check if m is in /^42*(42 31)*$/ form or not
def part2MatchAux(m):
    if m == '':
        return True
    if m[0:8] not in validMessages[42]:
        return False
    if part2MatchAux(m[8:]):
        return True
    return m[len(m)-8:len(m)] in validMessages[31] and part2MatchAux(m[8:len(m)-8])


# check if m contains at least two 42's at the head and at least one 31 at the tail
# if it does, check the inside by calling part2MatchAux
def part2Match(m):
    if len(m) < 24 or len(m) % 8 != 0:
        return False
    if m[0:8] not in validMessages[42] or m[8:16] not in validMessages[42] or m[len(m)-8:len(m)] not in validMessages[31]:
        return False
    return part2MatchAux(m[16:len(m)-8])


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


# ************************************************************************
# PART2 observations
# rule 0: 8 11                 => 8 followed by 11
# rule 8: 42 | 42 | 8          => repetition of 42, at least one
# rule 11: 42 31 | 42 11 31    => x repetition of 42 followed by x repetition of 31 where 1 <= x
#   => rule 0 actually means      y repetition of 42 followed by x repetition of 31 where 1 <= x < y
# rule 42 and rule 31 can be resolved without using rule 8 or rule 11
# the lengths of valid messages that match rule 42 or rule 31 are all 8, which makes the puzzle easy
# ************************************************************************

getValidMessages(42)
getValidMessages(31)
shortest = 1e9
longest = 0
for vm in validMessages[42]:
    shortest = min(shortest, len(vm))
    longest = max(longest, len(vm))
print('For rule 42, shortest =', shortest, 'longest =', longest)
shortest = 1e9
longest = 0
for vm in validMessages[31]:
    shortest = min(shortest, len(vm))
    longest = max(longest, len(vm))
print('For rule 31, shortest =', shortest, 'longest =', longest)


ans = 0
for m in messages:
    if part2Match(m):
        ans += 1
print(ans)

