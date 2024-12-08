#!/usr/bin/env python3

with open('./puzzle_input.txt', 'r') as fp:
    text = fp.read()

lines = text.split('\n')

g = {} # after ---> before
updates = []
goods = []

for line in lines[:-1]:
    if ',' in line:
        updates.append(list(map(int, line.split(','))))
    elif '|' in line:
        before, after = list(map(int, line.split('|')))
        g[after] = g.get(after, set())
        g[after].add(before)

for update in updates:
    mid = update[len(update) // 2]
    canthave = set()
    success = True 

    for num in update:
        if num in canthave:
            success = False
            break
        if num in g:
            canthave.update(g[num])

    if success:
        goods.append(mid)

print(goods)
print(sum(goods))

