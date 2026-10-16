# Semana 04 — Clasificación de lluvia con redes neuronales

## Descripción

Este proyecto corresponde a la Semana 04 del laboratorio de Tecnologías Emergentes.  
El objetivo es preparar datos meteorológicos de Huancayo, entrenar modelos de clasificación y realizar predicciones sobre la ocurrencia de lluvia.

Se trabaja con datos de temperatura máxima, temperatura mínima y precipitación. A partir de estos datos se genera una variable binaria que indica si un día fue lluvioso o no.

## Estructura del proyecto

```text
semana04/
├── pronostico_huancayo.csv
├── pronostico_huancayo.json
├── preparar_dataset.py
├── dataset_preparado.npz
├── perceptron_sintetico.py
├── curvas_entrenamiento_sintetico.png
├── clasificador_lluvia.py
├── curvas_entrenamiento_lluvia.png
├── modelo_lluvia.keras
├── predecir.py
├── README.md
└── tests/
    └── test_preparacion.py
```

## Archivos principales

### `pronostico_huancayo.csv`
Contiene los datos meteorológicos utilizados para preparar el conjunto de entrenamiento y prueba.

### `preparar_dataset.py`
Carga el archivo CSV, crea la variable objetivo `dia_lluvioso`, calcula la amplitud térmica, divide los datos en entrenamiento y prueba, estandariza las características y genera:

```text
dataset_preparado.npz
```

La regla utilizada es:

- precipitación > 0 → día lluvioso (`1`)
- precipitación <= 0 → día sin lluvia (`0`)

### `perceptron_sintetico.py`
Entrena una red neuronal con datos sintéticos y genera la gráfica:

```text
curvas_entrenamiento_sintetico.png
```

### `clasificador_lluvia.py`
Carga `dataset_preparado.npz`, entrena un clasificador de lluvia y genera:

```text
curvas_entrenamiento_lluvia.png
modelo_lluvia.keras
```

### `predecir.py`
Carga el modelo entrenado `modelo_lluvia.keras` y realiza predicciones de prueba.

### `tests/test_preparacion.py`
Contiene pruebas automatizadas para verificar el comportamiento de la función que determina si un día es lluvioso.

## Requisitos

Instalar las dependencias principales:

```bash
python -m pip install numpy pandas scikit-learn tensorflow matplotlib requests pytest
```

## Ejecución

Ubicarse dentro de la carpeta:

```powershell
cd semana04
```

### 1. Preparar el dataset

```powershell
python preparar_dataset.py
```

Esto genera:

```text
dataset_preparado.npz
```

### 2. Entrenar el perceptrón sintético

```powershell
python perceptron_sintetico.py
```

Esto genera:

```text
curvas_entrenamiento_sintetico.png
```

### 3. Entrenar el clasificador de lluvia

```powershell
python clasificador_lluvia.py
```

Esto genera:

```text
curvas_entrenamiento_lluvia.png
modelo_lluvia.keras
```

### 4. Realizar predicciones

```powershell
python predecir.py
```

### 5. Ejecutar las pruebas

```powershell
python -m pytest tests -v
```

Resultado obtenido durante la verificación:

```text
3 passed
```

## Resultados

Durante las pruebas del proyecto se verificó que:

- El dataset se prepara correctamente.
- El perceptrón sintético alcanza una precisión cercana al 91 % en la ejecución realizada.
- El clasificador de lluvia puede entrenarse y guardar el modelo en formato Keras.
- El script de predicción carga correctamente el modelo y devuelve probabilidades de lluvia.
- Las tres pruebas automatizadas de `test_preparacion.py` se ejecutan correctamente.

## Nota

Los resultados del modelo dependen de los datos meteorológicos disponibles. Si el conjunto de entrenamiento contiene una sola clase, el clasificador no podrá entrenarse correctamente. Por ello, el dataset debe incluir tanto días con lluvia como días sin lluvia.

## Autor

Proyecto académico — Semana 04  
Universidad Nacional del Centro del Perú  
Ingeniería de Sistemas
