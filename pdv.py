compras = []
descontos = []

while True:
    print("\n--- SISTEMA DE COMPRAS ---")
    print("1 - registrar compra")
    print("0 - fechar o sistema")

    print("\n")
    op = input("oque desejas fazer? ")

    if op == "1":
        while True:
            x = float(input("valor da compra: "))
            if x <= 0:
                print("\n")
                print("O valor não pode ser negativo ou nulo.")
                print("\n")
                continue
            break

        while True:
            y = int(input("idade do cliente: "))
            if y <= 0:
                print("\n")
                print("A idade não pode ser negativa ou nula.")
                print("\n")
                continue
            break

        compras.append(x)

        z = x

        if y >= 65:
            w = z * 0.20
            z = z - w
            descontos.append(w)
            

        if z > 100:
            w = z * 0.10
            z = z - w
                        
            descontos.append(w)
        
        print(f"valor da compra é: R${z:.2f}")

        
    elif op == "0":
        print("\n")
        print("fechando sistema...")
        print("\n")
        break

    else:
        print("\n")
        print("Opção invalida! escolha 1 ou 0")
        print("\n")

tt = sum(compras) - sum(descontos)

print("\n")
print("Quantidade de compras registradas:", len(compras))
print(f"Total bruto: R${sum(compras):.2f}")
print(f"Total de descontos concedidos: R${sum(descontos):.2f}")
print(f"Total final: R${tt:.2f}")

print("\n")
