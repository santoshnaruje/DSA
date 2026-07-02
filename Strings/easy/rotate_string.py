class Solution:
    def rotateString(self, s: str, goal) -> bool:

        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            if rotated == goal:
                return True
        return False

    def rotateStringOptimal(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s+s


if __name__ == "__main__":
    string = "rotation"
    goal = "tionrota"
    solution = Solution()
    print(solution.rotateStringOptimal(string, goal))
