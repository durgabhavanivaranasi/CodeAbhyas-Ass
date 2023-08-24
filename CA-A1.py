a={}
d=[1,2,2,1,2,3,1,2,3]
for i in d:
    if i not in a:
        a[i]=1
    elif i in a:
        a[i]+=1
max1=a[1]
min1=a[1]
for i in d:
    if a[i]>max1:
        max1=a[i]
    elif a[i]<min1:
        min1=a[i]
print(a)
print(max1)
print(min1)
