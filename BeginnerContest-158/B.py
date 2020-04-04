N, a, b = map(int, input().split())

all = a + b

# a = 0
if a == 0:
    print(0)
    exit(0)

if N <= a:
    print(N)
    exit(0)

# a > 0
c = round(N / all)
d = N % all

roundCnt = a * c

if d <= a :
    amariCnt = d
else:
    amariCnt = a

print(roundCnt + amariCnt)


#a = 0 print 0
#a > 0
# N <= a print N
# N > a
#  N/(a+b)=c     が割り切れる  a * c
#  N/(a+b)=c...d が余りが出る  a * c
#    d <= a のとき a * c + d
#    d >  a のとき a * c + a
#
