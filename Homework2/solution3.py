nums = [1, 2, 3, 4]
runningSum = []

s = 0
for i in nums:
    s += i
    runningSum.append(s)

print(runningSum)
