import collections

N = int(input())

words = [input() for i in range(N)]

C = collections.Counter(words)
if C.most_common()[0][1] > 1:
    print('No')
    exit()

for i in range(N-1):
    if words[i][-1] != words[i+1][0]:
        print('No')
        exit()

print('Yes')

        
