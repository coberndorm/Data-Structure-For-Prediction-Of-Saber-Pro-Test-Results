
def sumaGrupo (start, nums, target):
    if (start >= len(nums)):
        return target==0
    return sumaGrupo (start+1,nums,target - nums[start]) or sumaGrupo(start+1,nums,target)


print (sumaGrupo (0, [2,4,6], 10))