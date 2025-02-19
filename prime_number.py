a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
a_int = int(a)
b_int = int(b)

def judge (n):
    if a_int < 1 or b_int < 1:
        print("0以上の値を入力してください。")
        exit(1)
    elif isinstance(a_int, float) or isinstance(b_int, float):
        print("正の数を入力してください。")
        exit(1)
    if n < 2 :
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

result_a = judge(a_int)
result_b = judge(b_int)

def output (n):
    if n:
        print("素数です。")
    else:
        print("素数ではありません。")

output(result_a)    
output(result_b)

