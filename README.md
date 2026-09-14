# TECEMER Lab 1

Proyecto desarrollado como parte del laboratorio de Fundamentos y Entornos de Desarrollo en Python. El programa consume una API pública de chistes y muestra el resultado en la terminal, aplicando manejo de errores durante la consulta.

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