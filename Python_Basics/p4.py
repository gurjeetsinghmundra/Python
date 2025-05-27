# marks=int(input("Enter Total Marks: "))

# if marks>=35:
#     print("Passed")
# else:
#     print("Failed")

bp=int(input("Enter Buying Price: "))
sp=int(input("Enter Selling Price: "))

if bp>sp:
    print("Loss of ",bp-sp)
else:
    print("Profit of ",sp-bp)