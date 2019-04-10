from operator import itemgetter

N = int(input())
AB = [list(map(int, input().split(" "))) for _ in range(N)]
CD = [list(map(int, input().split(" "))) for _ in range(N)]

AB = sorted(AB, key=itemgetter(0), reverse=True)
CD = sorted(CD, key=itemgetter(1))
is_pair = [False for _ in range(N)]

count = 0

for a, b in AB:
    for i, cd in enumerate(CD):
        c, d = cd
        if is_pair[i]:
            continue
        if a < c and b < d:
            is_pair[i] = True
            count += 1
            break

print(count)
