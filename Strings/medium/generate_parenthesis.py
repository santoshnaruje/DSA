from typing import List


def generateParenthesis(n):
    result = []

    def backtrack(current, open, close):

        # 1. Base case
        if len(current) == 2 * n:
            result.append(current)
            return

        # 2. Add opening bracket
        if open < n:
            current += "("
            backtrack(current, open + 1, close)
            current = current[:-1]

        # 3. Add closing bracket
        if close < open:
            current += ")"
            backtrack(current,open,close+1)
            current = current[:-1]

    backtrack("", 0, 0)

    return result

if __name__ == "__main__":
    n = 1
    sol = generateParenthesis(n)
    print(sol)
