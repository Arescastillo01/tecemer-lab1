\# Clasificador de lluvia con una red neuronal



\## Descripción



En este proyecto se desarrolla un clasificador de días lluviosos utilizando una red neuronal tipo MLP (Perceptrón Multicapa) con TensorFlow y Keras.



El modelo utiliza datos meteorológicos de Huancayo y determina si un día puede clasificarse como lluvioso o no lluvioso.



\## Dataset



El archivo utilizado es:



`pronostico\_huancayo.csv`



Contiene información sobre:



\* Fecha

\* Temperatura máxima

\* Temperatura mínima

\* Precipitación



La variable objetivo `dia\_lluvioso` se obtiene a partir de la precipitación:



\* `1`: día lluvioso

\* `0`: día no lluvioso



\## Características utilizadas



Para entrenar el modelo se utilizan tres características:



\* `temp\_max`

\* `temp\_min`

\* `amplitud\_termica`



La amplitud térmica se calcula mediante:



`amplitud\_termica = temp\_max - temp\_min`



Los datos son estandarizados antes del entrenamiento.



\## Modelos utilizados



\### Regresión Logística



Se utiliza como modelo base para comparar el rendimiento de la red neuronal.



Precisión obtenida:



`0.7500`



\### Red neuronal MLP



La arquitectura utilizada es:



\* Capa de entrada: 3 características

\* Capa Dense: 8 neuronas, activación ReLU

\* Capa Dense: 4 neuronas, activación ReLU

\* Capa de salida: 1 neurona, activación Sigmoid



La red fue entrenada durante 40 épocas utilizando Adam y binary crossentropy.



Resultado obtenido:



\* Pérdida: `0.5145`

\* Precisión: `0.7500`



\## Predicción



El archivo `predecir.py` permite utilizar el modelo entrenado para realizar nuevas predicciones.



Ejecutar:



```powershell

python predecir.py

```



Las observaciones utilizadas en la prueba fueron clasificadas como días lluviosos.



\## Pruebas



Se implementaron tres pruebas automáticas para verificar la función `calcular\_dia\_lluvioso()`.



Ejecutar:



```powershell

python -m pytest tests/ -v

```



Resultado:



```text

3 passed

```



\## Archivos principales



\* `pronostico\_huancayo.csv`: datos meteorológicos.

\* `preparar\_dataset.py`: preparación y transformación de los datos.

\* `dataset\_preparado.npz`: dataset listo para el entrenamiento.

\* `perceptron\_sintetico.py`: ejercicio con datos sintéticos.

\* `clasificador\_lluvia.py`: entrenamiento de los modelos.

\* `modelo\_lluvia.keras`: modelo neuronal entrenado.

\* `predecir.py`: generación de nuevas predicciones.

\* `curvas\_entrenamiento\_lluvia.png`: gráfico del entrenamiento.

\* `curvas\_entrenamiento\_sintetico.png`: gráfico del ejercicio sintético.

\* `tests/test\_preparacion.py`: pruebas automatizadas.



\## Tecnologías utilizadas



\* Python

\* NumPy

\* Pandas

\* Scikit-learn

\* TensorFlow

\* Keras

\* Matplotlib

\* Pytest



