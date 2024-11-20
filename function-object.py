if __name__=='__main__':
    # Criando um objeto do tipo function
    def factorial(n):
        """returns n!"""
        return 1 if n < 2 else n * factorial(n - 1)
    
    # Imprimindo o resultado
    print(f'factorial(42): {factorial(42)}')

    # Imprimindo a docstring pelo metodo __doc__
    print(f'Docs: {factorial.__doc__}')

    # Do tipo function
    print(f'Type: {factorial}')

    # Atribuindo a referencia do objeto function a uma variavel
    fact = factorial

    # Chamando a variavel
    print(f'fact(5): {fact(5)}')

    # Passando o objeto function como parametro de outro objeto
    print(map(factorial,range(11)))

    # Criando uma lista com o resultado de map
    print(list(map(factorial,range(11))))
    