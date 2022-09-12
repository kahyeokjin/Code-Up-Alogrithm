def prove(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True
def solution(nums):
    answer=0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1,len(nums)):
                if prove(nums[i]+nums[j]+nums[k])>0:
                    answer+=1
    return answer
                
