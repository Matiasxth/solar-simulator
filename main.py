import math
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def ingreso_datos_streamlit():
    st.title("Simulador de Instalación Solar Fotovoltaica")

    consumo_mensual_kwh = st.number_input("Consumo mensual promedio (kWh):", min_value=0.0, step=10.0)
    irradiacion_diaria_promedio = st.number_input("Irradiación solar diaria promedio (kWh/m²):", min_value=0.0, step=0.1)
    factor_perdidas = st.slider("Factor de pérdidas del sistema (%):", min_value=0, max_value=30, value=15) / 100

    st.subheader("Datos del Panel Solar")
    potencia_panel_w = st.number_input("Potencia del panel (Wp):", min_value=0.0, step=10.0)
    tension_panel_v = st.number_input("Tensión nominal del panel (V):", min_value=0.0, step=1.0)
    corriente_panel_a = st.number_input("Corriente nominal del panel (A):", min_value=0.0, step=0.1)
    costo_panel = st.number_input("Costo del panel (USD):", min_value=0.0, step=10.0)

    st.subheader("Datos del Inversor")
    capacidad_inversor_kw = st.number_input("Capacidad del inversor (kW):", min_value=0.0, step=0.1)
    tension_max_inversor_v = st.number_input("Tensión máxima del inversor (V):", min_value=0.0, step=1.0)
    corriente_max_inversor_a = st.number_input("Corriente máxima del inversor (A):", min_value=0.0, step=0.1)
    costo_inversor = st.number_input("Costo del inversor (USD):", min_value=0.0, step=10.0)

    mano_obra = st.number_input("Costo de instalación por panel (USD):", min_value=0.0, step=10.0)

    return {
        "consumo_mensual_kwh": consumo_mensual_kwh,
        "irradiacion_diaria_promedio": irradiacion_diaria_promedio,
        "factor_perdidas": factor_perdidas,
        "potencia_panel_w": potencia_panel_w,
        "tension_panel_v": tension_panel_v,
        "corriente_panel_a": corriente_panel_a,
        "costo_panel": costo_panel,
        "capacidad_inversor_kw": capacidad_inversor_kw,
        "tension_max_inversor_v": tension_max_inversor_v,
        "corriente_max_inversor_a": corriente_max_inversor_a,
        "costo_inversor": costo_inversor,
        "mano_obra": mano_obra
    }

def calculos(datos):
    consumo_diario_kwh = datos["consumo_mensual_kwh"] / 30
    potencia_panel_kw = datos["potencia_panel_w"] / 1000
    energia_generada_diaria = potencia_panel_kw * datos["irradiacion_diaria_promedio"] * (1 - datos["factor_perdidas"])
    numero_paneles = math.ceil(consumo_diario_kwh / energia_generada_diaria)

    area_requerida = numero_paneles * (datos["potencia_panel_w"] / datos["tension_panel_v"] * datos["corriente_panel_a"] / 1000)
    potencia_total_sistema_kw = numero_paneles * potencia_panel_kw

    strings = math.ceil(numero_paneles / (datos["capacidad_inversor_kw"] * 1000 / datos["potencia_panel_w"]))

    costo_total_paneles = numero_paneles * datos["costo_panel"]
    costo_total_mano_obra = numero_paneles * datos["mano_obra"]
    costo_total_inversores = strings * datos["costo_inversor"]
    costo_total = costo_total_paneles + costo_total_mano_obra + costo_total_inversores

    ahorro_mensual = datos["consumo_mensual_kwh"] * 0.12  # Tarifa promedio por kWh en USD
    roi = costo_total / (ahorro_mensual * 12)

    return {
        "Número de paneles": numero_paneles,
        "Área requerida (m²)": area_requerida,
        "Potencia total del sistema (kW)": potencia_total_sistema_kw,
        "Cantidad de strings": strings,
        "Costo total (USD)": costo_total,
        "Retorno de inversión (años)": roi
    }

def simular_disposicion_paneles(numero_paneles, columnas=5):
    filas = math.ceil(numero_paneles / columnas)
    fig, ax = plt.subplots(figsize=(10, 6))
    for i in range(filas):
        for j in range(columnas):
            if i * columnas + j < numero_paneles:
                ax.add_patch(plt.Rectangle((j, -i), 1, 1, edgecolor="black", facecolor="skyblue"))
    ax.set_xlim(0, columnas)
    ax.set_ylim(-filas, 0)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("Disposición de los paneles solares")
    return fig

def mostrar_resultados_streamlit(resultados):
    st.subheader("Resultados del Sistema Solar")
    for key, value in resultados.items():
        st.write(f"{key}: {value:.2f}")
    fig = simular_disposicion_paneles(resultados["Número de paneles"])
    st.pyplot(fig)

def guardar_resultados_csv(resultados):
    df = pd.DataFrame([resultados])
    df.to_csv("resultados_solares.csv", index=False)
    st.write("Resultados guardados en 'resultados_solares.csv'. Puedes descargar el archivo desde tu entorno local.")

def main():
    datos = ingreso_datos_streamlit()
    if st.button("Calcular"):
        resultados = calculos(datos)
        mostrar_resultados_streamlit(resultados)
        guardar_resultados_csv(resultados)

if __name__ == "__main__":
    main()
