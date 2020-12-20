import math

SIDE_LEN = 10

# read tiles
tiles = {}
tid = None
while (True):
    try:
        line = input()
        if line.startswith('Tile '):
            tid = int(line[5:9])
            tiles[tid]= []
        elif line != '':
            tiles[tid].append(line)
    except:
        break
n = round(math.sqrt(len(tiles)))

# extract the tile side info to 4x4 integer list
# the first list contains the side info in top, right, bottom, left order
# we treat # as 1 and . as 0, and treat the left as msb on top and bottom, top as msb on left and right
#  => when rotating clockwise, the value flips when moving right to bottom and left to top
def flipSide(x):
    ret = 0
    for i in range(SIDE_LEN):
        ret = ret * 2 + (1 if (x & (1 << i)) else 0)
    return ret


sides = {}            # tile id => side value array
sideHist = {}         # histogram of side values
for tid in tiles:
    sides[tid] = []
    top = 0
    for i in range(SIDE_LEN):
        top = top * 2 + (1 if tiles[tid][0][i] == '#' else 0)
    right = 0
    for i in range(SIDE_LEN):
        right = right * 2 + (1 if tiles[tid][i][SIDE_LEN-1] == '#' else 0)
    bottom = 0
    for i in range(SIDE_LEN):
        bottom = bottom * 2 + (1 if tiles[tid][SIDE_LEN-1][i] == '#' else 0)
    left = 0
    for i in range(SIDE_LEN):
        left = left * 2 + (1 if tiles[tid][i][0] == '#' else 0)
    sides[tid].append([top, right, bottom, left])
    for i in range(4):
        v = sides[tid][0][i]
        if v in sideHist:
            sideHist[v] += 1
        else:
            sideHist[v] = 1
        v = flipSide(v)
        if v in sideHist:
            sideHist[v] += 1
        else:
            sideHist[v] = 1
    for i in range(3): # rotate the tile 3 times
        pre = sides[tid][-1]
        sides[tid].append([flipSide(pre[3]), pre[0], flipSide(pre[1]), pre[2]])


print(sideHist)
# observation: this shows all side values appear once or twice
# tile with two values that appear just once are corners
# and this gives the answer of PART-1

ans1 = 1
for tid in sides:
    ok = False
    for r in range(4):
        cnt = 0
        for s in range(4):
            if sideHist[sides[tid][r][s]] == 1:
                cnt += 1
        if 2 <= cnt:
            ok = True
    if ok:
        ans1 *= tid
print(ans1)


# sideToTile[s][v] := list of [tid, rotation] pairs that has side value v on side s
sideToTile = [{}] * 4
for tid in sides:
    for r in range(4):
        for s in range(4):
            v = sides[tid][r][s]
            if v in sideToTile[s]:
                sideToTile[s][v].append([tid, r])
            else:
                sideToTile[s][v] = [[tid, r]]

