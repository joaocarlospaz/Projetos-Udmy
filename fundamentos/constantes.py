"""
Constantes, "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # Velocidade atual do carro;
local_carro = 90 # Local atual em que está o carro;

RADAR_1 = 60 # Velocidade Max, do radar 1;
LOCAL_1 = 100 # Local onde o radar 1 está;
RADAR_RANGE = 1 # A distância onde o radar pega;

velocidade_radar1 = velocidade > RADAR_1
multa_radar1 = local_carro >= (LOCAL_1- RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = multa_radar1 and velocidade_radar1

if velocidade > RADAR_1:
    print('Ultrapassou os limites de velocidade.')

if multa_radar1:
    print('Carro passou dentro dos limites de velocidade')
    
if carro_multado:
    print('Carro multado radar 1.')