print("\n=======Bem vindo ao cálculo rápido de média da Fatec=======\n")

n1 = float(input("Digite aqui a sua nota de N1: "))
n2 = float(input("Digite aqui a sua nota de N2: "))

def calcular_media(n1, n2):
    return ((n1 * 0.4) + (n2 * 0.6)) / (0.4 + 0.6)
    
media = calcular_media(n1,n2)

if media >= 6:
    print(f"Sua média é: {media:.2f}, parabéns, você foi aprovado")

elif media <6:
    print("\nSua média infelizmente é menor que 6, você precisará fazer a N3")
    confirmacao = input("Já realizou a sua prova? (S/N): ")

    if confirmacao == "N":
        print("Volte depois que tiver sua pontuação de N3. Boa sorte na prova")
    elif confirmacao == "S":
       
        n3 = float(input("\nDigite aqui a sua nota de N3: "))
       
        if n1 < n2:
            n1 = max(n1, n3)
        else:
            n2 = max(n2, n3)

        media = calcular_media(n1, n2)

        print(f"\nApós a N3, sua média final é: {media:.2f}. {'Parabéns, você foi Aprovado\n' if media >= 6 else 'Infelizmente, você foi Reprovado\n'}")
