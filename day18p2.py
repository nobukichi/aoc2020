
# convert '3 * (2 + 1)' to [3, '*', [2, '+', 1]]
def parse(line):
    ret = []
    line = line.strip()
    pos = 0
    while pos < len(line):
        if line[pos] == '*' or line[pos] == '+':
            ret.append(line[pos])
        elif line[pos].isdigit():
            s = pos
            while pos < len(line) and line[pos].isdigit():
                pos += 1
            ret.append(int(line[s:pos]))
        elif line[pos] == '(':
            s = pos+1
            pos += 1
            lvl = 1
            while 0 < lvl:
                if line[pos] == '(':
                    lvl += 1
                if line[pos] == ')':
                    lvl -= 1
                pos += 1
            ret.append(parse(line[s:pos]))
        else:
            print('incorrect input at pos: ', pos, 'in', line)
            exit(-1)
        pos += 1
        # skip whitespace
        while pos < len(line) and line[pos] == ' ':
            pos += 1
    return ret


# convert [1, '*', 2, '+', 3 ] to [1, '*', [2, '+', 3]]
def prioritisePlus(exp):
    if type(exp) is not list or len(exp) == 1:
        return exp
    ret = []
    sub = []
    for i in range(len(exp)):
        if exp[i] == '*':
            ret.append(sub)
            ret.append('*')
            sub = []
        else:
            sub.append(prioritisePlus(exp[i]))
    ret.append(sub)
    return ret


# calculate [3, '*', [2, '+', 1]] from left to right
def calcAux(exp):
    ret = None
    op = ''
    for e in exp:
        t = type(e)
        if t is str:
            op = e
        else:
            val = None
            if t is int:
                val = e
            else:
                val = calcAux(e)
            if ret is None:
                ret = val
            elif op == '*':
                ret *= val
                op = ''
            elif op == '+':
                ret += val
                op = ''
            else:
                print('incorrect expression', exp)
                exit(-2)
    return ret


def calc(line):
    e1 = parse(line)
    e2 = prioritisePlus(e1)
    # print(line)
    # print(e1)
    # print(e2)
    return calcAux(e2)


# read input
lines = []
while (True):
    try:
        lines.append(input())
    except:
        break


# answer the question
ans = 0
for exp in lines:
    ans += calc(exp)
print(ans)
