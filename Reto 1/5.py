# Se importa la función Counter, que retorna un diccionario que informa sobre 
# la cantidad de apariciones q tiene un elemento en una lista
from collections import Counter

def main():
    # Guarda el input como lista
    lista = list(map(lambda x : x.lower() , (input("ingrese una lista de palabras\n").split())))

    # Se guardan las palabras que cumplan a un resultado en un conjunto, esto
    # para que se ignoren automaticamente palabras duplicadas y las cuente como
    # una sola
    resultado = set()

    # Se recorre la lista de palabras
    for i, str in enumerate(lista):
        caracteres = []
        # Guarda los carácteres de str en la lista "caracteres"
        for chr in str: caracteres.append(chr)
        
        # Se recorre la misma lista de palabras
        for j, str_j in enumerate(lista):
            # Ignora el caso en el q una palabra se conpare con si misma
            if i == j: continue
            
            caracteres_2 = []
            # Guarda los carácteres del segundo string en la lista "caracteres_2"
            for chr in str_j: caracteres_2.append(chr)
            
            # Compara la cantidad de apariciones de los carácteres de ambos
            # strings, si los mismos caracteres aparecen la misma cantidad de 
            # veces, entonces son anagramas entre sí los strings
            if Counter(caracteres) == Counter(caracteres_2): resultado.update([str, str_j])
            
    # Imprime el resultado
    print(list(resultado))
    
# Entrada del programa
if __name__ == "__main__":
    main()