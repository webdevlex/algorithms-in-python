class Solution:
    # Brute Force
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                l, r = i, j
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1

                if l >= r and resLen < (j - i + 1):
                    res = s[i : j + 1]
                    resLen = j - i + 1
        return res

    # Dynamic Programming
    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        memo = [[False] * n for _ in range(n)]

        res, resLen = "", 0
        for r in range(n):
            for l in range(r, -1, -1):
                if s[l] == s[r] and (r - l <= 2 or memo[l + 1][r - 1]):
                    memo[l][r] = True

                    if r - l >= resLen:
                        res = s[l : r + 1]
                        resLen = r - l
        return res

    # Two pointer
    def longestPalindrome3(self, s: str) -> str:
        res, resLen = "", 0
        for center in range(len(s)):
            # Odd
            l = center
            r = center
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

            # Even
            l = center
            r = center + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 >= resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1
        return res


solution = Solution()
res = solution.longestPalindrome3("abba")
print(res)
