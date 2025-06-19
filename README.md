# 🧮 Calculadora de Áreas - PyQt6

Una aplicación de escritorio desarrollada en **Python** utilizando **PyQt6** y **Programación Orientada a Objetos (POO)**, que permite calcular el área de figuras geométricas a través de una interfaz gráfica amigable, diseñada en Qt Designer.

---

---

## 🎯 Funcionalidades

- ✅ Cálculo de área de:
  - Círculo
  - Triángulo
  - Rectángulo
  - Cuadrado
- ✅ Menú interactivo con accesos rápidos
- ✅ Visualización de fórmulas matemáticas
- ✅ Imagen ilustrativa de las figuras
- ✅ Validación de entrada (solo números positivos)
- ✅ Historial de cálculos mostrado en la interfaz

---

## 🗂️ Estructura del Proyecto

```plaintext
proyecto/
├── src/
│   ├── logica/
│   │   └── areas.py         # Clases POO para cada figura
│   ├── vista/
│   │   ├── main_window.ui   # UI diseñada en Qt Designer
│   │   ├── ui_main.py       # UI convertida con pyuic6
│   │   └── img/
│   │       └── figuras.png  # Imagen con formas geométricas
├── app.py                   # Punto de entrada principal
└── README.md                # Documentación del proyecto
```


## 🛠️ Tecnologías y Requisitos

- Python 3.10+
- PyQt6

### 📦 Instalación de dependencias

```bash
pip install PyQt6
##🔧 Edición de la UI
Si deseas editar la UI desde .ui, necesitas Qt Designer y puedes convertirlo con:
bashpyuic6 src/vista/main_window.ui -o src/vista/ui_main.py
##▶️ ¿Cómo ejecutar la aplicación?
Desde la raíz del proyecto:
bashpython app.py
```
##👥 Integrante

Flores Torres Jhanpool - Ingeniería de Sistemas – Universidad Continental

##📝 Licencia
Este proyecto se distribuye bajo la licencia MIT. Uso libre con fines académicos y educativos.
