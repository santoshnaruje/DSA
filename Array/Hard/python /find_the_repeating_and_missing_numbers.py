class Solution:
    def find_repeat_and_missing_number_brute_force(self, nums):
        repeating_number = None
        missing_number = None

        for num in range(1,len(nums)+1):
            count = 0
            for j in range(len(nums)):
                if num == nums[j] :
                    count += 1
            if count == 2:
                repeating_number = num
            if count == 0:
                missing_number = num

            if missing_number and repeating_number:
                break

        return repeating_number, missing_number

    def find_repeat_and_missing_number_by_better_approach(self,nums):

        hash_map_nums = [0] * (len(nums)+1)
        missing_number = None
        repeating_number = None

        for num in nums:
            hash_map_nums[num] += 1

        for num in range(1,len(nums)+1):
            if hash_map_nums[num] == 2:
                repeating_number = num
            if hash_map_nums[num] == 0:
                missing_number = num
        return repeating_number, missing_number




if __name__ == '__main__':
    nums = [3, 5, 4, 1, 1]
    s = Solution()
    result= s.find_repeat_and_missing_number_brute_force(nums)
    result2 = s.find_repeat_and_missing_number_by_better_approach(nums)
    print(result)
    print(result2)

