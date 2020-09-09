
def isodd(n):
    if n%2!=0:
        print("Werid")
    else:
        if n in range(2,5):
            print("not weird")
        elif n in range(6,20):
            print("weird")
        else:
            print("not weird")
    return

print(isodd(10))