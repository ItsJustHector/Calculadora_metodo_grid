# 🧮 Calculadora Básica con Python y Tkinter

Una aplicación de escritorio ligera y funcional que simula una calculadora estándar. Desarrollada en **Python** utilizando la librería gráfica **Tkinter**.

Este proyecto demuestra el uso de maquetación con `grid`, manejo de eventos (mouse y teclado) y lógica básica de evaluación de expresiones matemáticas.

## 🚀 Características Principales

* **Interfaz Gráfica Limpia:** Diseño organizado utilizando el sistema de grillas (`grid`) de Tkinter.
* **Soporte Completo de Teclado:** Puedes usar tanto el teclado numérico (Numpad) como la fila de números estándar.
    * `Enter` para calcular.
    * `Esc` o `Supr` para borrar.
* **Operaciones Básicas:** Suma, Resta, Multiplicación y División.
* **Manejo de Errores:** Muestra un mensaje de "Error" si intentas operaciones inválidas (como dividir por cero).

## 📋 Requisitos Previos

Para ejecutar este proyecto necesitas tener instalado **Python 3.x**.

No se requieren librerías externas, ya que `tkinter` viene incluido en la instalación estándar de Python.

## 🛠️ Instalación y Ejecución

1.  **Clona o descarga** este repositorio (o guarda el código en un archivo llamado `calculadora.py`).
2.  Abre tu terminal o línea de comandos.
3.  Navega hasta la carpeta donde guardaste el archivo.
4.  Ejecuta el siguiente comando:

```bash
python calculadora.py

🎮 Guía de Uso
Una vez iniciada la aplicación, tienes dos formas de interactuar con ella:

1. Interfaz (Mouse)
Haz clic en los botones de la pantalla para introducir números y operadores.

C: Borra todo el contenido de la pantalla.

=: Realiza el cálculo.

2. Atajos de Teclado (Keyboard Binding)
El código está optimizado para detectar pulsaciones de teclas para una experiencia más rápida:

Tecla Física,Acción en Calculadora
0-9 (y Numpad),Inserta el número
"+, -, *, /",Operadores matemáticos
Enter (Intro),Calcular Resultado (=)
Escape o Supr,Borrar Todo (C)

🔍 ¿Cómo funciona el código?
El script se divide en tres partes fundamentales:

Lógica (on_click):

Utiliza la función nativa eval() de Python para procesar la cadena de texto matemática (ej. "2+2").

Gestiona las excepciones try/except para evitar que el programa se cierre si hay un error matemático.

Mapeo de Teclado (on_key):

Intercepta los eventos del teclado.

Traduce teclas como KP_Enter (Enter del Numpad) o Return a las funciones de la calculadora.

Interfaz Gráfica (UI):

Configura la ventana principal (root).

Genera los botones dinámicamente usando un bucle for y una lista de etiquetas, colocándolos en una cuadrícula de 4 columnas.
Autor: ItsJustHector Licencia: MIT (Libre uso y distribución)
