num=int(input())
for i in range(1,num):
    if i%2!=0:
        for j in range(1,i+1):
                print(j,end=",")
    else:
        for j in range(1,i+1):
                print(i,end=",")
                i=i-1
    print("\t")
for i in range(num,1,-1):
    if i%2==0:
        for j in range(i,0,-1):
                print(j,end=",")
    else:
        for j in range(1,i+1):
                print(j,end=",")
            
    print("\t")