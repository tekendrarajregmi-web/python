nums = [5,14,9,15,20]

def sort(nums, lows, high):
    pivot = nums[lows]
    i, j = lows, high

    while i < j:
        while i <= high - 1 and nums[i] <= pivot:
            i += 1

        while j >= lows + 1 and nums[j] >= pivot:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[lows], nums[j] = nums[j], nums[lows]
    return j

def q_sort(nums, low, high):
    if low < high:
        p_index = sort(nums, low, high)
        q_sort(nums, low, p_index - 1)
        q_sort(nums, p_index + 1, high)

q_sort(nums, 0, len(nums) - 1)

print(nums)
