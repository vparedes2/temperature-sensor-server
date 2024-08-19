import streamlit as st
import cv2
import numpy as np
from PIL import Image

def detect_faces(image):
    # Convertir la imagen de PIL a formato OpenCV
    open_cv_image = np.array(image.convert('RGB'))
    open_cv_image = open_cv_image[:, :, ::-1].copy()  # Convert RGB to BGR

    # Cargar el clasificador pre-entrenado para detección facial
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)

    # Detectar caras
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Dibujar rectángulos alrededor de las caras
    for (x, y, w, h) in faces:
        cv2.rectangle(open_cv_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Convertir la imagen de vuelta a formato PIL
    return Image.fromarray(cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2RGB)), len(faces)

st.title("Detección Facial con OpenCV")

uploaded_file = st.file_uploader("Elige una imagen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen original", use_column_width=True)
    
    if st.button("Detectar caras"):
        processed_image, num_faces = detect_faces(image)
        st.image(processed_image, caption=f"Imagen procesada - {num_faces} cara(s) detectada(s)", use_column_width=True)
        st.success(f"Se han detectado {num_faces} cara(s) en la imagen.")
