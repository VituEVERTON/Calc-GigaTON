import time

print(' =========================')
print(' --- SIMULADOR GIGATON ---')
print(' =========================')
valorProduto = int(input('\nInforme o Valor do Produto: '))

print('\nTaxas para MASTERCARD - VISA \n')
avistaDeb = 0.0147 * valorProduto + valorProduto
avistaCred = 0.0298 * valorProduto + valorProduto

p2 = 0.0481 * valorProduto+valorProduto
div2 = p2/2

p3 = 0.0540 * valorProduto+valorProduto
div3 = p3/3

p4 = 0.0601 * valorProduto+valorProduto
div4 = p4/4

p5 = 0.0662 * valorProduto+valorProduto
div5 = p5/5

p6 = 0.0723 * valorProduto+valorProduto
div6 = p6/6

p7 = 0.0786 * valorProduto+valorProduto
div7 = p7/7

p8 = 0.0849 * valorProduto+valorProduto
div8 = p8/8

p9 = 0.0913 * valorProduto+valorProduto
div9 = p9/9

p10 = 0.0978 * valorProduto+valorProduto
div10 = p10/10

p11 = 0.1043 * valorProduto+valorProduto
div11  = p11/11

p12 = 0.1109 * valorProduto+valorProduto
div12 = p12/12

print('À VISTA DÉBITO: ', avistaDeb)
print('À VISTA CRÉDITO: ', avistaCred)
print('2X de R$', round(div2,2),'TOTAL:',p2)
print('3X de R$', round(div3,2) ,'TOTAL:',p3)
print('4X de R$', round(div4,2) ,'TOTAL:',p4)
print('5X de R$', round(div5,2) ,'TOTAL:',p5)
print('6X de R$', round(div6,2) ,'TOTAL:',p6)
print('7X de R$', round(div7,2) ,'TOTAL:',p7)
print('8X de R$', round(div8,2) ,'TOTAL:',p8)
print('9X de R$', round(div9,2) ,'TOTAL:',p9)
print('10X de R$', round(div10,2) ,'TOTAL:',p10)
print('11X de R$', round(div11,2) ,'TOTAL:',p11)
print('12X de R$', round(div12,2) ,'TOTAL:',p12)

print('\nTaxas para ELO - HIPERCARD - AMEX\n')

avistaDeb = 0.0251 * valorProduto + valorProduto
avistaCred = 0.0426 * valorProduto + valorProduto

p2 = 0.0613 * valorProduto+valorProduto
div2 = p2/2

p3 = 0.0674 * valorProduto+valorProduto
div3 = p3/3

p4 = 0.0736 * valorProduto+valorProduto
div4 = p4/4

p5 = 0.0799 * valorProduto+valorProduto
div5 = p5/5

p6 = 0.0862 * valorProduto+valorProduto
div6 = p6/6

p7 = 0.0926 * valorProduto+valorProduto
div7 = p7/7

p8 = 0.0991 * valorProduto+valorProduto
div8 = p8/8

p9 = 0.105 * valorProduto+valorProduto
div9 = p9/9

p10 = 0.112 * valorProduto+valorProduto
div10 = p10/10

p11 = 0.119 * valorProduto+valorProduto
div11  = p11/11

p12 = 0.125 * valorProduto+valorProduto
div12 = p12/12

print('À VISTA DÉBITO: ', avistaDeb)
print('À VISTA CRÉDITO: ', avistaCred)
print('2X de R$', round(div2,2),'TOTAL:',p2)
print('3X de R$', round(div3,2) ,'TOTAL:',p3)
print('4X de R$', round(div4,2) ,'TOTAL:',p4)
print('5X de R$', round(div5,2) ,'TOTAL:',p5)
print('6X de R$', round(div6,2) ,'TOTAL:',p6)
print('7X de R$', round(div7,2) ,'TOTAL:',p7)
print('8X de R$', round(div8,2) ,'TOTAL:',p8)
print('9X de R$', round(div9,2) ,'TOTAL:',p9)
print('10X de R$', round(div10,2) ,'TOTAL:',p10)
print('11X de R$', round(div11,2) ,'TOTAL:',p11)
print('12X de R$', round(div12,2) ,'TOTAL:',p12)

time.sleep(10)






