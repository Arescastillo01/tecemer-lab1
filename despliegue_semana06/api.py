
import pickle

from flask import Flask, request, jsonify
from tensorflow import keras

from preprocesamiento_api import extraer_caracteristicas




app = Flask(__name__)




modelo_api = keras.models.load_model("modelo_produccion.keras")

with open("escalador_produccion.pkl", "rb") as f:
    escalador_api = pickle.load(f)




@app.route("/salud", methods=["GET"])
def salud():
    return jsonify({
        "estado": "ok",
        "modelo_cargado": True
    }), 200




@app.route("/predecir", methods=["POST"])
def predecir():

    datos_json = request.get_json(silent=True)


    if datos_json is None:
        return jsonify({
            "error": "Se esperaba un cuerpo JSON válido"
        }), 400

    try:
        caracteristicas = extraer_caracteristicas(datos_json)

    except ValueError as error:
        return jsonify({
            "error": str(error)
        }), 400

   
    caracteristicas_esc = escalador_api.transform(caracteristicas)

    
    probabilidad = float(
        modelo_api.predict(
            caracteristicas_esc,
            verbose=0
        )[0][0]
    )

    
    prediccion = (
        "lluvia"
        if probabilidad > 0.5
        else "no_lluvia"
    )

    return jsonify({
        "prediccion": prediccion,
        "probabilidad": round(probabilidad, 4)
    }), 200




if __name__ == "__main__":
    print("API Flask iniciada")
    print("Servidor: http://127.0.0.1:5000")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )