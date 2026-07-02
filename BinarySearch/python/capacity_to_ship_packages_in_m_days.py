class Solution:
    def capacity(self, capacity, days):

        def check_does_all_packages_ship(capacity, mid):
            used_days = 1
            current_count = 0
            for capacity_package in capacity:
                if current_count + capacity_package <= mid:
                    current_count += capacity_package
                else:
                    used_days += 1
                    current_count = capacity_package

                if used_days > days:
                    return False
            return True

        low = max(capacity)
        high = sum(capacity)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if check_does_all_packages_ship(capacity, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


if __name__ == "__main__":
    capacity = [5, 4, 5, 2, 3, 4, 5, 6]
    days = 5
    solution = Solution()
    print(solution.capacity(capacity, days))
