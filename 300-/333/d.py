"""
グラフの問題

考え方
木で考える
頂点１を根とする部分木の大きさの最小値

DSUとは
Disjoint Set Unionの略で、和訳すると「素集合データ構造」となる。
Union
Find


"""


class DSU:
    def __init__(self, n):
        # 各要素の親はそれぞれの数字なので格納
        self.parent = list(range(n))
        # 高さを示す
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        #親が異なる、すなわち異なる集合に属している時
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

def main():
    N = int(input())
    forest = DSU(N)

    for i in range(1, N):
        u, v = map(int, input().split())
        if u != 1:
            forest.union(u - 1, v - 1)

    group_sizes = [len(list(group)) for group in forest.groups()]
    result = N - max(group_sizes)
    
    print(result)

if __name__ == "__main__":
    main()
