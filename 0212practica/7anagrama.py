def son_anagramas(palabra1, palabra2):
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    
   
    return sorted(palabra1) == sorted(palabra2)


palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

if son_anagramas(palabra1, palabra2):
    print("Las palabras son anagramas.")
else:
    print("Las palabras NO son anagramas.")
