from math import sin,pi,exp,sqrt
# --example--
# print(sin(0))
# >>> 0
# -----------
def calculation (f ,a = 0 ,b = 1,n = 100):
    s = 0
    i = 0
    h = (b - a)/n 
    for i in range( n + 1 ):
        if i != 0:
            x1 = a + (i - 1) * h
            x2 = a + i * h
            s += (h/2) * (f(x1) + f(x2))
    return s

def f(x):
    return sin(x)

def g(x):
    return 4/(1 + x**2)

def k(x):
    return sqrt(pi) * exp(-x**2)

print( "(1):" +str(calculation(f, 0, pi/2, 50)))

print( "(2):" +str(calculation(g, 0, 1, 100)))

print( "(3):" +str(calculation(k, -100, 100, 1000)))


