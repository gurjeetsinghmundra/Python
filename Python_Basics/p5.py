for i in range(1,5):
    print(str(i)*i)

# for i in range(4,0,-1):
#     print(str(i)*i)


n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
        # print(str(j)*j)
    print()

print("=======================")

n=4
for i in range(1,n+1):
    if i%2==0:
        print(str(0)*i)
    else:
        print(str(1)*i)


print("=======================")

n=4
for i in range(1,n+1):
    if i%2==0:
        print("*"*i)
    else:
        print(str(i)*i)


''' 
 str will separately print value 
    ex:(1
        **
        333
        ****)

if we dont use str then 
1
**
9
****

''' 

print("=====================")

n=4 

for i in range(1,n+1):
    for j in range(1,i+1):
        if(j%2==0):
            print(0,end='')
        else:
            print(1,end='')
    print()