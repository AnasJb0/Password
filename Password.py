def NbCMin(p):
    n = 0
    for i in range(len(p)):
        if ord("a") <= ord(p[i]) <= ord("z"):
            n = n + 1
    return n

def NbCMaj(p):
    j = 0
    for i in range(len(p)):
        if ord("A") <= ord(p[i]) <= ord("Z"):
            j += 1
    return j

def NbCAlpha(p):
    a = 0
    for i in range(len(p)):
        if ord("A") <= ord(p[i]) <= ord("Z") or ord("a") <= ord(p[i]) <= ord("z"):
            g = 0
        else:
            a += 1
    return a

def LongMaj(p):
    o = 0
    k = 0
    for i in range(len(p)):
        if ord("A") <= ord(p[i]) <= ord("Z"):
            o += 1
        else:
            o = 0
        if k < o:
            k = o
    return k

def LongMin(p):
    t = 0
    y = 0
    for i in range(len(p)):
        if ord("a") <= ord(p[i]) <= ord("z"):
            t += 1
        else:
            t = 0
        if y < t:
            y = t
    return y

def score(p):
    s = len(p) * 4 + (len(p) - NbCMin(p)) * 3 + (len(p) - NbCMaj(p)) * 2 + NbCAlpha(p) * 5 - LongMin(p) * 2 - LongMaj(p) * 2
    return s

p = input("Type password: ")
s = score(p)
if s < 20:
    print("Very Weak")
elif 20 <= s < 40:
    print("Weak")
elif 40 <= s < 80:
    print("Strong")
else:
    print("Very Strong")