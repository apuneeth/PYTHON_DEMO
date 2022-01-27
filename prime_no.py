x=int(input("Enter The Range..."))
for i in range(1,x+1):
    for j in range(2,i+1):
        if i!=j:
            if i%j==0:
                break
    else:
        print(i)