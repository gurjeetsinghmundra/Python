l1=["A","B","C","D","E","F"]
for i in l1:
    print(l1[1:3])

# l1[1:5] this is called slicing


# the below is called step
print(l1[::3]) #[::3] means 0 + 3 + 3 

print(l1[::-1])
# will give reverse list

l2=[12,34,345,43,23,43,100,200,500,0,-1,-10,0]

for i in l2:
    if i>100:print(i)

count=0;

for i in l2:
    if i%2==0:
        count=count+1
print(count)

pos=0;
neg=0;
z=0

for i in l2:
    if i>0:
        pos+=1
    elif i==0:
        z=z+1;
    else:
        neg=neg+1
print("Positive ",pos)
print("Negative ",neg)
print("Zero ", z)


# 

fruits=["mango","banana","chickoo"]
fruits[1]="apple"
print(fruits)

fruits.insert(1,"banana")
fruits.append("A")
print(fruits)

# append means element will be added at the last



