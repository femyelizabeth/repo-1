l1=list(map(int,input("Enter 1st arr:").split(',')))
l2=list(map(int,input("Enter 2nd arr:").split(',')))
m=len(l1)
n=len(l2)
i=j=0
l3=[]
for k in range(m+n):
    if(i<m and j<n):
        if(l1[i]>=l2[j]):
            l3.append(l2[j])
            j+=1
        else:
            l3.append(l1[i])
            i+=1
    elif(i<m):
        l3.append(l1[i])
        i+=1
    else:
        l3.append(l2[i])
        j+=1
print("Merged sorted array:")
for i in range(0,m+n):
    print(l3[i],"\n")
