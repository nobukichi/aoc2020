from lark import Lark


# load the grammar for part1 or part2
# parser = Lark(open('grammar_p1.txt').read())
parser = Lark(open('grammar_p2.txt').read())


# calculate the tree parsed by Lark
def calc(tree):
    if tree.data == 'number':
        return int(tree.children[0])
    elif tree.data == 'mul':
        return calc(tree.children[0]) * calc(tree.children[1])
    elif tree.data == 'add':
        return calc(tree.children[0]) + calc(tree.children[1])
    else:
        return calc(tree.children[0])


ans = 0
while (True):
    try:
        ans += calc(parser.parse(input()))
    except:
        break
print(ans)
