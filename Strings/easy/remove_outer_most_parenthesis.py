class Solution:
    def removeOuterParentheses(self, chars: str) -> str:
        result = ""
        level = 0
        for char in chars :
            if char == "(" :
                level += 1
                if level > 1 :
                    result += char
            elif char == ")":
                if level > 1 :
                    result += char
                level -= 1
        return result


if __name__ == "__main__":
    solution = Solution()
    s = "(()())(())"
    print(solution.removeOuterParentheses(s))




