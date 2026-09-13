def combination_sum(nums, target):
    result = []
    nums.sort()

    def backtrack(path, balance, index):
        if balance == 0:
            result.append(path.copy())
            return

        if balance < 0:
            return

        for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(path, balance - nums[i], i+1)
                path.pop()


    backtrack([], target, 0)
    return result


if __name__ == '__main__':
    nums = [10,1,2,7,6,1,5]
    target = 8
    print(combination_sum(nums, target))
