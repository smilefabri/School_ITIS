"""



"""

def FindDuplicate(nums):
    hare = nums[0]
    tortoise = nums[0]

    while(True):
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
        
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1


print(FindDuplicate([5,3,4,4,5,6,4]))
