a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a_int = int(a)
b_int = int(b)

def gcd (x, y):
    while y != 0:  
        c = x % y
        x = y
        y = c
    if x == 1:
        return True
    else:
        return False
        
result = gcd(a_int, b_int)

def judge (z):
    if z == True :
        print("互いに素です。")
    else:
        print("互いに素ではありません。")

judge(result)