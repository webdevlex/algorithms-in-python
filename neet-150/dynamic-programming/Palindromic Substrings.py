class Solution:
    # Brute force
    def countSubstrings1(self, s: str) -> int:
        res = 0
        for l in range(len(s)):
            for r in range(l, len(s)):
                while l <= r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r:
                    res += 1

        return res

    def countSubstrings2(self, s: str) -> int:
        n = len(s)
        memo = [[False] * n for _ in range(n)]

        res = 0
        for l in range(n - 1, -1, -1):  # Start from the last index
            print(f"l: {l}")
            for r in range(l, n):  # Iterate forward for the right boundary
                print(f"r: {r}")
                if s[l] == s[r] and (r - l <= 2 or memo[l + 1][r - 1]):
                    memo[l][r] = True
                    res += 1
        return res

    # Optimized
    def countSubstrings3(self, s: str) -> int:
        res = 0
        for mid in range(len(s)):
            l = mid
            r = mid
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

            l = mid
            r = mid + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1

        return res


solutions = Solution()
res = solutions.countSubstrings2("aaaa")

print(res)
