list_ = [13, 9, 8, 4, 2, 2, 1]

def selectLocation(nums, targer, mid):
    if nums[mid] == targer:
        if mid-1 >= 0 and nums[mid-1] == targer:
            pass

def binarySearch(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f'Low: {low}, High: {high}, Mid: {mid}, Mid Value: {nums[mid]}, Target Matched: {nums[mid]==target}')
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            low = mid + 1
        if nums[mid] < target:
            high = mid - 1

    return -1

print(binarySearch(list_, 13))