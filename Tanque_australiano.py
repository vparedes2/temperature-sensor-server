import streamlit as st
import math

def calcular_contenido(nivel_vacio, tipo_tanque):
    # Definir el volumen total según el tipo de tanque
    volumen_total = 5400 if tipo_tanque == "5400 m³" else 4100
    
    # Calcular el radio del tanque
    radio = math.sqrt(volumen_total / (3 * math.pi))
    
    # Calcular la altura del agua (3m - nivel de vacío)
    altura_agua = 3 - (nivel_vacio / 100)
    
    # Calcular el volumen de agua
    volumen_agua = math.pi * (radio ** 2) * altura_agua
    
    # Asegurar que el volumen de agua no exceda el volumen total del tanque
    volumen_agua = min(volumen_agua, volumen_total)
    
    # Calcular el área de la base
    area_base = math.pi * (radio ** 2)
    
    return volumen_agua, area_base

st.title("Calculadora de Tanques Australianos")

# Entrada de datos
nivel_vacio = st.number_input("Nivel de vacío (cm):", min_value=0.0, max_value=300.0, step=0.1)
tipo_tanque = st.selectbox("Tipo de tanque:", ["5400 m³", "4100 m³"])

if st.button("Calcular"):
    volumen_agua, area_base = calcular_contenido(nivel_vacio, tipo_tanque)
    
    st.success(f"Contenido de agua: {volumen_agua:.2f} m³")
    st.info(f"Área de la base: {area_base:.2f} m²")

# Agregar información adicional
st.markdown("---")
st.markdown("""
## Información sobre los tanques australianos

Los tanques australianos son estructuras de almacenamiento de agua utilizadas principalmente en zonas rurales. 
Características:
- Altura: 3 metros
- Capacidades: 5400 m³ o 4100 m³
- Forma: Cilíndrica

El nivel de vacío se mide desde la parte superior del tanque hasta el nivel del agua.
- 0 cm de vacío significa que el tanque está completamente lleno.
- 300 cm de vacío significa que el tanque está completamente vacío.
""")
