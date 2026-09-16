# Conversor de Medidas
print('- Conversor de Medidas !')
n1 = int(input('Digite uma distância em metros: '))
me = str(n1) + 'm'
print(f'Conversor de Medidas, {me} em: \n'
       f'Km = {n1 / 1000} \n'
      f'hm = {n1 / 100} \n'
       f'dam = {n1 / 10} \n'
      f'dm = {n1 * 10:.0f} \n'
       f'cm = {n1 * 100:.0f} \n'
       f'mm = {n1 * 1000:.0f} \n')