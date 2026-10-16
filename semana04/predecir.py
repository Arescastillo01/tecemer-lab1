import numpy as np
from tensorflow import keras

# 1. Cargar el modelo entrenado
modelo = keras.models.load_model("modelo_lluvia.keras")

# 2. Nuevas observaciones:
# [temp_max, temp_min, amplitud_termica]
observaciones_nuevas = np.array([
    [0.5, 0.3, 0.1],
    [-1.2, -0.8, -0.4],
])

# 3. Realizar predicciones
probabilidades = modelo.predict(observaciones_nuevas, verbose=0)

predicciones = (probabilidades > 0.5).astype(int)

for i, (prob, pred) in enumerate(zip(probabilidades, predicciones)):
    etiqueta = "lluvioso" if pred[0] == 1 else "no lluvioso"

    print(
        f"Observación {i + 1}: "
        f"probabilidad={prob[0]:.3f} -> "
        f"predicción: día {etiqueta}"
    )