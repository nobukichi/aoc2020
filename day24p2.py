

def move(y, x, d):
    dy = -1 if d[0] == 'n' else 1 if d[0] == 's' else 0
    we = d[0] if dy == 0 else d[1]
    dx = -1 if we == 'w' else 1
    if dy != 0:
        dx = int((dx + (1 if y%2 == 0 else -1)) / 2)
    return y+dy, x+dx


def countBlackTiles(tiles):
    ret = 0
    for yx in tiles:
        ret += tiles[yx]
    return ret


EVENADJ = [ (-1,0), (-1,1), (0,-1), (0,1), (1,0), (1,1) ]
ODDADJ = [ (-1,-1), (-1,0), (0,-1), (0,1), (1,-1), (1,0) ]

def applyP2(tiles):
    nextTiles = {}
    mny, mnx, mxy, mxx = 1e9, 1e9, -1e9, -1e9
    for y, x in tiles:
        mny = min(mny, y)
        mxy = max(mxy, y)
        mnx = min(mnx, x)
        mxx = max(mxx, x)
    for y in range(mny - 1, mxy + 2):
        for x in range(mnx - 1, mxx + 2):
            adjBlk = 0
            for (dy, dx) in (EVENADJ if y % 2 == 0 else ODDADJ):
                if (y+dy, x+dx) in tiles:
                    adjBlk += tiles[(y+dy, x+dx)]
            if (y, x) in tiles:
                # black
                if 1 <= adjBlk <= 2:
                    nextTiles[(y, x)] = 1
            else:
                # whtie
                if adjBlk == 2:
                    nextTiles[(y, x)] = 1
    return nextTiles


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
        flippedTiles.pop((y, x))
    else:
        flippedTiles[(y, x)] = 1


for i in range(100):
    flippedTiles = applyP2(flippedTiles)
    print(countBlackTiles(flippedTiles))
