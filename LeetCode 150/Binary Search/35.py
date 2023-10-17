def search_insert_position(nums, target, low=0, high=None):
    if high is None:
        high = len(nums) - 1

    if low > high:
        return low

    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return search_insert_position(nums, target, mid + 1, high)
    else:
        return search_insert_position(nums, target, low, mid - 1)

# Example usages:
nums1, target1 = [1,3,5,6], 5
print(search_insert_position(nums1, target1))  # Output: 2

nums2, target2 = [1,3,5,6], 2
print(search_insert_position(nums2, target2))  # Output: 1

nums3, target3 = [1,3,5,6], 7
print(search_insert_position(nums3, target3))  # Output: 4
