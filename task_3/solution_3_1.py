a = input('enter string: ')
#n это алфавит
n = ''
#для каждого символа из а выполняется проверка, если его не находит в алфавите, тот символ присоединяется к нему
for i in a:
   if i not in n and i!='': n+=i
print(n)
