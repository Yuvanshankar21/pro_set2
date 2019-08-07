n = int(input())
add=0
t=n
while t>0:
  dig=t%10
  add+=dig**2
  t//=10
print(add)
