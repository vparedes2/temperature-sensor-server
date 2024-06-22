import streamlit as st
import math

def calcular_plan_izaje(peso_carga, radio_operacion, longitud_pluma, capacidad_maxima):
    momento_carga = peso_carga * radio_operacion
    factor_seguridad = capacidad_maxima / peso_carga if peso_carga > 0 else float('inf')
    angulo_pluma = math.degrees(math.atan(longitud_pluma / radio_operacion))
    porcentaje_carga = (peso_carga / capacidad_maxima) * 100 if capacidad_maxima > 0 else float('inf')
    
    return momento_carga, factor_seguridad, angulo_pluma, porcentaje_carga

st.title("Plan de Izaje para Hidrogrúa")

# Entradas del usuario
peso_carga = st.number_input("Peso de la carga (kg)", min_value=0.0, step=100.0)
radio_operacion = st.number_input("Radio de operación (m)", min_value=0.0, step=0.5)
longitud_pluma = st.number_input("Longitud de la pluma (m)", min_value=0.0, step=1.0)
capacidad_maxima = st.number_input("Capacidad máxima de la grúa en el radio establecido (kg)", min_value=0.0, step=100.0)

if st.button("Calcular Plan de Izaje"):
    momento_carga, factor_seguridad, angulo_pluma, porcentaje_carga = calcular_plan_izaje(
        peso_carga, radio_operacion, longitud_pluma, capacidad_maxima
    )
    
    st.subheader("Resultados del Plan de Izaje")
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

st.write("Nota: Asegúrese de ingresar la capacidad máxima de la grúa correcta para el radio de operación especificado, según la tabla de carga del fabricante.")
st.write("Creado por Lic. Paredes Victor.")
