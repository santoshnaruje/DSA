class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):

            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                print(right-left-  1)
                if right - left -1 > len(ans):
                    ans = s[left+1:right]


            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                if right - left -1 > len(ans):
                    ans = s[left+1:right]

        return ans



if __name__ == '__main__':
    # s="babad"
    s="cbbd"
    sol = Solution()
    print(sol.longestPalindrome(s))