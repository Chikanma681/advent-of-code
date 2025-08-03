def increasing(nums):
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        if diff <= 0 or diff > 3:
            return False
    return True

def decreasing(nums):
    for i in range(1, len(nums)):
        diff = nums[i-1] - nums[i]
        if diff <= 0 or diff > 3:
            return False
    return True

def is_safe(nums):
    return increasing(nums) or decreasing(nums)

def part1():
    safe_count = 0
    with open('fileinput.txt') as f:
        for line in f:
            nums = list(map(int, line.split()))
            if is_safe(nums):
                safe_count += 1
    return safe_count

def part2():
    safe_count = 0
    with open('fileinput.txt') as f:
        for line in f:
            nums = list(map(int, line.split()))
            if is_safe(nums):
                safe_count += 1
            else:
                for i in range(len(nums)):
                    modified = nums[:i] + nums[i+1:]
                    if is_safe(modified):
                        safe_count += 1
                        break
    return safe_count

def solve():
    part1_result = part1()
    part2_result = part2()
    
    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    solve()
