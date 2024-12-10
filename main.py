
import math
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def ingreso_datos_streamlit():
    st.title("Simulador de Paneles Solares")
    consumo_mensual_kwh = st.number_input("Consumo mensual promedio (kWh):", min_value=0.0, step=10.0)
    radiacion_diaria_promedio = st.number_input("Radiación solar diaria promedio (kWh/m²):", min_value=0.0, step=0.1)
    potencia_panel = st.number_input("Potencia de cada panel solar (Wp):", min_value=0.0, step=50.0)
    area_disponible = st.number_input("Área disponible para paneles (m²):", min_value=0.0, step=1.0)
    dimension_panel = st.number_input("Área de cada panel solar (m²):", min_value=0.0, step=0.1)
    costo_panel = st.number_input("Costo por panel solar (USD):", min_value=0.0, step=10.0)
    costo_inversor = st.number_input("Costo del inversor (USD):", min_value=0.0, step=10.0)
    mano_obra = st.number_input("Costo de instalación por panel (USD):", min_value=0.0, step=10.0)

    return {
        "consumo_mensual_kwh": consumo_mensual_kwh,
        "radiacion_diaria_promedio": radiacion_diaria_promedio,
        "potencia_panel": potencia_panel,
        "area_disponible": area_disponible,
        "dimension_panel": dimension_panel,
        "costo_panel": costo_panel,
        "costo_inversor": costo_inversor,
        "mano_obra": mano_obra
    }

def calculos(datos):
    eficiencia_panel = 0.85
    consumo_diario_kwh = datos["consumo_mensual_kwh"] / 30
    energia_necesaria_kwh = consumo_diario_kwh / eficiencia_panel
    numero_paneles = math.ceil(energia_necesaria_kwh / (datos["radiacion_diaria_promedio"] * (datos["potencia_panel"] / 1000)))
    area_requerida = numero_paneles * datos["dimension_panel"]
    costo_total_paneles = numero_paneles * datos["costo_panel"]
    costo_total_mano_obra = numero_paneles * datos["mano_obra"]
    costo_total = costo_total_paneles + datos["costo_inversor"] + costo_total_mano_obra
    ahorro_mensual = datos["consumo_mensual_kwh"] * 0.12
    roi = costo_total / (ahorro_mensual * 12)
    return {
        "Número de paneles": numero_paneles,
        "Área requerida (m²)": area_requerida,
        "Costo total (USD)": costo_total,
        "Retorno de inversión (años)": roi
    }

def mostrar_resultados_streamlit(resultados):
    st.subheader("Resultados del Sistema Solar")
    for key, value in resultados.items():
        st.write(f"{key}: {value:.2f}")
    conceptos = list(resultados.keys())
    valores = list(resultados.values())
    plt.bar(conceptos, valores, color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.title('Resultados del Sistema Solar')
    plt.ylabel('Valores')
    plt.tight_layout()
    st.pyplot(plt)

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
