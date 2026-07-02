class Solution:
    def countEverySubstrings(self, s, k):

        def atMostSubStrink(k, s):

            left = 0
            count = 0
            freq = {}
            for i, char in enumerate(s):
                freq[char] = freq.get(char, 0) + 1
                while len(freq) > k:
                    char = s[left]
                    freq[char] = freq.get(char, 0) - 1
                    if freq[char] == 0:
                        del freq[char]
                    left += 1

                count = count + (i - left + 1)

            return count


        return atMostSubStrink(k, s) - atMostSubStrink(k-1, s)

if __name__ == '__main__':
    sol = Solution()
    s= "pqpqs"
    # s = [1,2,1,2,3]
    k = 2
    print(sol.countEverySubstrings(s, k))
