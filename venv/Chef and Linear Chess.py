try:
    t=int(input())
    for i in range(t):
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        l = []
        for i in arr:
            if k%i==0:
                l.append(i)
            l.sort(reverse=True)
        if len(l)==0:
            print(-1)
            continue
        else:
            print(l[0])
except:
    Exception