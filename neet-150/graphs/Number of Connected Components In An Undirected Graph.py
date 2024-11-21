class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        res = n
        for n1, n2 in edges:
            res -= uf.union(n1, n2)
        return res


class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n

    def getParent(self, n):
        cur = n
        while cur != self.parents[cur]:
            self.parents[cur] = self.parents[self.parents[cur]]
            cur = self.parents[cur]
        return cur

    def union(self, n1, n2):
        p1, p2 = self.getParent(n1), self.getParent(n2)

        if p1 == p2:
            return 0

        if self.rank[p2] > self.rank[p1]:
            self.parents[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parents[p2] = p1
            self.rank[p1] += self.rank[p2]

        return 1


solution = Solution()
print(solution.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
