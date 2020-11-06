n = ''
for smth in 'a'*10:
  user_input = input('enter string: ')
  for i in user_input:
     if i not in n and i!='': n+=i
print(n)
