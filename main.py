#Loops

list1 = ['apples', 'bananas', 'oranges']
tup1 = (2,6,10)
for item in list1:
  print(item)
for i in range(0,11):
  print(i)
for i in range(0,11,2):
  print(i)
for z in range(2,51,5):
  print(z)

#nested loops
for i in range(0,5):
  for j in range(0,3):
    print(i * j)