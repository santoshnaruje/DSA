class Solution:
    def get_combination(self, nums,target):

        result = []

        def get_backtrack(index, remaining, path):

            if remaining == 0:
                result.append(path.copy())
                return

            if index == len(nums) or remaining < 0:
                return

            path.append(nums[index])
            get_backtrack(index, remaining - nums[index], path)
            path.pop()
            get_backtrack(index + 1, remaining, path)

        get_backtrack(0, target, [])
        return result

    def get_combination_using_for_loop_backtrack(self, nums, target):

        result = []

        def get_backtrack(start, remaining, path):

            if remaining == 0:
                result.append(path.copy())
                return

            if start == len(nums) or remaining < 0:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                get_backtrack(i, remaining - nums[i], path)
                path.pop()

        get_backtrack(0, target, [])
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 6, 7]
    target = 7
    #
    # nums = [1, 2]
    # target = 50

    print(solution.get_combination(nums, target))
    print(solution.get_combination_using_for_loop_backtrack(nums, target))
