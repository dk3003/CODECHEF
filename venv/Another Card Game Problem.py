testcases=int(input())
for i in range(testcases):
    arr = list(map(int,input().split()))
    q1=arr[0]//9
    r1=arr[0]%9
    q2=arr[1]//9
    r2=arr[1]%9
    if r1==0:
        res1=q1
    else:
        res1=q1+1
    if r2==0:
        res2=q2
    else:
        res2=q2+1
    if res1==res2:
        print(1,res2)
    elif res1<res2 :
        print(0,res1)
    else:
        print(1,res2)