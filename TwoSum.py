def twoSum(target, nums):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):    #Bir sayıyı birden fazla 
                   if nums[i] + nums[j] == target: #kullanmasını engellemek için 
                       return [i, j]               #aralığı i+1 den başlatıyoruz
