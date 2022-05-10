## calc bits de xarxa

numero = int(input("Digam un numero: "))

if numero < 2:
    print("Els bits necesaris son 1")
elif numero < 4:
    print("Els bits necesaris son 2")
elif numero < 8:
    print("Els bits necesaris son 3")
elif numero < 16:
    print("Els bits necesaris son 4")
elif numero < 32:
    print("Els bits necesaris son 5")
elif numero < 64:
    print("Els bits necesaris son 6")
    
    
## calc operadors

n1 = int(input("Diguem el primer numero: "))
n2 = int(input("Diguem el segon numero: "))
op = input("Que vols fer? Pots sumar, restar, dividir o multiplicar")

if op == "+":
    print("n1 + n2")
elif op == "-":
    print("n1 - n2")
elif op == "*":
    print("n1 * n2")
elif op == "/":
    print("n1 / n2")
else:
    print("No correcte")
    
    
## calc operadors - extras

if op == "//":
    print("n1 // n2")
elif op == "%":
    print("n1 % n2")
