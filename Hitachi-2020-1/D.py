N, T= map(int, input().split())
T = T + 0.5

ab = []

class MyClass:
    def __init__(self, a, b): 
        self.a = a     
        self.b = b

    def calc(self, t):   
        #print("a: {}, b: {}".format(a,b))
        n = self.a * t + self.b
        return n

    def disp(self):
        print(self.a, self.b)

if __name__ == "__main__":

    for i in range(N):
        a, b = map(int, input().split())
        ab.append(MyClass(a, b))

    cnt = 0
    t = 0

    while True:
        t = t + 1
        T = T - 1

        tmp = 100000000

        for i in ab:
            if i.calc(t) < tmp:
                tmp = i.calc(t)
                tmp_i = i

        ab.remove(tmp_i)

        T = T - tmp
        if T < 0:
            break

        cnt = cnt + 1

        if len(ab) == 0:
            break
    print(cnt)

