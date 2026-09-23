import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def calcular_dia_lluvioso(precipitacion):
    """Determina si hubo lluvia durante el día."""
    if hasattr(precipitacion, "astype"):
        return (precipitacion > 0).astype(int)
    return int(precipitacion > 0)


# 1. Cargar el dataset
df = pd.read_csv("pronostico_huancayo.csv")

print("Primeras filas del dataset:")
print(df.head())

print("\nInformación del dataset:")
print(df.info())

# 2. Crear la variable objetivo
df["dia_lluvioso"] = calcular_dia_lluvioso(df["precipitacion"])

# 3. Crear una nueva característica
df["amplitud_termica"] = df["temp_max"] - df["temp_min"]

# 4. Seleccionar las características
caracteristicas = [
    "temp_max",
    "temp_min",
    "amplitud_termica"
]

X = df[caracteristicas]
y = df["dia_lluvioso"]

# 5. Eliminar filas con valores nulos
datos = pd.concat([X, y], axis=1).dropna()

X = datos[caracteristicas]
y = datos["dia_lluvioso"]

# 6. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# 7. Estandarizar los datos
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 8. Guardar el dataset preparado
np.savez(
    "dataset_preparado.npz",
    X_train=X_train,
    X_test=X_test,
    y_train=y_train.to_numpy(),
    y_test=y_test.to_numpy()
)

print("\nDataset preparado correctamente.")
print(f"Datos de entrenamiento: {X_train.shape}")
print(f"Datos de prueba: {X_test.shape}")
print(f"Clases de entrenamiento: {np.unique(y_train)}")
print("Archivo generado: dataset_preparado.npz")