import streamlit as st
import math

def capacidad_grua_simulada(radio):
    # Esta es una función simulada. En la realidad, se usaría la tabla de carga real de la grúa.
    capacidad_maxima = 50000  # 50 toneladas
    return max(0, capacidad_maxima * (1 - radio / 50))  # Disminuye linealmente hasta 50m

def calcular_plan_izaje(peso_carga, radio_operacion, longitud_pluma):
    capacidad_maxima = capacidad_grua_simulada(radio_operacion)
    momento_carga = peso_carga * radio_operacion
    factor_seguridad = capacidad_maxima / peso_carga if peso_carga > 0 else float('inf')
    angulo_pluma = math.degrees(math.atan(longitud_pluma / radio_operacion))
    porcentaje_carga = (peso_carga / capacidad_maxima) * 100 if capacidad_maxima > 0 else float('inf')
    
    return momento_carga, factor_seguridad, angulo_pluma, porcentaje_carga, capacidad_maxima

st.title("Plan de Izaje para Hidrogrúa")

# Entradas del usuario
peso_carga = st.number_input("Peso de la carga (kg)", min_value=0.0, step=100.0)
radio_operacion = st.number_input("Radio de operación (m)", min_value=0.0, step=0.5)
longitud_pluma = st.number_input("Longitud de la pluma (m)", min_value=0.0, step=1.0)

if st.button("Calcular Plan de Izaje"):
    momento_carga, factor_seguridad, angulo_pluma, porcentaje_carga, capacidad_maxima = calcular_plan_izaje(
        peso_carga, radio_operacion, longitud_pluma
    )
    
    st.subheader("Resultados del Plan de Izaje")
    st.write(f"Capacidad máxima de la grúa en el radio establecido: {capacidad_maxima:.2f} kg")
    st.write(f"Momento de carga: {momento_carga:.2f} kg·m")
    st.write(f"Factor de seguridad: {factor_seguridad:.2f}")
    st.write(f"Ángulo de la pluma: {angulo_pluma:.2f}°")
    st.write(f"Porcentaje de carga: {porcentaje_carga:.2f}%")
    
    if factor_seguridad < 1.5:
        st.warning("¡Advertencia! El factor de seguridad es menor a 1.5. Se recomienda revisar los parámetros de izaje.")
    else:
        st.success("El plan de izaje cumple con el factor de seguridad mínimo recomendado.")
    
    if porcentaje_carga > 100:
        st.error("¡Error! El peso de la carga supera la capacidad máxima de la grúa para el radio establecido.")
    elif porcentaje_carga > 90:
        st.warning("¡Precaución! El peso de la carga está muy cerca de la capacidad máxima de la grúa.")

st.write("Nota: La capacidad de la grúa se calcula automáticamente basada en una simulación simplificada. En la práctica, se debe usar la tabla de carga específica de la grúa.")
