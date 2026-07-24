import numpy as np
import pandas as pd

# =====================================================
# CONFIGURAÇÕES
# =====================================================

SEED = 42

QUANTIDADE_AMOSTRAS = 1000
QUANTIDADE_OUTLIERS = 20

AREA_MIN = 10
AREA_MAX = 200

COEFICIENTE_ANGULAR = 1200      # preço cresce por m²
INTERCEPTO = 15000              # preço base

DESVIO_PADRAO_RUIDO = 1200     # dispersão natural

MULTIPLICADOR_OUTLIER = 50       # quão absurdos serão os outliers

ARQUIVO_SAIDA = "dataset_regressao_linear.csv"

# =====================================================

np.random.seed(SEED)

# Variável independente (X)
area = np.random.uniform(
    AREA_MIN,
    AREA_MAX,
    QUANTIDADE_AMOSTRAS
)

# Ruído aleatório
ruido = np.random.normal(
    loc=0,
    scale=DESVIO_PADRAO_RUIDO,
    size=QUANTIDADE_AMOSTRAS
)

# Relação linear
preco = (
    INTERCEPTO
    + COEFICIENTE_ANGULAR * area
    + ruido
)

# Criação do DataFrame principal
df = pd.DataFrame({
    "area": area,
    "preco": preco
})

# =====================================================
# Geração dos outliers
# =====================================================

area_outlier = np.random.uniform(
    AREA_MIN,
    AREA_MAX,
    QUANTIDADE_OUTLIERS
)

preco_outlier = (
    INTERCEPTO
    + COEFICIENTE_ANGULAR * area_outlier
)

# Faz metade absurdamente alta
metade = QUANTIDADE_OUTLIERS // 2

preco_outlier[:metade] *= MULTIPLICADOR_OUTLIER

# Faz a outra metade absurdamente baixa
preco_outlier[metade:] /= MULTIPLICADOR_OUTLIER

df_outliers = pd.DataFrame({
    "area": area_outlier,
    "preco": preco_outlier
})

# Junta tudo
df = pd.concat(
    [df, df_outliers],
    ignore_index=True
)

# Salva
df.to_csv("src/regressão/dataset/" +
    ARQUIVO_SAIDA,
    index=False
)

print("=" * 40)
print("Dataset gerado com sucesso!")
print(f"Arquivo: {ARQUIVO_SAIDA}")
print(f"Amostras normais : {QUANTIDADE_AMOSTRAS}")
print(f"Outliers         : {QUANTIDADE_OUTLIERS}")
print(f"Total            : {len(df)}")
print("=" * 40)