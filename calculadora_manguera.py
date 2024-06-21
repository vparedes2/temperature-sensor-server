import streamlit as st
import math

def calcular_volumen(diametro, longitud, nivel):
    radio = diametro / 2 / 39.37  # Convertir pulgadas a metros
    area_total = math.pi * radio**2
    
    if nivel == 100:
        area_seccion = area_total
    else:
        angulo = 2 * math.acos(1 - 2 * nivel / 100)
        area_seccion = (angulo - math.sin(angulo)) * radio**2 / 2
    
    volumen = area_seccion * longitud
    return volumen

st.title("Calculadora de Contenido de Fluido en Mangueras")

diametro = st.selectbox("Seleccione el diámetro de la manguera:", [12, 10])
longitud = st.number_input("Ingrese la longitud de la manguera (metros):", min_value=0.1, value=1.0, step=0.1)
nivel = st.selectbox("Seleccione el nivel de llenado %:", [25, 50, 75, 100])

if st.button("Calcular"):
    volumen = calcular_volumen(diametro, longitud, nivel)
    
    st.subheader("Resultados:")
    st.write(f"Diámetro de la manguera: {diametro} pulgadas")
    st.write(f"Longitud de la manguera: {longitud} metros")
    st.write(f"Nivel de llenado: {nivel}%")
    st.write(f"Volumen de fluido: {volumen:.2f} metros cúbicos")
    st.write(f"Volumen de fluido: {volumen * 1000:.2f} litros")

st.write("Nota: Este cálculo asume que la manguera está en posición horizontal y que el fluido se distribuye uniformemente.")
