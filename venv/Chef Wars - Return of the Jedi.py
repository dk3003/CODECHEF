try:
    t = int(input())

    for i in range(t):
        h, p = map(int, input().split())
        l = []
        while h != 0:

            h = h - p

            p = p // 2

            if h <= 0:
                print("1")
                break
            elif p <= 0:
                print("0")
                break

except:
    Exception



