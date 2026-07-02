class Solution:
    def largestOdd(self, s):

        end = len(s) - 1
        start = 0

        while end >=0:
            if int(s[end]) % 2 != 0:
                break
            end = end - 1

        while start <= end:
            if s[start] != '0' :
                break
            start = start + 1

        print(s[start:end+1])


if __name__ == '__main__':
    s= "0214638"
    sol = Solution()
    print(sol.largestOdd(s))