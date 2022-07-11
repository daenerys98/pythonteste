notaA=float(input("informe a primeira nota: "))
notaB=float(input("informe a segunda nota: "))

#calcular media
mediafinal = (notaA + notaB) / 2

#verificação
if mediafinal >=7.0:
    print("A média: %.1f - aprovado"%mediafinal)
else:
    print("A média: %.1f - reprovado"% mediafinal)