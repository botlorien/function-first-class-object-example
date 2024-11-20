if __name__=='__main__':
    # Criando um lista de frutas
    fruits = 'strawberry fig apple cherry raspberry banana'.split()
    
    # Examplo de uma higher-order function que recebe uma function como argumento do parametro key
    print(f'sorted: {sorted(fruits,key=len)}')

    # Criando uma outra fuction para ser usada como argumento de key
    def reverse(word):
        return word[::-1]
    
    # Testando o resultado da function
    print(f'reverse: {reverse('testing')}')

    # Imprimindo o resultado da function criada e passada como argumento
    print(f'sorted: {sorted(fruits,key=reverse)}')

    # Usando lambda (função anonima)
    print(f'sorted: {sorted(fruits,key=lambda word:word[::-1])}')