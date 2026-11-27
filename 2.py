ma=1000000
n=int(input())
for i in range(1,n+1):
    a=n**2-15*n
    if a<ma:
        ma=a
print(ma)
