n = int(input())
numbers = list(map(int, input().split()))
reversed_num = []

for num in range(len(numbers)-1, -1, -1):
  reversed_num.append(numbers[num])


print(*reversed_num)
