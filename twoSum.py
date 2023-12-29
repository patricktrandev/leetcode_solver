nums_list= [2,7,11,15]
target_test=9

def solveTwoSum(nums, target):
    seen={}
    i=0
    while i<len(nums_list):

        num= nums[i]
        remaining= target-num
        if remaining in seen:
            return [i, seen[remaining]]
        seen[num]=i
        i+=1


test= solveTwoSum(nums_list, target_test)
print(test)