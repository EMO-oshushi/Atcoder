N = int(input())
max_available = [int(input()) for _ in range(5)]

tmp = min(max_available)
if tmp >= N:
    print(5)
else:
    print(4 + (N + tmp - 1) // tmp)
