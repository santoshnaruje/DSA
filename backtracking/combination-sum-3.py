def combination_sum(n, k):
    result = []

    def backtrack(path, balance, index):
        if balance == 0 and len(path) == k:
            result.append(path.copy())
            return

        if balance < 0 or len(path) > k:
            return

        for i in range(index, 10):
            path.append(i)
            backtrack(path, balance - i, i+1)
            path.pop()

    backtrack([], n, 1)
    return result


if __name__ == '__main__':
    n = 9
    k = 3
    print(combination_sum(n,k))

# Remember NcR formula = N! / (N-R)! * R!

# | Part                                 |             Complexity |
# | ------------------------------------ | ---------------------: |
# | Backtracking                         |       `O(C(9,k) × k)` |
# | Copying results                      |       `O(C(9,k) × k)` |
# | **Time**                             | **`O(C(9,k) × k)`** |
# | Recursion stack                      |                  `O(k)` |
# | Output/result                        |       `O(C(9,k) × k)` |
# | **Space including output**           | **`O(C(9,k) × k)`** |
# | **Auxiliary space excluding output** |                **`O(k)`** |