class Solution:
    def frequencySort(self, s):

        freq = [(0,chr(i + ord("a"))) for i in range(26)]

        for char in s:
            index = ord(char) - ord("a")
            freq[index] = (freq[index][0]+1, char)

        freq.sort(key=lambda x: (-x[0],x[1]))

        for count, char in freq:
            if count > 0:
                print(char)

    def frequencySortOptimal(self,s):

        result=[]

        freq={}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        sorted_char=sorted(freq.items(), key=lambda x: (-x[1],x[0]))

        for char, count in sorted_char:
            result.append(char* count)

        return "".join(result)


if __name__=="__main__":
    s="Aabb"
    sol = Solution()
    print(sol.frequencySortOptimal(s))


































