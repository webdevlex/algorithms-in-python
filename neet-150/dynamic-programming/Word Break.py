from typing import List


class Solution:
    # Recursion
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i == len(s):
                return True

            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    if dfs(i + len(w)):
                        return True
            return False

        return dfs(0)

    # Recursion (Hash Set)
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        def dfs(i):
            if i == len(s):
                return True

            for j in range(i, len(s)):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1):
                        return True
            return False

        return dfs(0)

    # Dynamic Programming (Top-Down)
    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s): True}

        def dfs(i):
            if i in memo:
                return memo[i]

            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return dfs(0)

    # Dynamic Programming (Top-Down) (Hash Set)
    def wordBreak4(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        t = 0
        for w in wordDict:
            t = max(t, len(w))

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            for j in range(i, min(len(s), i + t)):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return dfs(0)

    # Dynamic Programming (Bottom-Up)
    def wordBreak5(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


solution = Solution()
res = solution.wordBreak("applepenapple", ["cats", "cat", "sin", "in", "car"])
print(res)
