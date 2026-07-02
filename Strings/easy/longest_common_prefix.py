from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        first = strs[0]
        last = strs[-1]

        common_prefix= ""

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            common_prefix += first[i]

        return common_prefix

if __name__ == '__main__':
    input_strs= ["interview", "internet", "internal", "interval"]
    print(Solution().longestCommonPrefix(input_strs))
