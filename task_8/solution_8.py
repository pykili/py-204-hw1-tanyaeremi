n = int(input())
summ = 0
count = 0
for i in range(1, n+1):
  a = int(input('Число: '))
  summ += i
  count += 1
print(summ / count)
