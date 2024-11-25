# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# print(l1+l2[::-1])

l1 = [1,2,2,2,2,3,4,5,5]
l2 = []

for a in l1:
  if a not in l2:
    l2.append(a)
print(l1)
print(l2)