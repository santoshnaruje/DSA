def combination_sum(nums, target):
    result = []

    def backtrack(path, balance, index):
        if balance == 0:
            result.append(path.copy())
            return

        if balance < 0:
            return

        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(path, balance - nums[i], i)
            path.pop()

    backtrack([], target, 0)
    return result


if __name__ == '__main__':
    nums = [2, 3, 6, 7]
    target = 7
    print(combination_sum(nums, target))
