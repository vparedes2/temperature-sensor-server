import streamlit as st
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import io

def recognize_face(image):
    # Convertir la imagen a un array numpy
    image_np = np.array(image)
    
    # Encontrar todas las caras en la imagen
    face_locations = face_recognition.face_locations(image_np)
    
    # Crear una copia de la imagen para dibujar
    image_with_faces = image.copy()
    draw = ImageDraw.Draw(image_with_faces)
    
    # Dibujar rectángulos alrededor de las caras
    for (top, right, bottom, left) in face_locations:
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255), width=2)
    
    return image_with_faces, len(face_locations)

st.title("Reconocimiento Facial")

uploaded_file = st.file_uploader("Elige una imagen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen original", use_column_width=True)
    
    if st.button("Detectar caras"):
        processed_image, num_faces = recognize_face(image)
        st.image(processed_image, caption=f"Imagen procesada - {num_faces} cara(s) detectada(s)", use_column_width=True)
        st.success(f"Se han detectado {num_faces} cara(s) en la imagen.")
