class Solution:

    def reverseWordsBruteForce(self, s: str):
        result = []
        word = ""
        for char in s:
            if char == " ":
                if word:
                    result.append(word)
                    word = ""
            else:
                word += char

        if word:
            result.append(word)

        result.reverse()
        return " ".join(result)

    def reverseWordsOptimalApproach(self, s: str):

        i = len(s) - 1

        result = ""

        while i >= 0:

            # Skip the trailing spaces
            while i >= 0 and s[i] == " ":
                i -= 1

            if i < 0:
                break

            end = i

            # Find the exact word
            while i >= 0 and s[i] != " ":
                i -= 1

            word = s[i + 1:end + 1]

            if result != "":
                result += " "

            result += word

        return result


if __name__ == '__main__':
    sol = Solution()
    s = "  hello world  "
    # s= "welcome to the jungle"
    # s = "the sky is blue"
    # result = sol.reverseWordsBruteForce(s)
    result = sol.reverseWordsOptimalApproach(s)
    print(result)
