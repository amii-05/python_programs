listtwo=[5,1,4,9,3,0,2,6,8,7,98,2005]
find=2005
found=False
for i in range(len(listtwo)):
    if listtwo[i]==find:
        found=True
        break
if found:
    print("Found")
else:
    print("Not found")