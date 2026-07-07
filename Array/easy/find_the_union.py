# Find the union of two sorted arrays
# Created by santosh

from collections import OrderedDict


class Solution:
    def union_by_map(self, m: list[int], n: list[int]) -> list[int]:
        freq: dict[int, int] = {}
        for el in m:
            freq[el] = freq.get(el, 0) + 1
        for el in n:
            freq[el] = freq.get(el, 0) + 1
        return sorted(freq.keys())

    def union_by_set(self, m: list[int], n: list[int]) -> list[int]:
        res = set(m) | set(n)
        return sorted(res)

    def union_by_2_pointers(self, arr1: list[int], arr2: list[int]) -> list[int]:
        union: list[int] = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if not union or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j += 1
            else:
                union.append(arr1[i])
                i += 1
                j += 1

        while i < len(arr1):
            union.append(arr1[i])
            i += 1
        while j < len(arr2):
            union.append(arr2[j])
            j += 1

        return union


if __name__ == "__main__":
    m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = [2, 3, 4, 4, 5, 11, 12]

    s = Solution()
    print("Union by map:", s.union_by_map(m, n))
    print("Union by set:", s.union_by_set(m, n))
    print("Union by 2 pointers:", s.union_by_2_pointers(m, n))

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
