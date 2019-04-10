S = input()
N = len(S)
count0 = 0
count1 = 0
for c in S:
    if c == "0":
        count0 += 1
    else:
        count1 += 1
print(N - abs(count0 - count1))
