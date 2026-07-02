from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = None
        cand2 = None
        result = []

        cand1_count = 0
        cand2_count = 0

        for num in nums:
            if num == cand1:
                cand1_count += 1
            elif num == cand2:
                cand2_count += 1
            elif cand1_count == 0 :
                cand1 = num
                cand1_count=1
            elif cand2_count == 0 :
                cand2 = num
                cand2_count=1
            else:
                cand1_count -= 1
                cand2_count -= 1

        # Count the candidates 1 and candidates 2
        cand1_count = nums.count(cand1)
        cand2_count = nums.count(cand2)

        if cand1_count > len(nums)/3 :
            result.append(cand1)

        if cand1 != cand2 and cand2_count > len(nums)/3 :
            result.append(cand2)

        return result

if __name__ == '__main__':
    solution = Solution()
    result = solution.majorityElement([3,2,3])

    print(result)

