S = input()
K = int(input())
flag = True

if K >= len(S):
    K = len(S)

for i in range(K):
    if S[i] != '1':
        flag = False
        print(str(S[i]))
        break

if flag:
    print('1')
