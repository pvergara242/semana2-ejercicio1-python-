def leer_frase():
    try:
       return input("ingresa una frase o texto: ")
    except ValueError as e:
        print('Error:', e)


def anagrama(palabra1, palabra2):
    if len(palabra1) !=len(palabra2): #1
     return "no" #1
    for j in palabra1 : #n
        try:
            palabra2.index(j) #n
        except:
           return "no" #1

    return "si" #1

valor1 = leer_frase()
valor2 = leer_frase()
valor3 = anagrama(valor1, valor2)
print("la" + valor1, "y la" + valor2, "son anagrama" + valor3) #1

# 2 + (n2 + 1) + 2
# la complejidad del big-o es n2
