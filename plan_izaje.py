import streamlit as st
import math

def calcular_plan_izaje(peso_carga, radio_operacion, capacidad_grua, longitud_pluma):
    # Cálculos básicos
    momento_carga = peso_carga * radio_operacion
    factor_seguridad = capacidad_grua / momento_carga
    angulo_pluma = math.degrees(math.atan(longitud_pluma / radio_operacion))
    
    return momento_carga, factor_seguridad, angulo_pluma

st.title("Plan de Izaje para Hidrogrúa - Rio Limay OFS")

# Entradas del usuario
peso_carga = st.number_input("Peso de la carga (kg)", min_value=0.0, step=100.0)
radio_operacion = st.number_input("Radio de operación (m)", min_value=0.0, step=0.5)
capacidad_grua = st.number_input("Capacidad de la grúa (kg-m)", min_value=0.0, step=1000.0)
longitud_pluma = st.number_input("Longitud de la pluma (m)", min_value=0.0, step=1.0)

if st.button("Calcular Plan de Izaje"):
    momento_carga, factor_seguridad, angulo_pluma = calcular_plan_izaje(
        peso_carga, radio_operacion, capacidad_grua, longitud_pluma
    )
    
    st.subheader("Resultados del Plan de Izaje")
    st.write(f"Momento de carga: {momento_carga:.2f} kg-m")
    st.write(f"Factor de seguridad: {factor_seguridad:.2f}")
    st.write(f"Ángulo de la pluma: {angulo_pluma:.2f}°")
    
    if factor_seguridad < 1.5:
        st.warning("¡Advertencia! El factor de seguridad es menor a 1.5. Se recomienda revisar los parámetros de izaje.")
    else:
        st.success("El plan de izaje cumple con el factor de seguridad mínimo recomendado.")
