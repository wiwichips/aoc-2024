#!/usr/bin/env python3

from functools import cmp_to_key

with open('./puzzle_input.txt', 'r') as fp:
#with open('./demo_input.txt', 'r') as fp:
    text = fp.read()

lines = text.split('\n')

g = {} # after ---> before
updates = []
bads = []

for line in lines[:-1]:
    if ',' in line:
        updates.append(list(map(int, line.split(','))))
    elif '|' in line:
        before, after = list(map(int, line.split('|')))
        g[after] = g.get(after, set())
        g[after].add(before)

for update in updates:
    canthave = set()

    for num in update:
        if num in canthave:
            bads.append(update)
            break
        if num in g:
            canthave.update(g[num])

def cmp(left, right):
    if left == right:
        return 0 
    if left in g:
        if right in g[left]:
            return 1
    if right in g:
        if left in g[right]:
            return -1
    return 0 

mids = []

for update in bads:
    update.sort(key=cmp_to_key(cmp))
    mids.append(update[len(update) // 2])

print(sum(mids))


