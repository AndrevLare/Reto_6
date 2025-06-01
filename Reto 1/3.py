def main()->list:
    # guardo el input como lista separando los números por comas
    list = input("ingrese la lista de numeros separados por comas\n").split(",")
    
    # Variable que almacena el resultado
    output = []
    
    # Recorro la lista
    for e in list:
        # Supone q es primo al inicio y si no es lo descarta
        prime = True
        
        # Evalua desde el 2 hasta la mitad del numero, ya q despues de ahi,
        # no habria nada q pueda dividir al numero en cuestión
        try:
            for i in range(2, (int(e)//2)+1):
                # Mira si el numero no es divisible entre i, si lo es, entoces no
                # es primo
                prime = prime and int(e)%int(i) != 0
            
            # Si no es primo termina el ciclo
            if not(prime): break
        
            # Si el número es primo lo añade a la lista, y si es 1 lo desarta y si
            # es 2 lo añade, ya q estos dos números los ignora el for
            if (prime or int(e) == 2) and (int(e) > 1): output.append(e)
        except ValueError:
            print(f"Entrada invalida: '{e}'. Por favor ingrese solo numeros enteros.")
            return main()
    # Retorno de la respuesta
    return output

# Entrada del programa, ejecuta e imprime el resultado de main
if __name__ == "__main__":
    print(main())