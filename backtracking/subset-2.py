def generateSubset(num):
    num.sort()
    result = []

    def backtrack(path, index):
        if index == len(num):
            result.append(path.copy())
            return

        path.append(num[index])
        backtrack(path, index + 1)
        path.pop()

        next_index = index+1
        while next_index < len(num) and num[next_index] == num[index]:
            next_index+=1

        backtrack(path, next_index)

    backtrack([], 0)

    return result


if __name__ == "__main__":
    nums = [1, 2, 2]
    print(generateSubset(nums))
