def largest_num(number):
  largest = number[0]
  for num in number:
    if num > largest:
     largest = num
  return largest
  
n = int(input("Enter a limit of number: "))
number = list(map(int, input("Enter numbers in the list: ").split()))
large = largest_num(number)
print(f"The largest number: {large}")
