def main(str:str)->bool:
    # Inicia el booleano en true, ya que la logica del programa ve q sea 
    # palindromo, sino q no lo sea y en ese caso, descartarlo
    palindrome = True
    # Recorro el string obteniendo el indice y el caracter
    for i, chr in enumerate(str):
        # Evalua el elemento X con su elemento "espejo" y se ve si son iguales
        evaluation_case = chr == str[-i-1]
    
        # Se verifica q todas las palabras hasta el momento cumplan lo que se
        # espera de un palindromo, si se incumple y hay un false, ya no es 
        # palindromo y se mantiene asi hasta el final del for
        palindrome = palindrome and evaluation_case
    return palindrome

# Entrada del programa, recibe el input e imprime el resultado de la funcion
# main evaluada en string
if __name__ == "__main__":
    string = input()
    print(string, "es un palindromo" if main(string) else "no es un palindromo")