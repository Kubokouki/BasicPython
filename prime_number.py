a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
a_int = int(a)
b_int = int(b)

if a_int < 2 :
   print("素数ではありません。")
if a_int == 2:
    print("素数です。")
if a_int % 2 == 0:
    print("素数ではありません。")  
    
i = 3
while i * i <= a_int:
    if a_int % i == 0:
        print("素数ではありません。")
    i += 2
print("素数です。")

if b_int < 2 :
   print("素数ではありません。")
if b_int == 2:
    print("素数です。")
if b_int % 2 == 0:
    print("素数ではありません。")  
else:
    i = 3
    while i * i <= b_int:
        if b_int % i == 0:
            print("素数ではありません。")
        break
        i += 2
    else:
        print("素数です。")