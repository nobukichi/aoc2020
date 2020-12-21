
# read input
foods = []    # list of { "ingr" : set of ingredients, "alle": set of allergens }
ingredients = set()
allergens = set()
while (True):
    try:
        line = input()
        tokens = line.split(' (contains ')
        if 1 < len(tokens):
            f = { "ingr": set(tokens[0].split()), "alle": set(tokens[1].split(')')[0].split(', '))}
            ingredients |= f["ingr"]
            allergens |= f["alle"]
            foods.append(f)
    except:
        break
# print('ingredients', ingredients)
# print('allergens', allergens)
# print('foods', foods)


mayContain = {}  # mayContain[i] := set of allergens that an ingredient i may contain
for i in ingredients:
    mayContain[i] = allergens.copy()
for f in foods:
    for a in f["alle"]:
        for i in ingredients:
            if i not in f["ingr"] and a in mayContain[i]:
                mayContain[i].remove(a)
print('mayContain', mayContain)


safeIngredients = set()
for i in mayContain:
    if len(mayContain[i]) == 0:
        safeIngredients.add(i)
print('safeIngredients', safeIngredients)


ans1 = 0
for f in foods:
    ans1 += len(f["ingr"] & safeIngredients)
print('ans1', ans1)


mayBeIn = {}  # mayBeIn[a] := set of ingredients that allergen a may be included in
for a in allergens:
    mayBeIn[a] = set()
    for i in mayContain:
        if a in mayContain[i]:
            mayBeIn[a].add(i)
print('mayBeIn', mayBeIn)


alleToIngr = {}  # definite allergen to ingredient mapping
while True:
    identifiedIngr = None
    for a in mayBeIn:
        if len(mayBeIn[a]) == 1:
            identifiedIngr = mayBeIn[a].pop()
            alleToIngr[a] = identifiedIngr
            mayBeIn.pop(a)
            break
    if identifiedIngr is not None:
        for a in mayBeIn:
            if identifiedIngr in mayBeIn[a]:
                mayBeIn[a].remove(identifiedIngr)
    else:
        break


dangerousIngredients = []
for a in sorted(allergens):
    dangerousIngredients.append(alleToIngr[a])
print('ans2', ','.join(dangerousIngredients))
