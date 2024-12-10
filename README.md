# solar-simulator
# Simulador de Instalación Solar Fotovoltaica

Este proyecto es una aplicación interactiva desarrollada en Python utilizando Streamlit. Permite realizar cálculos técnicos para la instalación de sistemas de paneles solares, incluyendo la disposición de paneles, costos, y retorno de inversión.

## Funcionalidades
- Ingreso de datos personalizados sobre el sistema fotovoltaico.
- Cálculo del número de paneles necesarios y su disposición.
- Dimensionamiento de inversores.
- Estimación del costo total del sistema.
- Cálculo del retorno de inversión (ROI).
- Visualización de la disposición de paneles solares.
- Generación de un archivo CSV con los resultados.

## Requisitos
- Python 3.8 o superior
- Librerías necesarias:
  - `streamlit`
  - `pandas`
  - `matplotlib`

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/solar-installation-simulator.git
   cd solar-installation-simulator
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   streamlit run solar_installation_tool.py
   ```

## Uso
1. Ingresa los datos requeridos en la interfaz:
   - Consumo mensual promedio en kWh.
   - Irradiación solar promedio diaria.
   - Detalles del panel solar (potencia, tensión, corriente, costo).
   - Detalles del inversor (capacidad, tensión máxima, corriente máxima, costo).
   - Costo de instalación por panel.

2. Presiona el botón "Calcular" para generar los resultados:
   - Número de paneles necesarios.
   - Potencia total del sistema.
   - Disposición de paneles.
   - Costo total y retorno de inversión.

3. Descarga los resultados generados en formato CSV.

## Visualización de la Disposición de Paneles
La aplicación genera una visualización gráfica mostrando cómo se organizarían los paneles solares en un espacio determinado.

## Contribución
Si deseas contribuir a este proyecto:
1. Haz un fork del repositorio.
2. Crea una rama nueva para tu funcionalidad: `git checkout -b nueva-funcionalidad`.
3. Realiza tus cambios y haz un commit: `git commit -m 'Añadir nueva funcionalidad'`.
4. Envía un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.


