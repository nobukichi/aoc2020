

def move(y, x, d):
    dy = -1 if d[0] == 'n' else 1 if d[0] == 's' else 0
    we = d[0] if dy == 0 else d[1]
    dx = -1 if we == 'w' else 1
    if dy != 0:
        dx = int((dx + (1 if y%2 == 0 else -1)) / 2)
    # print('d=', d, 'd[0]=', d[0], 'y=', y, 'we=', we, 'dy=',dy, 'dx=', dx)
    return y+dy, x+dx


flipList = []
flippedTiles = {}


# read rules and messages
while (True):
    try:
        line = input()
        m = []
        i = 0
        while i < len(line):
            if line[i] == 's' or line[i] == 'n':
                m.append(line[i:i+2])
                i += 2
            else:
                m.append(line[i])
                i += 1
        if 0 < len(m):
            flipList.append(m)
    except:
        break


for flip in flipList:
    y, x = 0, 0
    for d in flip:
        y, x = move(y, x, d)
    if (y, x) in flippedTiles:
        flippedTiles[(y, x)] = 1 - flippedTiles[(y, x)]
    else:
        flippedTiles[(y, x)] = 1


ans = 0
for yx in flippedTiles:
    ans += flippedTiles[yx]
print(ans)
