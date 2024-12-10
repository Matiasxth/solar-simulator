import math
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Base de datos de paneles solares e inversores
paneles_db = pd.DataFrame({
    "Modelo": ["Panel A", "Panel B", "Panel C"],
    "Potencia (Wp)": [400, 450, 500],
    "Dimensiones (m²)": [1.94, 2.05, 2.15],
    "Costo (USD)": [200, 250, 300]
})

inversores_db = pd.DataFrame({
    "Modelo": ["Inversor A", "Inversor B", "Inversor C"],
    "Capacidad (kW)": [3, 5, 10],
    "Costo (USD)": [500, 800, 1500]
})

def ingreso_datos_streamlit():
    st.title("Simulador de Paneles Solares")
    consumo_mensual_kwh = st.number_input("Consumo mensual promedio (kWh):", min_value=0.0, step=10.0)
    radiacion_diaria_promedio = st.number_input("Radiación solar diaria promedio (kWh/m²):", min_value=0.0, step=0.1)
    area_disponible = st.number_input("Área disponible para paneles (m²):", min_value=0.0, step=1.0)
    mano_obra = st.number_input("Costo de instalación por panel (USD):", min_value=0.0, step=10.0)

    st.subheader("Selección de Panel Solar")
    panel_seleccionado = st.selectbox("Selecciona un panel solar:", paneles_db["Modelo"])
    panel = paneles_db[paneles_db["Modelo"] == panel_seleccionado].iloc[0]

    st.subheader("Selección de Inversor")
    inversor_seleccionado = st.selectbox("Selecciona un inversor:", inversores_db["Modelo"])
    inversor = inversores_db[inversores_db["Modelo"] == inversor_seleccionado].iloc[0]

    return {
        "consumo_mensual_kwh": consumo_mensual_kwh,
        "radiacion_diaria_promedio": radiacion_diaria_promedio,
        "area_disponible": area_disponible,
        "mano_obra": mano_obra,
        "panel": panel,
        "inversor": inversor
    }

def calculos(datos):
    eficiencia_panel = 0.85
    consumo_diario_kwh = datos["consumo_mensual_kwh"] / 30
    energia_necesaria_kwh = consumo_diario_kwh / eficiencia_panel
    potencia_panel = datos["panel"]["Potencia (Wp)"] / 1000
    numero_paneles = math.ceil(energia_necesaria_kwh / (datos["radiacion_diaria_promedio"] * potencia_panel))
    area_requerida = numero_paneles * datos["panel"]["Dimensiones (m²)"]
    strings = math.ceil(numero_paneles / (datos["inversor"]["Capacidad (kW)"] * 1000 / datos["panel"]["Potencia (Wp)"]))

    costo_total_paneles = numero_paneles * datos["panel"]["Costo (USD)"]
    costo_total_mano_obra = numero_paneles * datos["mano_obra"]
    costo_total_inversor = datos["inversor"]["Costo (USD)"] * strings
    costo_total = costo_total_paneles + costo_total_mano_obra + costo_total_inversor

    ahorro_mensual = datos["consumo_mensual_kwh"] * 0.12
    roi = costo_total / (ahorro_mensual * 12)

    return {
        "Número de paneles": numero_paneles,
        "Área requerida (m²)": area_requerida,
        "Cantidad de strings": strings,
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
