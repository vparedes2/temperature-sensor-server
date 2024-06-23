import streamlit as st
import os
import tempfile
from PIL import Image
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Configuración de la página
st.set_page_config(page_title="Generador de Reportes", layout="wide")

# Título de la aplicación
st.title("Generador de Reportes")

# Función para grabar audio
def record_audio(duration):
    fs = 44100  # Frecuencia de muestreo
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    return recording, fs

# Función para transcribir audio
def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio, language="es-ES")
        return text
    except sr.UnknownValueError:
        return "No se pudo transcribir el audio"
    except sr.RequestError:
        return "Error en la solicitud de transcripción"

# Función para enviar correo electrónico
def send_email(to_email, subject, body, image_path):
    # Configuración del servidor SMTP (ejemplo con Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "vparedes2@gmail.com"
    smtp_password = "oicirbaf"

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Agregar el cuerpo del mensaje
    msg.attach(MIMEText(body, 'plain'))

    # Agregar la imagen
    with open(image_path, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(image_path))
        msg.attach(img)

    # Enviar el correo
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

# Subir imagen
uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen subida', use_column_width=True)

    # Grabar audio
    st.write("Presiona el botón para grabar tu comentario (máximo 30 segundos)")
    if st.button("Grabar"):
        with st.spinner("Grabando..."):
            audio, fs = record_audio(30)  # Grabar por 30 segundos
        st.success("Grabación completada")

        # Guardar el audio en un archivo temporal
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            wav.write(temp_audio.name, fs, audio)

        # Transcribir el audio
        transcription = transcribe_audio(temp_audio.name)
        st.write("Transcripción:")
        st.write(transcription)

        # Formulario para enviar por correo
        st.subheader("Enviar reporte por correo")
        to_email = st.text_input("Correo electrónico del destinatario")
        subject = st.text_input("Asunto del correo")

        if st.button("Enviar reporte"):
            try:
                # Guardar la imagen en un archivo temporal
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_image:
                    image.save(temp_image.name, format="JPEG")

                # Enviar el correo
                body = f"Transcripción del comentario:\n\n{transcription}"
                send_email(to_email, subject, body, temp_image.name)
                st.success("Reporte enviado con éxito")

                # Limpiar archivos temporales
                os.unlink(temp_audio.name)
                os.unlink(temp_image.name)
            except Exception as e:
                st.error(f"Error al enviar el correo: {str(e)}")
