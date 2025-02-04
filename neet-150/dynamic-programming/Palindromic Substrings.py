class Solution:
    # Brute Force
    def countSubstrings1(self, s: str) -> str:
        res = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r:
                    res += 1
        return res

    # Dynamic Programming
    def countSubstrings2(self, s: str) -> str:
        n = len(s)
        memo = [[False] * n for _ in range(n)]

        res = 0
        for r in range(n):
            for l in range(r, -1, -1):
                if s[l] == s[r] and (r - l <= 2 or memo[l + 1][r - 1]):
                    memo[l][r] = True
                    res += 1
        return res

    # Two pointer
    def countSubstrings3(self, s: str) -> str:
        res = 0
        for center in range(len(s)):
            # Odd
            l = center
            r = center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # Even
            l = center
            r = center + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res


solution = Solution()
res = solution.countSubstrings3("aaa")
print(res)
