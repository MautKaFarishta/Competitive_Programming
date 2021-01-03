def checkPossibility(nums) -> bool:
        f=1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                f+=1
            if f>2:
                return False
        return True

print(checkPossibility([3,4,2,3]))