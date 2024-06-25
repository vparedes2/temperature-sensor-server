import streamlit as st

def calcular_presion(longitud, altitud_maxima, perfil_terreno):
  """
  Calcula la presión en el punto más bajo de una línea flexible.

  Args:
    longitud: Longitud de la tubería flexible (en metros).
    altitud_maxima: Altitud máxima de la tubería flexible (en metros).
    perfil_terreno: Lista de puntos de altura a lo largo del trazado de la tubería (en metros).

  Returns:
    Presión en el punto más bajo de la tubería flexible (en kPa).
  """

  # Calcular la densidad del agua (en kg/m^3)
  densidad_agua = 1000

  # Calcular la gravedad (en m/s^2)
  gravedad = 9.81

  # Calcular la presión atmosférica (en kPa)
  presion_atmosferica = 101.3

  # Calcular la altura máxima absoluta (en metros)
  altura_maxima_absoluta = altitud_maxima + max(perfil_terreno)

  # Calcular la altura mínima absoluta (en metros)
  altura_minima_absoluta = altitud_maxima + min(perfil_terreno)

  # Calcular la diferencia de altura (en metros)
  diferencia_altura = altura_maxima_absoluta - altura_minima_absoluta

  # Calcular la presión en el punto más bajo (en kPa)
  presion = presion_atmosferica + (densidad_agua * gravedad * diferencia_altura) / 1000

  return presion

def main():
  st.title("Calculadora de presión en tuberías flexibles")

  # Seleccionar la longitud de la tubería
  longitud_opcion = st.selectbox("Longitud de la tubería:", ["10 pulgadas", "12 pulgadas"])
  if longitud_opcion == "10 pulgadas":
    longitud = 0.254  # Convertir pulgadas a metros
  else:
    longitud = 0.305  # Convertir pulgadas a metros

  # Ingresar la altitud máxima
  altitud_maxima = st.number_input("Altitud máxima (en metros):")

  # Ingresar el perfil del terreno
  perfil_terreno = st.number_input("Perfil del terreno (en metros, separados por comas):", key="perfil_terreno")
  perfil_terreno = [float(valor) for valor in perfil_terreno.split(",")]

  # Calcular la presión
  if st.button("Calcular presión"):
    presion = calcular_presion(longitud, altitud_maxima, perfil_terreno)
    st.write(f"Presión en el punto más bajo: {presion:.2f} kPa")

if __name__ == "__main__":
  main()
