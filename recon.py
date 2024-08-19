import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile
import os

# Configuración de la página de Streamlit
st.set_page_config(page_title="Detección Facial", page_icon="👤", layout="wide")

# Función para detectar caras
def detect_faces(image):
    # Convertir la imagen de PIL a formato OpenCV
    open_cv_image = np.array(image.convert('RGB'))
    open_cv_image = open_cv_image[:, :, ::-1].copy()  # Convertir RGB a BGR

    # Cargar el clasificador pre-entrenado para detección facial
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)

    # Detectar caras
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dibujar rectángulos alrededor de las caras
    for (x, y, w, h) in faces:
        cv2.rectangle(open_cv_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Convertir la imagen de vuelta a formato PIL
    return Image.fromarray(cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2RGB)), len(faces)

# Título de la aplicación
st.title("Detección Facial con OpenCV")

# Descripción
st.write("""
Esta aplicación utiliza OpenCV para detectar caras en imágenes.
Sube una imagen y haz clic en 'Detectar caras' para ver los resultados.
""")

# Subida de archivo
uploaded_file = st.file_uploader("Elige una imagen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Mostrar la imagen original
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen original", use_column_width=True)
    
    # Botón para detectar caras
    if st.button("Detectar caras"):
        # Procesamiento de la imagen
        processed_image, num_faces = detect_faces(image)
        
        # Mostrar resultados
        st.image(processed_image, caption=f"Imagen procesada - {num_faces} cara(s) detectada(s)", use_column_width=True)
        st.success(f"Se han detectado {num_faces} cara(s) en la imagen.")
        
        # Opción para descargar la imagen procesada
        if st.button("Descargar imagen procesada"):
            # Guardar la imagen procesada temporalmente
            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
                processed_image.save(tmp_file.name)
            
            # Ofrecer el archivo para descargar
            with open(tmp_file.name, 'rb') as file:
                st.download_button(
                    label="Descargar",
                    data=file,
                    file_name="imagen_procesada.png",
                    mime="image/png"
                )
            
            # Eliminar el archivo temporal
            os.unlink(tmp_file.name)

# Información adicional
st.sidebar.title("Acerca de")
st.sidebar.info("""
Esta aplicación de detección facial utiliza OpenCV y Streamlit.
Fue creada como un ejemplo de cómo integrar procesamiento de imágenes en una aplicación web sencilla.
""")
st.sidebar.warning("""
Nota: La detección facial se realiza localmente en el servidor.
No se almacenan las imágenes subidas.
""")
