class Solution:
    def merge(self, nums1, nums2, m, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        return nums1


if __name__ == '__main__':
    nums1 = [0]
    nums2 = [1]
    m = 0
    n = 1
    solution = Solution()
    print(solution.merge(nums1, nums2, m, n))
