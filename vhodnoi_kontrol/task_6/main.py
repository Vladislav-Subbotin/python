a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in range(0, len(a)):
  b.append(a[i])
  if b.count(a[i]) > 1 and c.count(a[i]) == 0:
    c.append(a[i])
print(c)