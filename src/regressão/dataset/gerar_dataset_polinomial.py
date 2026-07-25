import numpy as np
import pandas as pd

# ==========================
# Configurações do Dataset
# ==========================

QUANTIDADE_AMOSTRAS = 1000

AREA_MIN = 20
AREA_MAX = 300

COEFICIENTE_QUADRATICO = 8
COEFICIENTE_LINEAR = 400
INTERCEPTO = 50000

DESVIO_PADRAO_RUIDO = 30000

QUANTIDADE_OUTLIERS = 10
MULTIPLICADOR_OUTLIER = 5

ARQUIVO_SAIDA = "dataset_regressao_polinomial.csv"

# ==========================
# Geração dos dados
# ==========================

np.random.seed(42)

area = np.random.uniform(
    AREA_MIN,
    AREA_MAX,
    QUANTIDADE_AMOSTRAS
)

ruido = np.random.normal(
    0,
    DESVIO_PADRAO_RUIDO,
    QUANTIDADE_AMOSTRAS
)

preco = (
    COEFICIENTE_QUADRATICO * area**2
    + COEFICIENTE_LINEAR * area
    + INTERCEPTO
    + ruido
)

# ==========================
# Inserção dos Outliers
# ==========================

indices = np.random.choice(
    QUANTIDADE_AMOSTRAS,
    QUANTIDADE_OUTLIERS,
    replace=False
)

preco[indices] *= MULTIPLICADOR_OUTLIER

# ==========================
# Salvar CSV
# ==========================

df = pd.DataFrame({
    "area": area,
    "preco": preco
})

df.to_csv("src/regressão/dataset/" +
    ARQUIVO_SAIDA,
    index=False
)

print(f"Dataset salvo em: {ARQUIVO_SAIDA}")