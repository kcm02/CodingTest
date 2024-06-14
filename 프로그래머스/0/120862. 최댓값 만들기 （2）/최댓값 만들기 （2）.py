def solution(numbers):
    nums = sorted(numbers)
    return max(nums[-1] * nums[-2], nums[0] * nums[1])