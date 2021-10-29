while True:
 print("---------------------------------")
 print("  Seja bem-vindo(a) ao MyBank    ")
 print("   SIMULADOR DE INVESTIMENTO     ")
 print("---------------------------------")

 print("Escolha um Titulo")
 print("1 - Pesouro Prefixado 2024")
 print("2 - Pesouro Prefixado 2026")

 Cliente = str(input("Digite o número do titulo ecolhido para fazer a simulação: "))

 if Cliente == '1':
     investimento = float(input("Quanto deseja investir?: "))
     mensalidade = float(input("Se você for investir todo mês, qual o valor?: "))
     aporte = 32
     TotalInvest = (mensalidade * aporte) + investimento
     Rentabilidade = TotalInvest / investimento - 1
     vbruto = TotalInvest * (Rentabilidade/100)
     ValBruto = vbruto + TotalInvest
     IR = (15/100)
     B3 = (0.25/100) * 3

     totalIR = (ValBruto - TotalInvest) * IR
     totalB3 = (ValBruto - TotalInvest) * B3

     ValLiquido = ValBruto - (totalIR + totalB3)
 else:
     investimento = float(input("Quanto deseja investir?: "))
     mensalidade = float(input("Se você for investir todo mês, qual o valor?: "))
     aporte = 50
     TotalInvest = (mensalidade * aporte) + investimento
     Rentabilidade = TotalInvest / investimento - 1
     vbruto = TotalInvest * (Rentabilidade/100)
     ValBruto = vbruto + TotalInvest
     IR = (15/100)
     B3 = (0.25/100) * 5

     totalIR = (ValBruto - TotalInvest) * IR
     totalB3 = (ValBruto - TotalInvest) * B3

     ValLiquido = ValBruto - (totalIR + totalB3)
     

 print("---------------------------------")

 print("           RESULTADO             ")

 print("---------------------------------")
 print("Valor invetido inicialmente: {}".format(investimento))
 print("Aportes no valor de {} por {} meses".format(mensalidade,aporte))
 print("Valor Total Investido {}".format(TotalInvest))

 print("---------------------------------")

 print("Valor Bruto: {}".format(ValBruto))
 print("I.R: {}".format(totalIR))
 print("Taxa B3: {}".format(totalB3))
 print("Valor Liquido: {}".format(ValLiquido))

 print("---------------------------------")

 novamente = str(input("Deseja realizar outra simulação? s/n:"))
 if novamente == 'n':
   print("Obrigado por usar nosso simulador") 
   break