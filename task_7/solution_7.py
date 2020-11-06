a = input()
c = len(a)
c = c//2
for i in range(c):
   if a[i] != a[-1-i]:
      is_palindrom=False
      print(is_palindrom)
      quit()
is_palindrom=True
print(is_palindrom)
