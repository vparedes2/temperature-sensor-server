import streamlit as st
import tempfile
from PIL import Image
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

# Configuración de la página
st.set_page_config(page_title="Generador de Reportes", layout="wide")

# Título de la aplicación
st.title("Generador de Reportes")

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

    # Agregar comentario de texto
    st.write("Escribe tu comentario para el reporte:")
    comment = st.text_area("Comentario", height=150)

    # Formulario para enviar por correo
    st.subheader("Enviar reporte por correo")
    to_email = st.text_input("Correo electrónico del destinatario")
    subject = st.text_input("Asunto del correo")

    if st.button("Enviar reporte"):
        if to_email and subject and comment:
            try:
                # Guardar la imagen en un archivo temporal
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_image:
                    # Convertir la imagen a RGB antes de guardarla como JPEG
                    rgb_image = image.convert('RGB')
                    rgb_image.save(temp_image.name, format="JPEG")

                # Enviar el correo
                body = f"Comentario del reporte:\n\n{comment}"
                send_email(to_email, subject, body, temp_image.name)
                st.success("Reporte enviado con éxito")

                # Limpiar archivo temporal
                os.unlink(temp_image.name)
            except Exception as e:
                st.error(f"Error al enviar el correo: {str(e)}")
        else:
            st.warning("Por favor, completa todos los campos antes de enviar el reporte.")
