with open("20-input.txt") as f:
    lines = f.read().strip().split('\n')


def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]
    return nums

def sol(p):
    KEY = 811589153
    coords = [1000, 2000, 3000]
    if p == 1:
        nums = list(enumerate(map(int, lines)))
        n = len(nums)
        og = nums.copy()

        for i, x in og:
            for index in range(n):
                if nums[index][0] == i:
                    break

            if x < 0:
                cur = index
                for _ in range(-x):
                    nums = swap(nums, cur, (cur - 1) % n)
                    cur = (cur - 1) % n
                continue

            cur = index
            for _ in range(x):
                nums = swap(nums, cur, (cur + 1) % n)
                cur = (cur + 1) % n

        p1 = 0
        for zero_index in range(n):
            if nums[zero_index][1] == 0:
                break
        for c in coords:
            p1 += nums[(zero_index + c) % n][1]
        return p1
    
    #part 2
    nums2 = list(map(int, lines))
    for i in range(len(nums2)):
        nums2[i] = (i, nums2[i] * KEY)
    n = len(nums2)
    og = nums2.copy()

    for _ in range(10):
        for i, x in og:
            for index in range(n):
                if nums2[index][0] == i:
                    break

            x %= (n - 1)

            if x > 0:
                cur = index
                for _ in range(x):
                    nums2 = swap(nums2, cur, (cur + 1) % n)
                    cur = (cur + 1) % n
    p2 = 0
    for zero_index in range(n):
        if nums2[zero_index][1] == 0:
            break
    for c in coords:
        p2 += nums2[(zero_index + c) % n][1]
    return p2
    
print(sol(1))
print(sol(2))