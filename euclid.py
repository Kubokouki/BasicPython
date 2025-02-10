a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
a_int = int(a)
b_int = int(b)

while b_int != 0:  # bが0になるまでループ
    c = a_int % b_int
    a_int = b_int
    b_int = c

print("最大公約数は" + str(a_int) + "です。")