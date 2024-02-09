i = 1 #1
while i < 6:
 print(i) 
 i += 1

 i = 1 #2
while i < 6:
  if i == 3:
    break
i += 1

i = 0  #3
while i < 6:
  i += 1
  if i == 3:
    continue
print(i)

i = 1 #4
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")