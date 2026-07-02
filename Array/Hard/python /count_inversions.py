class Solution:
    def countInversionBruteForce(self, nums):

        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    count += 1

        return count

    def merge(self, nums, low, mid, high):

        temp = []
        left = low
        right = mid + 1
        count = 0

        while left <= mid and right <= high:
            if nums[left] < nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                count += (mid - left + 1)
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1

        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(low, high + 1):
            nums[i] = temp[i - low]

        return count

    def mergeSort(self, nums, low, high, ):
        if low >= high:
            return 0
        count = 0
        mid = (low + high) // 2
        count +=self.mergeSort(nums, low, mid  )
        count +=self.mergeSort(nums, mid + 1, high )
        count +=self.merge(nums, low, mid, high  )
        return count

    def countInversionOptimal(self, nums):

        low = 0
        high = len(nums) - 1
        count = self.mergeSort(nums, low, high)

        return count


if __name__ == '__main__':
    s = Solution()
    nums = [5, 4, 3, 2, 1]
    # nums = [1, 2, 3, 4, 5]
    # result = s.countInversionBruteForce(nums)
    result=s.countInversionOptimal(nums)
    print(result)
