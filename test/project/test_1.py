import time
s = 0
a = [10]
while(s != 5):
  a.append(s)
  s = s+1
  print(s)
  time.sleep(1)

print(a)
print(len(a))