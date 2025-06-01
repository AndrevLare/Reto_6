def main():
    try:
        # Guarda el input, lo vuelve lista y mapea cada elemento para volverlo un int
        lista = list(map(int, input("ingrese una lista de numeros enteros\n").split()))

        # Lista con todas las sumas de un numero de la lista y su anterior en ella
        sumas = []

        # Se recorre la lista
        for i , e in enumerate(lista):
            # Ignora el primer elemento para evitar exepción por estar fuera de rango
            if i == 0: continue

            # Suma i y su anterior en la lista y añade el resultado a "sumas"
            sumas.append(e + lista[i-1])

        # Busca e imprime el mayor número de las sumas
        print(max(sumas))
    except ValueError:
        print("Entrada invalida, por favor ingrese solo numeros enteros.")
        return main()
    
# Entrada del programa
if __name__ == "__main__":
    main()