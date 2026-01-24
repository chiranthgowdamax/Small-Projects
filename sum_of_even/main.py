def sum_even(n):
  if n<= 1:
   return 0
  
  total = 0
  for i in range(2, n+1, 2):
    total += i
  return total

n = int(input("Enter a number: "))
print(sum_even(n))
