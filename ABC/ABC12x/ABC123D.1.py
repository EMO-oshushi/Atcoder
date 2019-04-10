import heapq


class Delicious (object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def total(self):
        return(A[self.x] + B[self.y] + C[self.z])

    def __lt__(self, other):
        return self.total() > other.total()


X, Y, Z, K = map(int, input().split(" "))
A = sorted(map(int, input().split(" ")), reverse=True)
B = sorted(map(int, input().split(" ")), reverse=True)
C = sorted(map(int, input().split(" ")), reverse=True)

ds = []
heapq.heappush(ds, Delicious(0, 0, 0))

check = {}

for _ in range(K):
    d = heapq.heappop(ds)
    while (d.x, d.y, d.z) in check:
        d = heapq.heappop(ds)
    print(d.total())
    check[d.x, d.y, d.z] = True

    if d.x < X-1:
        heapq.heappush(ds, Delicious(d.x+1, d.y, d.z))
    if d.y < Y-1:
        heapq.heappush(ds, Delicious(d.x, d.y+1, d.z))
    if d.z < Z-1:
        heapq.heappush(ds, Delicious(d.x, d.y, d.z+1))
