import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Configuración de la página (Responsive / Mobile-First estricto)
st.set_page_config(page_title="Física II - UTN FRRE", layout="centered", page_icon="🔌")

# Función auxiliar para formatear los resultados con coma decimal estilo regional
def format_ar(valor):
    return f"{valor:.2f}".replace('.', ',')

# --- ENCABEZADO INSTITUCIONAL ---
st.image("https://www.frre.utn.edu.ar/static/img/LOGO.png", width=110)
st.title("Simulador de Circuitos RLC Serie")
st.markdown("### Cátedra: **FISICA II**")
st.markdown("👩‍💻 **Desarrollado por:** Veronica Acosta")
st.divider()


# --- MARCO TEÓRICO COMPLETO DE LA CÁTEDRA (Optimizado contra desbordamiento móvil) ---
st.markdown("## 📖 Marco Teórico de Respaldo (UT09)")
st.caption("Consultá las bases teóricas, ecuaciones fundamentales y convenios de fase de la UTN.")

with st.expander("📘 Ver Apuntes de Cátedra: Fórmulas y Comportamiento"):
    
    st.markdown("### 1. Impedancia Compleja")
    st.markdown("""
    La oposición total al paso de la corriente alterna en un circuito serie se define mediante la **Impedancia ($Z$)**. En forma binómica se expresa como:  
    $Z = R + j(X_L - X_C)$  
    
    El módulo y su desfasaje angular se calculan mediante las siguientes relaciones trigonométricas:  
    * **Módulo:** $|Z| = \\sqrt{R^2 + (X_L - X_C)^2}$  
    * **Ángulo ($\\phi$):** $\\phi = \\arctan((X_L - X_C) / R)$
    """)
    
    st.markdown("### 2. Reactancias y Frecuencia")
    st.markdown("""
    La oposición de los elementos reactivos depende de la frecuencia angular $\\omega = 2\\pi f$:  
    * **Reactancia Inductiva:** $X_L = 2\\pi f \\cdot L$ *(Aumenta con la frecuencia)*.  
    * **Reactancia Capacitiva:** $X_C = 1 / (2\\pi f \\cdot C)$ *(Disminuye con la frecuencia)*.
    """)
    
    st.markdown("### 3. Criterio de Fases y Cuadrantes")
    st.markdown("""
    * **$X_L > X_C$ (Inductivo):** $\\phi > 0$. La tensión adelanta a la corriente. El fasor resultante se sitúa en el **1º Cuadrante** (hacia arriba).
    * **$X_C > X_L$ (Capacitivo):** $\\phi < 0$. La corriente adelanta a la tensión. El fasor resultante se sitúa en el **4º Cuadrante** (hacia abajo).
    * **$X_L = X_C$ (Resonancia):** $\\phi = 0$. Ondas en fase. El fasor se acuesta sobre el eje horizontal.
    """)

    st.markdown("### 4. Triángulo de Potencias")
    st.markdown("""
    * **Potencia Activa ($P$):** $P = I_{ef}^2 \\cdot R$ $[W]$
    * **Potencia Reactiva ($Q$):** $Q = I_{ef}^2 \\cdot (X_L - X_C)$ $[VAR]$
    * **Potencia Aparente ($S$):** $S = V_{ef} \\cdot I_{ef}$ $[VA]$
    """)

st.divider()


# --- SECCIÓN 2: BANCO DE EJERCICIOS DE LA GUÍA (Acordeones UX) ---
st.markdown("## 📚 Guía de Ejercicios de Respaldo")
st.caption("Tocá un problema para cargar sus parámetros automáticamente en el simulador.")

with st.expander("📝 Problema 1: Circuitos Elementales Puros (R, L, C)"):
    st.markdown("""
    **Enunciado:** Un circuito serie contiene individualmente elementos puros alimentados por una fuente $V(t) = 20 \\cdot \\cos(2\\pi f \\cdot t)$ a $50\\text{ Hz}$ ($V_{ef} = 14,142\\text{ V}$):
    * **Caso A (R Puro):** Resistencia $R = 10\\ \\Omega$.
    * **Caso B (L Puro):** Inductor $L = 5\\text{ mH} = 0,005\\text{ H}$.
    * **Caso C (C Puro):** Capacitor $C = 1000\\ \\mu\\text{F} = 0,001\\text{ F}$.
    """)
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if st.button("R Puro", key="btn_p1_r", use_container_width=True):
            st.session_state["inputs"] = [10.0, 0.0, 999999.0, 14.142, 50.0]
    with col_b:
        if st.button("L Puro", key="btn_p1_l", use_container_width=True):
            st.session_state["inputs"] = [0.0, 0.005, 999999.0, 14.142, 50.0]
    with col_c:
        if st.button("C Puro", key="btn_p1_c", use_container_width=True):
            st.session_state["inputs"] = [0.0, 0.0, 0.001, 14.142, 50.0]

with st.expander("📝 Problema 2: Circuito RL Serie"):
    st.markdown("""
    **Enunciado:** Resistencia $R = 12\\ \\Omega$ e inductancia $L = 2,5\\text{ mH}$ en serie. Fuente con $V_0 = 20\\text{ V}$ ($V_{ef} = 14,142\\text{ V}$) y frecuencia $f = 50\\text{ Hz}$.
    """)
    if st.button("Cargar Problema 2", key="btn_p2", use_container_width=True):
        st.session_state["inputs"] = [12.0, 0.0025, 999999.0, 14.142, 50.0]

with st.expander("📝 Problema 3: Circuito RC Serie"):
    st.markdown("""
    **Enunciado:** Resistencia $R = 20\\ \\Omega$ y capacitor $C = 1000\\ \\mu\\text{F}$ en serie. Fuente de onda con $f = 50\\text{ Hz}$ y $V_{ef} = 14,142\\text{ V}$.
    """)
    if st.button("Cargar Problema 3", key="btn_p3", use_container_width=True):
        st.session_state["inputs"] = [20.0, 0.0, 0.001, 14.142, 50.0]

with st.expander("📝 Problema 4: Circuito RLC Serie Completo"):
    st.markdown("""
    **Enunciado:** Circuito serie con $R = 20\\ \\Omega$, $L = 2,5\\text{ mH}$ y $C = 1000\\ \\mu\\text{F}$. Fuente de voltaje eficaz $V_{ef} = 14,142\\text{ V}$ a $50\\text{ Hz}$.
    """)
    if st.button("Cargar Problema 4", key="btn_p4", use_container_width=True):
        st.session_state["inputs"] = [20.0, 0.0025, 0.001, 14.142, 50.0]

with st.expander("📝 Problema 5: Análisis Inverso"):
    st.markdown("""
    **Enunciado:** Lecturas a alta frecuencia ($f = 250\\text{ Hz}$): $V_L = 8\\text{ V}$, $V_C = 4\\text{ V}$, $V_{fuente} = 5\\text{ V}$ e $I_{ef} = 3\\text{ A}$. Deducir los valores reales de los componentes.
    """)
    if st.button("Cargar Problema 5", key="btn_p5", use_container_width=True):
        st.session_state["inputs"] = [1.0, 0.0017, 0.000478, 5.0, 250.0]

st.divider()


# --- SECCIÓN 3: INGRESO INTERACTIVO DE DATOS ---
st.markdown("## ⚙️ Panel de Carga de Parámetros")

if "inputs" not in st.session_state:
    st.session_state["inputs"] = [20.0, 0.0025, 0.001, 14.142, 50.0]

data_inicial = {
    "R [Ω]": [st.session_state["inputs"][0]],
    "L [H]": [st.session_state["inputs"][1]],
    "C [F]": [st.session_state["inputs"][2]],
    "Vrms [V]": [st.session_state["inputs"][3]],
    "f [Hz]": [st.session_state["inputs"][4]]
}
df_inputs = pd.DataFrame(data_inicial)

st.markdown("✏️ **Modificá los valores directamente sobre las celdas:**")
edited_df = st.data_editor(df_inputs, hide_index=True, use_container_width=True)

R = float(edited_df.iloc[0, 0])
L = float(edited_df.iloc[0, 1])
C = float(edited_df.iloc[0, 2])
Vrms = float(edited_df.iloc[0, 3])
f = float(edited_df.iloc[0, 4])


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


# --- SECCIÓN 5: VISUALIZACIÓN GRÁFICA RESPONSIVE ---
st.markdown("## 📊 Simulación Gráfica")

# 1. Gráfico Temporal (Sin leyendas nativas molestas)
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=v_t, name="v(t)", line=dict(color='#E74C3C', width=3)))
fig.add_trace(go.Scatter(x=t, y=i_t * 10, name="i(t)x10", line=dict(color='#3498DB', width=3, dash='dash')))
fig.update_layout(
    title="Comportamiento Temporal de las Ondas",
    xaxis_title="Tiempo (s)",
    yaxis_title="Amplitud",
    showlegend=False,
    template="plotly_white",
    height=280,
    margin=dict(l=10, r=10, t=40, b=10)
)
st.plotly_chart(fig, use_container_width=True)
st.markdown("<p style='text-align: center; font-size: 13px;'>🔴 Voltaje de la Fuente v(t) &nbsp;&nbsp;|&nbsp;&nbsp; 🔵 Corriente i(t) multiplicada x10</p>", unsafe_allow_html=True)

# Explicación del gráfico temporal
with st.container(border=True):
    st.markdown("💡 **Análisis Físico de las Ondas:**")
    if es_R_puro:
        st.write("Al ser un circuito **Resistivo Puro**, las ondas están en fase. Nacen y cruzan por cero exactamente en el mismo instante (desfasaje nulo de 0°).")
    elif es_L_puro:
        st.write("En un **Inductor Puro**, la corriente (azul) está retrasada exactamente 90° respecto al voltaje debido a la fem autoinducida de la bobina.")
    elif es_C_puro:
        st.write("Bajo carga **Capacitiva Pura**, la corriente (azul) se adelanta exactamente 90° respecto a la tensión por la carga instantánea de las placas.")
    elif es_RL:
        st.write(f"Circuito mixto **RL**. La bobina retrasa la corriente (azul) respecto al voltaje, desplazándola a la derecha un ángulo de {format_ar(np.degrees(phi))}°.")
    elif es_RC:
        st.write(f"Circuito mixto **RC**. El capacitor adelanta la corriente (azul), haciendo que cruce por cero antes que el voltaje con un ángulo de {format_ar(np.degrees(phi))}°.")
    elif es_RLC:
        if abs(XL - XC) < 1e-4:
            st.write("¡**Resonancia Eléctrica**! Al igualarse XL y XC, los efectos reactivos se anulan y el circuito vuelve a quedar en fase pura (sincronizados).")
        elif XL > XC:
            st.write(f"Circuito **RLC Inductivo** ($XL > XC$). La frecuencia está por encima de la resonancia, predomina la bobina y la corriente (azul) se retrasa.")
        else:
            st.write(f"Circuito **RLC Capacitivo** ($XC > XL$). La frecuencia está por debajo de la resonancia, manda el capacitor y la corriente (azul) se adelanta.")

st.write("")

# 2. Gráfico Fasorial (Sin leyendas nativas que colapsen el vector)
fig_fasor = go.Figure()
fig_fasor.add_trace(go.Scatter(x=[0, R], y=[0, 0], line=dict(color='black', width=4)))
fig_fasor.add_trace(go.Scatter(x=[R, R], y=[0, XL-XC], line=dict(color='blue', width=4)))
fig_fasor.add_trace(go.Scatter(x=[0, R], y=[0, XL-XC], line=dict(color='red', width=6)))
fig_fasor.update_layout(
    title="Diagrama Fasorial de Impedancias",
    showlegend=False,
    height=280,
    margin=dict(l=30, r=30, t=40, b=30),
    xaxis=dict(title="R [Ω]"),
    yaxis=dict(title="X [Ω]"),
    template="plotly_white"
)
st.plotly_chart(fig_fasor, use_container_width=True)
st.markdown("<p style='text-align: center; font-size: 13px;'>⚫ Resistencia R &nbsp;&nbsp;|&nbsp;&nbsp; 🔵 Reactancia Neta (XL-XC) &nbsp;&nbsp;|&nbsp;&nbsp; 🔴 Impedancia Total Z</p>", unsafe_allow_html=True)

# Explicación del diagrama fasorial
with st.container(border=True):
    st.markdown("📐 **Análisis Geométrico del Fasor:**")
    if es_R_puro:
        st.write("Sin reactancias, el vector azul es nulo. El fasor de Impedancia Z (rojo) se acuesta horizontalmente sobre la Resistencia ($Z = R$).")
    elif es_L_puro:
        st.write("Sin resistencia, el fasor de Impedancia Z (rojo) coincide con la reactancia inductiva (azul), apuntando verticalmente hacia arriba (+90°).")
    elif es_C_puro:
        st.write("Sin resistencia, la oposición es meramente capacitiva. El fasor Z (rojo) se estira verticalmente hacia abajo sobre el eje imaginario (-90°).")
    elif es_RL:
        st.write(f"El triángulo se dibuja en el **1º Cuadrante**. La reactancia inductiva tira hacia arriba generando un ángulo de desfase positivo de +{format_ar(np.degrees(phi))}°.")
    elif es_RC:
        st.write(f"El triángulo cae en el **4º Cuadrante**. La reactancia capacitiva tira el vector hacia abajo, operando con un ángulo de {format_ar(np.degrees(phi))}°.")
    elif es_RLC:
        if abs(XL - XC) < 1e-4:
            st.write(f"En **Resonancia**, XL y XC se cancelan a cero. El cateto vertical azul desaparece y la impedancia Z (rojo) se acuesta igualando a R.")
        elif XL > XC:
            st.write(f"Como $XL > XC$, la resta es positiva. El vector azul apunta hacia arriba y la impedancia se sitúa en el primer cuadrante con un ángulo positivo.")
        else:
            st.write(f"Como $XC > XL$, la resta da negativa. El vector azul apunta hacia abajo, arrastrando a la impedancia Z al cuarto cuadrante.")

st.divider()


# --- SECCIÓN 6: RESULTADOS CON TOOLTIPS TEÓRICOS ---
st.markdown("## 📈 Resultados Analíticos y Teóricos")
st.caption("Mantené presionado sobre las líneas con el icono (i) para ver las ecuaciones.")

t_z = "Z = sqrt(R² + (XL - XC)²)"
t_phi = "φ = arctan((XL - XC) / R)"
t_i = "Irms = Vrms / Z"
t_x = "XL = 2·π·f·L  |  XC = 1 / (2·π·f·C)"
t_v = "ΔVR = I·R  |  ΔVL = I·XL  |  ΔVC = I·XC"
t_p = "P = I²·R  |  Q = I²·X  |  S = V·I"
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
        ⚠️ El circuito actual no califica para resonancia (requiere L y C activos).
    </div>
    """, unsafe_allow_html=True)

# --- PIE DE PÁGINA Y CONTADOR DE VISITAS DINÁMICO REAL ---
st.divider()

col_pie, col_contador = st.columns([2, 1])

with col_pie:
    st.caption("UTN FRRE - Universidad Tecnológica Nacional Facultad Regional Resistencia | Física II")

with col_contador:
    # Usamos Mojo para contar las visitas reales y Shields para darle el diseño azul (#3498DB)
    url_dinamica_azul = "https://badge.mojotv.cn/api/badge/count?id=simulador-rlc-utn.streamlit.app&theme=cyan"
    
    st.markdown(f"""
    <div style="text-align: right; margin-top: -5px;">
        <img src="{url_dinamica_azul}" alt="Contador de visitas real" style="max-width: 100%; height: auto;"/>
    </div>
    """, unsafe_allow_html=True)
