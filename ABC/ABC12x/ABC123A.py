position = [int(input()) for _ in range(5)]
k = int(input())
if position[4] - position[0] <= k:
    print("Yay!")
else:
    print(":(")
