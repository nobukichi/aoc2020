import math


# Constants given by the puzzle
SEAMONSTER = [
  '                  # ',
  '#    ##    ##    ###',
  ' #  #  #  #  #  #   '
]
SIDE_LEN = 10

# my constants
TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3
TILEID = 0
ROTATION = 1


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


# Extract tile contents by rotating/flipping the tile and removing the border
def getTileContent(tile, rotation):
    flip = False
    if 3 < rotation:
        flip = True
        rotation -= 4
    temp = []
    for i in range(1, SIDE_LEN-1):
        if (flip):
            temp.append(tile[i][::-1][1:SIDE_LEN-1])
        else:
            temp.append(tile[i][1:SIDE_LEN-1])
    if rotation == 0:
        return temp
    ret = []
    if rotation == 1:
        for i in range(SIDE_LEN-2):
            line = ''
            for j in range(SIDE_LEN-2):
                line += temp[SIDE_LEN-3-j][i]
            ret.append(line)
    elif rotation == 2:
        for i in range(SIDE_LEN-2):
            line = ''
            for j in range(SIDE_LEN-2):
                line += temp[SIDE_LEN-3-i][SIDE_LEN-3-j]
            ret.append(line)
    elif rotation == 3:
        for i in range(SIDE_LEN-2):
            line = ''
            for j in range(SIDE_LEN-2):
                line += temp[j][SIDE_LEN-3-i]
            ret.append(line)
    return ret



# extract the tile side info to 8x4 integer list
# the first list contains the side info in top, right, bottom, left order
# we treat # as 1 and . as 0, and treat the left as msb on top and bottom, top as msb on left and right
#  => when rotating clockwise, the value flips when moving right to bottom and left to top
# the fifth list and onward are flipped versions
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
    # add flipped tile
    sides[tid].append([flipSide(top), left, flipSide(bottom), right])
    for i in range(3): # rotate the tile 3 times
        pre = sides[tid][-1]
        sides[tid].append([flipSide(pre[3]), pre[0], flipSide(pre[1]), pre[2]])


# for tid in sides:
#     print('tid', tid , "=>", sides[tid])


# print(sideHist)
# observation: this shows all side values appear once or twice
# tile with two values that appear just once are corners
# and this gives the answer of PART-1
ans1 = 1
cornerTiles = []
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
        cornerTiles.append(tid)
# print(ans1)


# sideToTile[s][v] := list of [tid, rotation] pairs that has side value v on side s
sideToTile = []
for i in range(4):
    sideToTile.append({})
for tid in sides:
    for r in range(8):
        for s in range(4):
            v = sides[tid][r][s]
            if v in sideToTile[s]:
                sideToTile[s][v].append([tid, r])
            else:
                sideToTile[s][v] = [[tid, r]]


# construct images having each possible corners at top left
images = []
for i in range(len(cornerTiles)):
    topLeft = sides[cornerTiles[i]]
    theRotation = []
    for r in range(8):
        if sideHist[topLeft[r][TOP]] == 1 and sideHist[topLeft[r][LEFT]] == 1:
            theRotation.append(r)
    for r in theRotation:
        imgTiles = []
        for j in range(n):
            imgTiles.append([None] * n)
        imgTiles[0][0] = [cornerTiles[i], r]
        for y in range(n):
            for x in range(n):
                leftTid = imgTiles[y][x-1][TILEID] if 0 < x else -1
                leftRotation = imgTiles[y][x-1][ROTATION] if 0 < x else -1
                topTid = imgTiles[y-1][x][TILEID] if 0 < y else -1
                topRotation = imgTiles[y-1][x][ROTATION] if 0 < y else -1
                excludeLeft = lambda tidRot: tidRot[0] != leftTid
                excludeTop = lambda tidRot: tidRot[0] != topTid
                if y == 0:
                    if x == 0:
                        continue
                    left = sides[leftTid][leftRotation][RIGHT]
                    candLeft = list(filter(excludeLeft, sideToTile[LEFT][left]))
                    if len(candLeft) != 1:
                        print('Need to implement backtracking :(')
                        exit()
                    imgTiles[y][x] = candLeft[0]
                elif x == 0:
                    top = sides[topTid][topRotation][BOTTOM]
                    candTop = list(filter(excludeTop, sideToTile[TOP][top]))
                    if len(candTop) != 1:
                        print('Need to implement backtracking :(')
                        exit()
                    imgTiles[y][x] = candTop[0]
                else:
                    left = sides[leftTid][leftRotation][RIGHT]
                    top = sides[topTid][topRotation][BOTTOM]
                    candLeft = list(filter(excludeLeft, sideToTile[LEFT][left]))
                    candTop = list(filter(excludeTop, sideToTile[TOP][top]))
                    if len(candLeft) != 1 or len(candTop) != 1 or candLeft[0][TILEID] != candTop[0][TILEID] or candLeft[0][ROTATION] != candTop[0][ROTATION]:
                        print('Need to implement backtracking :(')
                        exit()
                    imgTiles[y][x] = candLeft[0]
        # print(imgTiles)
        img = []
        for row in range(n):
            tileContents = []
            for col in range(n):
                tileContents.append(getTileContent(tiles[imgTiles[row][col][TILEID]], imgTiles[row][col][ROTATION]))
            for l in range(SIDE_LEN-2):
                line = ''
                for col in range(n):
                    line += tileContents[col][l]
                img.append(line)
        images.append(img)


# Pre-processing to find sea monsters
smwidth = len(SEAMONSTER[0])
smheight = len(SEAMONSTER)
smdef = []
smarea = 0
for i in range(len(SEAMONSTER)):
    occ = []
    pos = 0
    while pos < len(SEAMONSTER[i]):
        pos = SEAMONSTER[i].find('#', pos)
        if 0 <= pos:
            occ.append(pos)
            smarea += 1
            pos += 1
        else:
            break
    smdef.append(occ)


# Count sea monsters in the image
# We count them even if they overlap with each other. I guess we can assume they do not.
def countSeaMonsters(img):
    cnt = 0
    for i in range(len(img)-smheight+1):
        for j in range(len(img[i])-smwidth+1):
            ok = True
            for y in range(smheight):
                for x in smdef[y]:
                    if img[i+y][j+x] != '#':
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                cnt += 1
    return cnt


# count the waves in the image
def countWaves(img):
    cnt = 0
    for line in img:
        cnt += line.count('#')
    return cnt


# PART 2 main
for img in images:
    smcount = countSeaMonsters(img)
    if 0 < smcount:
        ans2 = countWaves(img) - smcount*smarea
        print('answer =', ans2, ', the number of sea monsters =', smcount)

# I am glad that I did not have to implement backtracking, which could have been just tedious
