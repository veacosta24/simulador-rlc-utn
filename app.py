import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Configuración de la página (Responsive / Mobile-First)
st.set_page_config(page_title="Física II - UTN FRRE", layout="centered", page_icon="🔌")

# Función auxiliar para formatear los resultados con coma decimal estilo regional
def format_ar(valor):
    return f"{valor:.2f}".replace('.', ',')

# --- ENCABEZADO INSTITUCIONAL ---
st.image("https://www.frre.utn.edu.ar/static/img/LOGO.png", width=120)
st.title("Simulador de Circuitos RLC Serie")
st.markdown("### Cátedra: **FISICA II**")
st.markdown("👩‍💻 **Desarrollado por:** Veronica Acosta")
st.divider()


# --- NUEVA SECCIÓN: MARCO TEÓRICO COMPLETO DE LA CÁTEDRA (UT09) ---
st.markdown("## 📖 Marco Teórico de Respaldo (UT09)")
st.caption("Consultá las bases teóricas, ecuaciones fundamentales y convenios de fase de la UTN antes de simular.")

with st.expander("📘 Ver Apuntes de Cátedra: Fórmulas y Comportamiento Fasorial"):
    
    st.markdown("### 1. Impedancia Compleja e Inversa")
    st.markdown("""
    La oposición total al paso de la corriente alterna en un circuito serie se define mediante la **Impedancia ($Z$)**. En forma binómica se expresa como:
    $$Z = R + j(X_L - X_C)$$
    Donde el módulo y su desfasaje angular (según la guía teórica) se calculan como:
    * **Módulo:** $|Z| = \\sqrt{R^2 + (X_L - X_C)^2}$
    * **Ángulo de Desfasaje ($\\phi$):** $\\phi = \\arctan\\left(\\frac{X_L - X_C}{R}\\right)$
    """)
    
    st.markdown("### 2. Reactancias y Frecuencia")
    st.markdown("""
    El comportamiento de los elementos reactivos depende intrínsecamente de la frecuencia angular $\\omega = 2\\pi f$:
    * **Reactancia Inductiva ($X_L$):** $X_L = \\omega \\cdot L = 2\\pi f \\cdot L$ *(Aumenta linealmente con la frecuencia)*.
    * **Reactancia Capacitiva ($X_C$):** $X_C = \\frac{1}{\\omega \\cdot C} = \\frac{1}{2\\pi f \\cdot C}$ *(Disminuye inversamente con la frecuencia)*.
    """)
    
    st.markdown("### 3. Criterio de Fases y Cuadrantes Fasoriales")
    st.markdown("""
    Dependiendo de la relación entre $X_L$ y $X_C$, el circuito adoptará una de las siguientes identidades:
    
    | Condición | Tipo de Circuito | Desfasaje ($\\phi$) | Comportamiento de las Ondas | Cuadrante Fasor |
    | :--- | :--- | :--- | :--- | :--- |
    | **$X_L > X_C$** | Inductivo | $\\phi > 0$ (Positivo) | La Tensión **adelanta** a la Corriente | 1º Cuadrante (Hacia arriba) |
    | **$X_C > X_L$** | Capacitivo | $\\phi < 0$ (Negativo) | La Corriente **adelanta** a la Tensión | 4º Cuadrante (Hacia abajo) |
    | **$X_L = X_C$** | Resonante | $\\phi = 0$ (Nulo) | Tensión y Corriente en **Fase** | Sobre Eje Real Horizontal |
    """)

    st.markdown("### 4. Triángulo de Potencias")
    st.markdown("""
    El balance energético en corriente alterna se divide en tres componentes vectoriales:
    * **Potencia Activa ($P$):** $P = I_{ef}^2 \\cdot R = V_{ef} \\cdot I_{ef} \\cdot \\cos(\\phi)$ — Unidad: Vatios $[W]$
    * **Potencia Reactiva ($Q$):** $Q = I_{ef}^2 \\cdot (X_L - X_C) = V_{ef} \\cdot I_{ef} \\cdot \\operatorname{sen}(\\phi)$ — Unidad: Voltio-Amperios Reactivos $[VAR]$
    * **Potencia Aparente ($S$):** $S = V_{ef} \\cdot I_{ef} = \\sqrt{P^2 + Q^2}$ — Unidad: Voltio-Amperios $[VA]$
    """)

st.divider()


# --- SECCIÓN 2: BANCO DE EJERCICIOS DE LA GUÍA (Acordeones UX) ---
st.markdown("## 📚 Guía de Ejercicios de Respaldo")
st.caption("Expandí cualquier problema para consultar su enunciado teórico y cargar sus datos automáticamente.")

with st.expander("📝 Problema 1: Circuitos Elementales Puros (R, L, C)"):
    st.markdown("""
    **Enunciado:** Un circuito serie contiene individualmente elementos puros alimentados por una fuente $V(t) = 20 \\cdot \\cos(2\\pi f \\cdot t)$ a $50\\text{ Hz}$ ($V_{ef} = 14,142\\text{ V}$):
    * **Caso A (R Puro):** Resistencia $R = 10\\ \\Omega$.
    * **Caso B (L Puro):** Inductor $L = 5\\text{ mH} = 0,005\\text{ H}$.
    * **Caso C (C Puro):** Capacitor $C = 1000\\ \\mu\\text{F} = 0,001\\text{ F}$.
    """)
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if st.button("Cargar R Puro", key="btn_p1_r"):
            st.session_state["inputs"] = [10.0, 0.0, 999999.0, 14.142, 50.0]
    with col_b:
        if st.button("Cargar L Puro", key="btn_p1_l"):
            st.session_state["inputs"] = [0.0, 0.005, 999999.0, 14.142, 50.0]
    with col_c:
        if st.button("Cargar C Puro", key="btn_p1_c"):
            st.session_state["inputs"] = [0.0, 0.0, 0.001, 14.142, 50.0]

with st.expander("📝 Problema 2: Circuito RL Serie"):
    st.markdown("""
    **Enunciado:** Un circuito serie se compone de una resistencia $R = 12\\ \\Omega$ y una bobina pura con inductancia $L = 2,5\\text{ mH} = 0,0025\\text{ H}$. El conjunto está acoplado a una fuente de corriente alterna de Amplitud Máxima $V_0 = 20\\text{ V}$ ($V_{ef} = 14,142\\text{ V}$) y frecuencia $f = 50\\text{ Hz}$.
    * Calcular impedancia compleja, desfasaje angular, intensidad eficaz y caídas de tensión parciales.
    """)
    if st.button("Cargar Datos del Problema 2", key="btn_p2"):
        st.session_state["inputs"] = [12.0, 0.0025, 999999.0, 14.142, 50.0]

with st.expander("📝 Problema 3: Circuito RC Serie"):
    st.markdown("""
    **Enunciado:** Se conecta en serie una resistencia $R = 20\\ \\Omega$ y un capacitor de capacitancia $C = 1000\\ \\mu\\text{F} = 0,001\\text{ F}$. La fuente de tensión alterna del sistema impone una función de onda $V(t) = 20 \\cdot \\cos(2\\pi f \\cdot t)$ con frecuencia $f = 50\\text{ Hz}$.
    * Determinar el triángulo de impedancias, corriente de la malla, caídas de potencial y balance de potencias.
    """)
    if st.button("Cargar Datos del Problema 3", key="btn_p3"):
        st.session_state["inputs"] = [20.0, 0.0, 0.001, 14.142, 50.0]

with st.expander("📝 Problema 4: Circuito RLC Serie Completo"):
    st.markdown("""
    **Enunciado:** Para un circuito serie con $R = 20\\ \\Omega$, $L = 2,5\\text{ mH} = 0,0025\\text{ H}$ y $C = 1000\\ \\mu\\text{F} = 0,001\\text{ F}$, conectado a una fuente de voltaje eficaz $V_{ef} = 14,142\\text{ V}$ a una frecuencia de red de $50\\text{ Hz}$:
    * Calcular impedancia mixta, corriente de malla, caídas de potencial individuales y potencias.
    * Evaluar el punto de resonancia teórica $f_0$.
    """)
    if st.button("Cargar Datos del Problema 4", key="btn_p4"):
        st.session_state["inputs"] = [20.0, 0.0025, 0.001, 14.142, 50.0]

with st.expander("📝 Problema 5: Análisis Inverso"):
    st.markdown("""
    **Enunciado:** Mediante lecturas instrumentales en un laboratorio de Física II sobre un circuito RLC serie operando a alta frecuencia ($f = 250\\text{ Hz}$), se registran los siguientes valores eficaces: $V_L = 8\\text{ V}$, $V_C = 4\\text{ V}$, $V_{fuente} = 5\\text{ V}$ e $I_{ef} = 3\\text{ A}$.
    * Desarrollar el análisis inverso para deducir los valores nominales de $R$, $L$ y $C$.
    """)
    if st.button("Cargar Datos del Problema 5", key="btn_p5"):
        st.session_state["inputs"] = [1.0, 0.0017, 0.000478, 5.0, 250.0]

st.divider()


# --- SECCIÓN 3: INGRESO INTERACTIVO DE DATOS ---
st.markdown("## ⚙️ Panel de Carga de Parámetros")

if "inputs" not in st.session_state:
    st.session_state["inputs"] = [20.0, 0.0025, 0.001, 14.142, 50.0]

data_inicial = {
    "Resistencia (R) [Ω]": [st.session_state["inputs"][0]],
    "Inductancia (L) [H]": [st.session_state["inputs"][1]],
    "Capacitancia (C) [F]": [st.session_state["inputs"][2]],
    "Voltaje Eficaz (Vrms) [V]": [st.session_state["inputs"][3]],
    "Frecuencia (f) [Hz]": [st.session_state["inputs"][4]]
}
df_inputs = pd.DataFrame(data_inicial)

st.markdown("✏️ **Modificá los valores directamente sobre la tabla desde tu celular o PC:**")
edited_df = st.data_editor(df_inputs, hide_index=True, use_container_width=True)

R = float(edited_df.iloc[0, 0])
L = float(edited_df.iloc[0, 1])
C = float(edited_df.iloc[0, 2])
Vrms = float(edited_df.iloc[0, 3])
f = float(edited_df.iloc[0, 4])

with st.expander("📂 Carga Masiva opcional mediante archivo Excel (.xlsx)"):
    archivo_cargado = st.file_uploader("Subir archivo Excel", type=["xlsx"])
    if archivo_cargado:
        df_excel = pd.read_excel(archivo_cargado)
        st.success("✅ Archivo cargado con éxito.")
        fila = st.number_input("Seleccionar Fila del Excel para evaluar", min_value=0, max_value=len(df_excel)-1, value=0)
        R = float(df_excel.loc[fila, 'R'])
        L = float(df_excel.loc[fila, 'L'])
        C = float(df_excel.loc[fila, 'C'])
        Vrms = float(df_excel.loc[fila, 'Vrms'])
        f = float(df_excel.loc[fila, 'f'])

st.divider()


# --- SECCIÓN 4: NÚCLEO ALGORÍTMICO Y MATEMÁTICO ---
w = 2 * np.pi * f
XL = w * L
XC = 1 / (w * C) if (C != 0 and C < 999999) else 0
Z = np.sqrt(R**2 + (XL - XC)**2)
phi = np.arctan((XL - XC) / R) if R != 0 else (np.pi/2 if (XL - XC) >= 0 else -np.pi/2)

Imax = (Vrms * np.sqrt(2)) / Z if Z != 0 else 0
Ief = Imax / np.sqrt(2)

es_R_puro = (R > 0 and L == 0 and C >= 999999)
es_L_puro = (R == 0 and L > 0 and C >= 999999)
es_C_puro = (R == 0 and L == 0 and C < 999999)
es_RL = (R > 0 and L > 0 and C >= 999999)
es_RC = (R > 0 and L == 0 and C < 999999)
es_RLC = (R > 0 and L > 0 and C < 999999)

DV_R = Ief * R
DV_L = Ief * XL
DV_C = Ief * XC

P_act = (Ief**2) * R
P_react = (Ief**2) * (XL - XC)
P_apar = Vrms * Ief

f_res = 1 / (2 * np.pi * np.sqrt(L * C)) if (L > 0 and C > 0 and C < 999999) else 0

t = np.linspace(0, 0.05, 1000)
v_t = (Vrms * np.sqrt(2)) * np.sin(w * t)

if es_R_puro:
    i_t = Imax * np.sin(w * t)
elif es_L_puro:
    i_t = -Imax * np.cos(w * t)
elif es_C_puro:
    i_t = Imax * np.cos(w * t)
else:
    i_t = Imax * np.sin(w * t - phi)


# --- SECCIÓN 5: SIMULACIÓN GRÁFICA INTERACTIVA ---
st.markdown("## 📊 Simulación Gráfica")

# 1. Curvas en el Dominio del Tiempo
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=v_t, name="v(t) [V]", line=dict(color='#E74C3C', width=3)))
fig.add_trace(go.Scatter(x=t, y=i_t * 10, name="i(t) [A] x10", line=dict(color='#3498DB', width=3, dash='dash')))
fig.update_layout(
    title="Comportamiento Temporal de las Ondas",
    xaxis_title="Tiempo (s)",
    yaxis_title="Amplitud",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    template="plotly_white",
    height=330,
    margin=dict(l=10, r=10, t=40, b=10)
)
st.plotly_chart(fig, use_container_width=True)

# Explicación dinámica del gráfico temporal
with st.container(border=True):
    st.markdown("💡 **Análisis Físico de las Ondas:**")
    if es_R_puro:
        st.write("Al ser un circuito **Resistivo Puro**, las ondas de tensión y corriente nacen y cruzan por cero exactamente en el mismo instante. El desfasaje angular es nulo (0°), indicando que la resistencia consume energía de forma inmediata sin desfasar la señal.")
    elif es_L_puro:
        st.write("En este escenario de **Inductor Puro**, la onda de corriente (azul) arranca retrasada exactamente 90° (un cuarto de ciclo) respecto al voltaje. La bobina reacciona contra el cambio de corriente induciendo una fuerza electromotriz contraria.")
    elif es_C_puro:
        st.write("Bajo una carga **Capacitiva Pura**, la corriente (azul) se encuentra adelantada 90° respecto a la tensión de la fuente, alcanzando su pico máximo en el instante cero debido al proceso inicial de carga de las placas del capacitor.")
    elif es_RL:
        st.write(f"Circuito mixto **Resistivo-Inductivo**. La presencia de la bobina provoca que la corriente (azul) sufra un retraso respecto al voltaje, desplazándose hacia la derecha con un ángulo de desfase calculado de {format_ar(np.degrees(phi))}°.")
    elif es_RC:
        st.write(f"Circuito mixto **Resistivo-Capacitivo**. El campo eléctrico del capacitor ejerce un efecto de adelanto sobre la corriente. Visualmente, la onda azul se adelanta y cruza por cero antes que el voltaje, operando con un ángulo negativo de {format_ar(np.degrees(phi))}°.")
    elif es_RLC:
        if abs(XL - XC) < 1e-4:
            st.write("¡Estado de **Resonancia Eléctrica**! Al igualarse los efectos óhmicos de la bobina y el capacitor ($XL = XC$), el circuito se comporta de forma puramente resistiva. Las ondas se acoplan perfectamente en el tiempo y cruzan por cero de manera síncrona.")
        elif XL > XC:
            st.write(f"Circuito mixto **RLC de perfil Inductivo** ($XL > XC$). Debido a que la frecuencia de {format_ar(f)} Hz está por debajo de los efectos reactivos capacitivos, la bobina predomina. La onda de corriente se observa retrasada respecto al voltaje.")
        else:
            st.write(f"Circuito mixto **RLC de perfil Capacitivo** ($XC > XL$). Como la frecuencia actual está por debajo del punto de resonancia, el capacitor domina la dinámica de la red, forzando a la onda de corriente a adelantarse a la de voltaje.")

# 2. Vectores en el Dominio Fasorial (Referencias activadas)
fig_fasor = go.Figure()
fig_fasor.add_trace(go.Scatter(x=[0, R], y=[0, 0], name="Resistencia R", line=dict(color='black', width=4)))
fig_fasor.add_trace(go.Scatter(x=[R, R], y=[0, XL-XC], name="Reactancia Neta (XL-XC)", line=dict(color='blue', width=4)))
fig_fasor.add_trace(go.Scatter(x=[0, R], y=[0, XL-XC], name="Impedancia Z", line=dict(color='red', width=6)))
fig_fasor.update_layout(
    title="Diagrama Fasorial de Impedancias",
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    height=350,
    margin=dict(l=40, r=40, t=40, b=40),
    xaxis=dict(title="R [Ω]"),
    yaxis=dict(title="X [Ω]"),
    template="plotly_white"
)
st.plotly_chart(fig_fasor, use_container_width=True)

# Explicación geométrica del diagrama fasorial
with st.container(border=True):
    st.markdown("📐 **Análisis Geométrico del Fasor (Vectores):**")
    if es_R_puro:
        st.write("Al no existir componentes inductivos ni capacitivos, el vector azul de reactancia neta es nulo. Por ende, la hipotenusa roja (Impedancia Z) se acuesta perfectamente sobre el eje horizontal negro, concluyendo que Z = R en fase pura.")
    elif es_L_puro:
        st.write("Como la resistencia es cero, el diagrama carece de base horizontal. El fasor de impedancia (rojo) se unifica con la reactancia inductiva (azul), apuntando de manera vertical hacia arriba en el eje imaginario positivo (+90°).")
    elif es_C_puro:
        st.write("Sin resistencia en la malla, el vector de impedancia total (rojo) se proyecta verticalmente hacia abajo sobre el eje imaginario negativo (-90°), reflejando que la oposición se debe únicamente al capacitor.")
    elif es_RL:
        st.write(f"Circuito Mixto Inductivo. La base representa la resistencia y el cateto azul la reactancia inductiva que tira hacia arriba. El vector rojo de impedancia total Z se sitúa en el primer cuadrante con un ángulo positivo de {format_ar(np.degrees(phi))}°.")
    elif es_RC:
        st.write(f"Circuito Mixto Capacitivo. El cateto azul de reactancia neta apunta hacia abajo sobre el eje imaginario. Por ende, el vector rojo de impedancia total Z se sitúa en el cuarto cuadrante con un ángulo negativo de {format_ar(np.degrees(phi))}°.")
    elif es_RLC:
        if abs(XL - XC) < 1e-4:
            st.write(f"¡Frecuencia de Resonancia Exacta ({format_ar(f)} Hz)! Como XL = XC, el cateto vertical azul de reactancia neta desaparece por completo. El vector rojo de Impedancia Z vuelve a acostarse horizontalmente sobre la Resistencia (Z = R = {format_ar(R)} Ω).")
        elif XL > XC:
            st.write(f"¡Frecuencia por encima de la Resonancia (f > {format_ar(f_res)} Hz)! Como XL > XC, el circuito se comporta como Inductivo. El vector azul apunta hacia arriba y la impedancia Z se sitúa en el primer cuadrante con un ángulo de +{format_ar(np.degrees(phi))}°.")
        else:
            st.write(f"¡Frecuencia por debajo de la Resonancia (f < {format_ar(f_res)} Hz)! Como XC > XL, el circuito es Capacitivo. El vector azul apunta hacia abajo y la impedancia Z se sitúa en el cuarto cuadrante con un ángulo de {format_ar(np.degrees(phi))}°.")

st.divider()


# --- SECCIÓN 6: RESULTADOS CON TOOLTIPS TEÓRICOS DE RESPALDO ---
st.markdown("## 📈 Resultados Analíticos y Teóricos")
st.caption("Mantené presionado o pasá el cursor sobre las líneas con el icono (i) para visualizar las ecuaciones de la cátedra.")

t_z = "Z = sqrt(R² + (XL - XC)²)"
t_phi = "φ = arctan((XL - XC) / R)"
t_i = "Irms = Vrms / Z"
t_x = "XL = 2·π·f·L  |  XC = 1 / (2·π·f·C)"
t_v = "ΔVR = I·R  |  ΔVL = I·XL  |  ΔVC = I·XC"
t_p = "P = I²·R (W)  |  Q = I²·X (VAR)  |  S = V·I (VA)"
t_r = "f0 = 1 / (2·π·sqrt(L·C))"

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Impedancia (Z)", f"{format_ar(Z)} Ω", help=t_z)
with c2:
    st.metric("Desfase (φ)", f"{format_ar(np.degrees(phi))}°", help=t_phi)
with c3:
    st.metric("Corriente (Irms)", f"{format_ar(Ief)} A", help=t_i)

st.markdown("#### Detalle de Componentes")
st.markdown(f"ℹ️ **Reactancias:** XL = {format_ar(XL)} Ω  |  XC = {format_ar(XC)} Ω", help=t_x)
st.markdown(f"ℹ️ **Caídas de Tensión:** ΔVR = {format_ar(DV_R)}V  |  ΔVL = {format_ar(DV_L)}V  |  ΔVC = {format_ar(DV_C)}V", help=t_v)

st.markdown("#### Potencias y Criterio de Resonancia")
st.markdown(f"ℹ️ **Triángulo de Potencias:** P = {format_ar(P_act)}W  |  Q = {format_ar(P_react)}VAR  |  S = {format_ar(P_apar)}VA", help=t_p)

if f_res > 0:
    st.markdown(f"""
    <div title="{t_r}" style="background-color:#d4edda; color:#155724; padding:12px; border-radius:5px; border-left:5px solid #28a745; margin-top:10px; cursor:help;">
        🎯 <b>Frecuencia de Resonancia teórica (f0):</b> {format_ar(f_res)} Hz
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style="background-color:#fff3cd; color:#856404; padding:12px; border-radius:5px; border-left:5px solid #ffc107; margin-top:10px;">
        ⚠️ El circuito actual no califica para resonancia (requieres componentes tanto inductivos como capacitivos activos).
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("UTN FRRE - Universidad Tecnológica Nacional Facultad Regional Resistencia | Física II")