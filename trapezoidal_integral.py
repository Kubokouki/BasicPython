from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
s = 0
i = 0
h = (1/2)*3.141592/100 
for i in range(101):
    if i != 0:
        s = s + (h/2*(sin((i-1)*h)+sin(i*h)))
print("面積は"+ str(s) + "です。")
