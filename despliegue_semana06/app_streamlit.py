import os
import pickle
import streamlit as st
from tensorflow import keras

from preprocesamiento_api import extraer_caracteristicas




st.set_page_config(
    page_title="Predicción de Lluvia",
    page_icon="🌧️",
    layout="centered"
)


st.title("🌧️ Predicción de Lluvia en Huancayo")

st.write(
    "Ingrese los datos climáticos para estimar "
    "si lloverá mañana."
)




RUTA_MODELO = "modelo_produccion.keras"
RUTA_ESCALADOR = "escalador_produccion.pkl"


# Verificar que existan los archivos
if not os.path.exists(RUTA_MODELO):
    st.error("No se encontró modelo_produccion.keras")
    st.stop()

if not os.path.exists(RUTA_ESCALADOR):
    st.error("No se encontró escalador_produccion.pkl")
    st.stop()




@st.cache_resource
def cargar_modelo():

    modelo = keras.models.load_model(RUTA_MODELO)

    with open(RUTA_ESCALADOR, "rb") as f:
        escalador = pickle.load(f)

    return modelo, escalador


modelo, escalador = cargar_modelo()




temp_max = st.number_input(
    "Temperatura máxima (°C)",
    value=18.5,
    step=0.1
)

temp_min = st.number_input(
    "Temperatura mínima (°C)",
    value=4.2,
    step=0.1
)

viento_max = st.number_input(
    "Viento máximo",
    value=12.0,
    step=0.1
)




if st.button("Predecir lluvia de mañana"):

    datos = {
        "temp_max": temp_max,
        "temp_min": temp_min,
        "viento_max": viento_max
    }

    try:

        caracteristicas = extraer_caracteristicas(datos)

        caracteristicas_esc = escalador.transform(
            caracteristicas
        )

        probabilidad = float(
            modelo.predict(
                caracteristicas_esc,
                verbose=0
            )[0][0]
        )

        prediccion = (
            "lluvia"
            if probabilidad > 0.5
            else "no_lluvia"
        )

        st.subheader("Resultado")

        if prediccion == "lluvia":
            st.success("🌧️ Predicción: LLUVIA")
        else:
            st.success("☀️ Predicción: NO LLUVIA")

        st.write(
            f"Probabilidad de lluvia: "
            f"**{probabilidad * 100:.2f}%**"
        )

    except Exception as error:

        st.error(
            f"Error al realizar la predicción: {error}"
        )