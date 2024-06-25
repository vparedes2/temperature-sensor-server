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

# Ejemplo de uso
longitud = 10  # Longitud de la tubería flexible (en metros)
altitud_maxima = 50  # Altitud máxima de la tubería flexible (en metros)
perfil_terreno = [20, 30, 40, 35, 25]  # Perfil del terreno (en metros)

presion = calcular_presion(longitud, altitud_maxima, perfil_terreno)

print(f"Presión en el punto más bajo: {presion:.2f} kPa")

Explicación del código:
 * Función calcular_presion:
   * Esta función recibe como argumentos la longitud de la tubería flexible, la altitud máxima y el perfil del terreno.
   * Calcula la densidad del agua, la gravedad y la presión atmosférica.
   * Calcula la altura máxima absoluta y la altura mínima absoluta.
   * Calcula la diferencia de altura.
   * Calcula la presión en el punto más bajo utilizando la fórmula de la presión hidrostática.
   * Devuelve la presión en kPa.
 * Ejemplo de uso:
   * Se definen variables para la longitud, la altitud máxima y el perfil del terreno.
   * Se llama a la función calcular_presion para calcular la presión en el punto más bajo.
   * Se imprime el resultado en la consola.
Nota:
Este código es un ejemplo básico y no tiene en cuenta todos los factores que pueden afectar la presión en una línea flexible, como la fricción y la viscosidad del agua. Para obtener resultados más precisos, se recomienda utilizar un software de ingeniería hidráulica más avanzado.
