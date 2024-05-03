fruits = ["apple", "banana", "cherry"] #1
for x  in fruits:
    print(x)


fruits = ["apple", "banana", "cherry"] #2
for x in fruits:
  if x == "banana":
    continue
print(x)

for x in range(6): #3
   print(x)


fruits = ["apple", "banana", "cherry"] #4
for x in fruits:
  if x == "banana":
    break
print(x)
