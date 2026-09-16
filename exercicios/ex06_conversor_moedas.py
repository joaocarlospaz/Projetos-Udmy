#Conversor de Moedas.
real = float(input('Diga-me quanto vc tem em sua carteira em R$: '))
print(f'O dinheiro que vc tem em Real é de {real:.2f} R$. \n'
      f'Convertido em Dollars fica {real / 5.59:.2f} U$!')
dollar = float(input('Agora vamos fazer ao contrario, quanto você tem em Dollar: '))
print(f'O dinheiro que vc tem em Dollars é de {dollar:.2f} U$. \n'
      f'Convertido em Real fica {dollar * 5.59:.2f} R$.')
print('Obrigado por experimentar nosso programa! <3')