# 🔌 Simulador de Circuitos RLC Serie — UTN FRRE

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://simulador-rlc-utn.streamlit.app/)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Cátedra](https://img.shields.io/badge/UTN_FRRE-F%C3%ADsica_II-0055A5)](https://www.frre.utn.edu.ar/)

Aplicación web interactiva desarrollada para la simulación, análisis y visualización de **Circuitos de Corriente Alterna RLC Serie** (Unidad Temática 09 - Física II). Permite a los estudiantes contrastar los cálculos analíticos de la guía de trabajos prácticos con simulaciones visuales en tiempo real.

🚀 **Acceso directo a la aplicación en la nube:** [simulador-rlc-utn.streamlit.app](https://simulador-rlc-utn.streamlit.app/)

---

## 💻 Desarrollado por
* **Alumna:** Verónica Elizabeth Acosta
* **Rol:** Estudiante de Ingeniería en Sistemas de Información
* **Cátedra:** Física II — UTN Facultad Regional Resistencia (FRRE)
* **Docente:** Mario Sergio Cleva

---

## ✨ Características Principales

* **📊 Gráficos Temporales en Doble Eje Y (Plotly):** Representación síncrona de la Tensión de la fuente $v(t)$ [V] y la Corriente $i(t)$ [A] con ejes independientes y autoescalables para evitar la pérdida visual de picos en señales de pequeña magnitud. Trazos continuos de alta legibilidad.
* **📐 Diagrama Fasorial Dinámico:** Representación en el plano complejo de la Resistencia ($R$), Reactancia Neta ($X_L - X_C$) e Impedancia Total ($Z$) con actualización vectorial instantánea.
* **✏️ Editor Tabular Interactivo (Data Editor):** Modificación directa de parámetros físicos ($R, L, C, V_{rms}, f$) sobre la interfaz sin requerir archivos externos.
* **📚 Banco de Ejercicios de la Guía Precargados:** Acceso mediante un clic a los problemas de la Guía de Trabajos Prácticos de la Cátedra (P1 al P5, incluyendo escenarios puros y análisis inverso).
* **🎯 Detector de Resonancia:** Cálculo analítico e indicador dinámico de la Frecuencia de Resonancia ($f_0$).
* **📱 Diseño Responsive & Cloud-Native:** Desplegado en Streamlit Cloud y optimizado para su uso en computadoras y dispositivos móviles.

---

## 📖 Fundamento Teórico y Ecuaciones

El simulador implementa el marco matemático de la UT09 para circuitos serie en Corriente Alterna:

* **Reactancia Inductiva:** $$X_L = 2\pi f \cdot L$$
* **Reactancia Capacitiva:** $$X_C = \frac{1}{2\pi f \cdot C}$$
* **Impedancia Total:** $$|Z| = \sqrt{R^2 + (X_L - X_C)^2}$$
* **Ángulo de Desfase:** $$\phi = \arctan\left(\frac{X_L - X_C}{R}\right)$$
* **Frecuencia de Resonancia:** $$f_0 = \frac{1}{2\pi \sqrt{L \cdot C}}$$

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.11
* **Framework Web:** Streamlit Cloud
* **Motor Gráfico:** Plotly Subplots (Doble eje autoescalable)
* **Procesamiento de Datos:** NumPy & Pandas

---

## ⚙️ Ejecución Local (Opcional)

Si deseás clonar y ejecutar el proyecto de manera local en tu equipo:

* Clonar el repositorio:
git clone https://github.com/veacosta24/simulador-rlc-utn.git
cd simulador-rlc-utn

* Instalar dependencias:
Asegurate de tener el archivo requirements.txt en la misma carpeta y ejecutá el siguiente comando en tu terminal:
pip install -r requirements.txt

* Ejecutar la aplicación:
Lanzá el servidor local de Streamlit para abrir la interfaz ejecutando:
streamlit run app.py
