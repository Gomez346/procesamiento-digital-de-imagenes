n = int(input("ingrese un numero: "))
x = 1  
c = 0
while x <= n:
    if n % x == 0:
        c = c + 1
    x = x + 1
if c == 2:
    print("el número ingresado es primo", n)
else:
        print("el número ingresado no es primo", n)