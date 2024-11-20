from functools import reduce
from operator import add

if __name__=='__main__':
    # Criando um objeto do tipo function
    def factorial(n):
        """returns n!"""
        return 1 if n < 2 else n * factorial(n - 1)
    
    # Interando sobre um range de valores usando map
    print(list(map(factorial,range(6))))

    # Interando sobre o mesmo range de valores usando listcomps
    print([factorial(n) for n in range(6)])

    # Filtrando apenas os argumentos impar usando map e filter
    print(list(map(factorial,filter(lambda n: n % 2,range(6)))))

    # Filtrando apenas os argumentos impar usando listcomps com condicionais
    print([factorial(n) for n in range(6) if n % 2])

    # Obs: Observa-se que a escrita com listcomps é mais legivel

    # Usando reduce para somar os valores no range 100
    print(reduce(add,range(100)))

    # Usando sum para fazer o mesmo
    print(sum(range(100)))