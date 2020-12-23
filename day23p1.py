# data = '389125467'
data = '398254716'


def moveOne(s):
    mx = len(s)
    curr = int(s[0])
    pickedup = list(map(int, list(s[1:4])))
    dest = mx if curr == 1 else curr-1
    while dest in pickedup:
        dest = mx if dest == 1 else dest-1
    destPos = s.find(str(dest))
    print('mx=', mx, 'curr=', curr, 'dest=', dest, 'destPos=', destPos)
    return s[4:destPos+1] + s[1:4] + s[destPos+1:] + s[0]


def answer(s):
    onePos = s.find('1')
    return s[onePos+1:] + s[:onePos]


print(data)
for i in range(100):
    data = moveOne(data)
    print(' =>', data)
print(answer(data))
