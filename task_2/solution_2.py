a = input()
max = 0
result = ''
for i in a:
#включаем счетчик
  count = a.count(i)
  if count > max:
    max = count
    result = i
print(result)
