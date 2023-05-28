from math import factorial
op = 0
n = int(input("Digite um número: "))
while op != 3:
    print()
    print("""[1] Fatorial
[2] Novos Valores
[3] Encerrar Programa""")
    print()
    op = int(input("Digite sua opção: "))
    if op == 1:
        fatorial = factorial(n)
        print()
        print("O fatorial do número ({}) é = {}".format(n,fatorial))
    elif op == 2:
        print()
        n = int(input("Digite um número: "))
print("Programa encerrado!")
    
    