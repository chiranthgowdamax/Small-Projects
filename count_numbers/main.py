def count_numbers(nums):
  positive = 0
  negative = 0
  zero = 0
  
  for num in nums:
    if num > 0:
      positive += 1
    elif num < 0:
      negative += 1
    else:
      zero += 1
  return positive, negative, zero

n = int(input("Enter a number to allocate memory: "))
numbers = list(map(int,input("Enter numbers according to number of memory allocated: ").split(",")))

pos,neg,zero = count_numbers(numbers)
print(f"Positives = {pos}")
print(f"Negatives = {neg}")
print(f"Zeros = {zero}")
