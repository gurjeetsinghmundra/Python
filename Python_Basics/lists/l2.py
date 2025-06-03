# even odd using append

l3=[12,34,23,45,46,37]
even=[]
odd=[]

for i in l3:
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
print(l3)
print(even,len(even))
print(odd,len(odd))

# remove, pop
l4=["A","B","C","D","E","F"]
l4.remove("B")
l4.pop()
l4.pop(2)

print(l4)

#sort
l5=[34,43,12,1,345,3243,234]
l5.sort()
print(l5)
l5.sort(reverse=True)
print(l5)

# copy

l1=[1,23,43]
l2=l1.copy()

print(l1)
l1.pop()
print(l1)
print(l2)

# if we write l2=l1 directly then changes in l1 will be reflected in l2
# but when using copy, changes in l1 will not affect l2