print("\nBem vindo ao hortifruti RODRIGUES !\n")
print("Iniciando a caixa...\n")


saldo_dia =[]

def escolha_caixa():
    while True:
        print("Escolha a operação:\n 1-Vendas\n 2-Saldo do Dia\n 3-SAIR\n")
        esc = input("Digite a opção escolhida: \n")
        if esc =="1":
            vendas()

        elif esc == "2":
            total_vendas()
            
        elif esc == "3":
            print("Saindo...")
            break
        else:
            print("\nOpção invalida\n")

def vendas(): 
    "fazer uma função para somar todos os valores inseridos"
    valores =[]
    while True:
        print("insira o valor do produto ou dgite (0) para finalizar a compra")
        valor = float(input("R$: "))
        i = valor
        valores.append(valor)
        
        if i == 0:
            x = sum(valores)
            print("\nO valor da sua compra é de: R$", x,"\n")
            saldo_dia.append(x)
            break
        else:
            print("insira o valor do produto ou dgite (0) para finalizar a compra")
            valor = float(input("R$: "))
            i = valor
            valores.append(valor)
            if i == 0:
                x = sum(valores)
                print("\nO valor da sua compra é de: R$", x,"\n")
                saldo_dia.append(x)
                break
    forma_pgto()
        
'''if i != 0:
            print("insira o valor do produto")
            valor = float(input("R$: "))
            i = valor
            valores.append(valor)
            if i == 0:
                x = sum(valores)
                print("\nO valor da sua compra é de: R$", x,"\n")
                saldo_dia.append(x)
                break'''

''' if i == 0:
            x = sum(valores)
            print("\nO valor da sua compra é de: R$", x,"\n")
            saldo_dia.append(x)
            break
        
        else:
            print("insira o valor do produto")
            valor = float(input("R$: "))
            i = valor
            if i ==0: 
                break
            else: 
                valores.append(valor)'''

def total_vendas():
    print("\n--------------------\n O Total de vendas do dia foi: \n")
    total = sum(saldo_dia)
    return print(total,"\n--------------------\n")


def forma_pgto():
    while True:
        print("Informe a forma de pagamento desejada:\n 1- Deinheiro\n 2- Cartão\n")
        opcao = input("Digite a opção escohida: ")
        if opcao == "1":
            print("\nInforme o valor para o calculo do troco:")
            dinheiro = float(input("R$: "))
            valor = saldo_dia[-1]
            troco = dinheiro - valor
            print("\nO troco é: R$", troco)
            break
        elif opcao == "2":
            print("Compra Aprovada")
            break
        else:
            print("Opção invalida")
               
escolha_caixa()