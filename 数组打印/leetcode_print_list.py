## 输入nums数组，输出长度为n
nums = [0, 1, 1, 2, 2, 4, 4, 6, 7]
n = input("n=>")
n = int(n)

## count是输出的长度为n
count = n
## num等于输入数组的第一个数，比如为0
num = nums[0]

	## 因为num已经等于了数组第一个元素了，所以计数要大于0+1 = 1

for i in range(1,len(nums)):
	if(count > 1):
		if(num == nums[i]):		## 如果num 等于num[i] i从1开始跳过0
							## 这两句就是把 剩下的数组全部向前移一位
			for j in range(i,len(nums)-1):
				nums[j] = nums[j+1]
			#nums.pop[i]
		else:			##	如果num不重复，那么num就等于新的nums[i]，然后计数-1，
			num = nums[i]
			count -= 1
	else:
		break

print(n,"nums =",nums)