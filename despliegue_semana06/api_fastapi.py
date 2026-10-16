import pickle

from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow import keras

from preprocesamiento_api import extraer_caracteristicas


app = FastAPI(
    title="API de Predicción de Lluvia",
    description="API para predecir si lloverá mañana en Huancayo",
    version="1.0.0"
)



modelo_api = keras.models.load_model("modelo_produccion.keras")


with open("escalador_produccion.pkl", "rb") as f:
    escalador_api = pickle.load(f)


# Datos esperados
class DatosClima(BaseModel):
    temp_max: float
    temp_min: float
    viento_max: float


@app.get("/salud")
def salud():
    return {
        "estado": "ok",
        "modelo_cargado": True
    }


@app.post("/predecir")
def predecir(datos: DatosClima):

    datos_json = {
        "temp_max": datos.temp_max,
        "temp_min": datos.temp_min,
        "viento_max": datos.viento_max
    }

    caracteristicas = extraer_caracteristicas(datos_json)

    caracteristicas_esc = escalador_api.transform(caracteristicas)

    probabilidad = float(
        modelo_api.predict(
            caracteristicas_esc,
            verbose=0
        )[0][0]
    )

    prediccion = "lluvia" if probabilidad > 0.5 else "no_lluvia"

    return {
        "prediccion": prediccion,
        "probabilidad": round(probabilidad, 4)
    }