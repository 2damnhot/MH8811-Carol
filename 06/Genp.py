import random
a = 'ABCDRYUHSIJDFGHIROJGKFDNBJKX'
b = 'abcdefgasiurohdoojcviosuoe'
c = '1234567890'
d = '!@#$%^&*)(_*&^%)'

if __name__ == "__main__":
    def genPassword(n):
        code = ''
        for i in a:
            index = random.randint(0,len(a)-1)
            code += a[index]*(int(n/4))
        for i in b:
            index = random.randint(0,len(b)-1)
            code += b[index]*(int(n/4))
        for i in c:
            index = random.randint(0,len(c)-1)
            code += c[index]*(int(n/4))
        for i in d:
            index = random.randint(0,len(d)-1)
            code += d[index]*(int(n/4))
            s=''.join(random.sample(code,k=n))
        return s
    print(genPassword(12))

if __name__ != "__main__":
    def genPassword(n):
        code = ''
        for i in a:
            index = random.randint(0,len(a)-1)
            code += a[index]*(int(n/4))
        for i in b:
            index = random.randint(0,len(b)-1)
            code += b[index]*(int(n/4))
        for i in c:
            index = random.randint(0,len(c)-1)
            code += c[index]*(int(n/4))
        for i in d:
            index = random.randint(0,len(d)-1)
            code += d[index]*(int(n/4))
            s=''.join(random.sample(code,k=n))
        return s




