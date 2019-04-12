N = int(input())
HP = set(map(int, input().split(" ")))

while len(HP) > 1:
    minHP = min(HP)
    nextHPs = set([minHP])
    for each_HP in HP:
        temp = each_HP % minHP
        if temp != 0:
            nextHPs.add(temp)
    HP = list(nextHPs)
print(list(HP)[0])
