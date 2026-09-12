def generateSubset(num):
    result = []

    def backtrack(path, index):
        if index == len(num):
            result.append(path.copy())
            return

        path.append(num[index])
        backtrack(path, index + 1)
        path.pop()
        backtrack(path, index+1)


    backtrack([], 0)

    return result


if __name__ == "__main__":
    num = [1,2,2]
    print(generateSubset(num))


# Time Complexity: \(\mathcal{O}(2^n \cdot n)\) because there are \(2^{n}\) total subsets, and copying each subset takes \(\mathcal{O}(n)\) time
# Space Complexity: \(\mathcal{O}(n)\) for the recursion stack depth and the current path storage (excluding the output list).