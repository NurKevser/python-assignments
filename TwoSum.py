def twoSum(target, nums):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):    #Bir sayıyı birden fazla 
                   if nums[i] + nums[j] == target: #kullanmasını engellemek için 
                       return [i, j]               #aralığı i+1 den başlatıyoruz



                  WİTH LIST COMPHERENSION

nums = [8,2,4,7,1,5,6,9]
target = 16
[(i,j) for i in range(len(nums)) for j in range(i+1, len(nums)) \
 if nums[i]+nums[j] == target]                
