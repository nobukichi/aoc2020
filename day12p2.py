x = 0
y = 0
dx = 10
dy = 1

n = int(input())
for i in range(n):
    line = input()
    t = line[0]
    o = int(line[1:])
    if t == 'N':
        dy += o
    elif t == 'S':
        dy -= o
    elif t == 'E':
        dx += o
    elif t == 'W':
        dx -= o
    elif t == 'L':
        for j in range(0, o, 90):
            tmp = dx
            dx = -dy
            dy = tmp
    elif t == 'R':
        for j in range(0, o, 90):
            tmp = dy
            dy = -dx
            dx = tmp
    elif t == 'F':
        x += dx * o
        y += dy * o
    print('after step ', i , ' x = ', x, ', y = ', y, ', dx = ', dx, ', dy = ', dy)
print(abs(x)+abs(y))