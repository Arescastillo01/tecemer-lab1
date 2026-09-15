# TECEMER Lab 1

Proyecto desarrollado como parte del laboratorio de Fundamentos y Entornos de Desarrollo en Python. El programa consume una API pública de chistes y muestra el resultado en la terminal, aplicando manejo de errores durante la consulta.

## Requisitos

- Python 3.10 o superior
- Git
- Visual Studio Code
- Conexión a internet

## Instalación

1. Crear el entorno virtual:

```bash
python -m venv .venv
```

2. Activar el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

3. Instalar el proyecto en modo editable:

```bash
pip install -e .
```

## Uso

Para ejecutar el programa:

```bash
python src/tecemer_lab1/app.py
```

El programa realizará una consulta a una API pública y mostrará un chiste en dos líneas.

## Estructura del repositorio

```text
tecemer-lab1/
├── src/
│   └── tecemer_lab1/
│       ├── __init__.py
│       └── app.py
├── .venv/              (no versionado)
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Autor

Ares Gabriel Castillo Ayarza

## Curso

Tecnologías Emergentes — ISO46B

## Flujo de datos - Semana 2

Durante esta semana se desarrolló un flujo de datos utilizando NumPy, Requests y Pandas.

### Fuente de datos

Los datos meteorológicos fueron obtenidos desde la API pública Open-Meteo, utilizando las coordenadas de Huancayo. Se consultó el pronóstico de 7 días, incluyendo temperatura máxima, temperatura mínima y precipitación.

### Transformación de datos

Los datos obtenidos en formato JSON fueron procesados y convertidos a CSV. Posteriormente, con Pandas se realizaron las siguientes transformaciones:

- Conversión de la fecha a formato datetime.
- Cálculo de la amplitud térmica.
- Identificación de días lluviosos.
- Clasificación de los días en frío, templado o cálido.
- Agrupación de los datos por categoría.

También se utilizó NumPy para trabajar con arrays, realizar operaciones vectorizadas y calcular estadísticas descriptivas.

### Archivos generados

- `numpy_demo.py`
- `clima.py`
- `analisis.py`
- `pronostico_huancayo.json`
- `pronostico_huancayo.csv`
- `pronostico_huancayo_procesado.csv`
- `resumen_por_categoria.csv`

### Resultado

El flujo desarrollado permite obtener datos meteorológicos desde una API REST, almacenarlos, transformarlos y analizarlos utilizando herramientas de Python.