import streamlit as st
from PIL import Image
import io

# Configuración de la página de Streamlit
st.set_page_config(page_title="Visualizador de Imágenes", page_icon="🖼️", layout="wide")

# Título de la aplicación
st.title("Visualizador de Imágenes Simple")

# Descripción
st.write("""
Esta aplicación te permite cargar y visualizar imágenes.
Sube una imagen para verla en la pantalla.
""")

# Subida de archivo
uploaded_file = st.file_uploader("Elige una imagen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Abrir la imagen
    image = Image.open(uploaded_file)
    
    # Mostrar la imagen
    st.image(image, caption="Imagen cargada", use_column_width=True)
    
    # Información de la imagen
    st.write(f"Dimensiones de la imagen: {image.size[0]} x {image.size[1]} píxeles")
    st.write(f"Formato de la imagen: {image.format}")
    
    # Opción para descargar la imagen
    if st.button("Descargar imagen"):
        # Guardar la imagen en un buffer
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        # Ofrecer el archivo para descargar
        st.download_button(
            label="Descargar imagen",
            data=byte_im,
            file_name="imagen.png",
            mime="image/png"
        )

# Información adicional
st.sidebar.title("Acerca de")
st.sidebar.info("""
Esta aplicación simple de visualización de imágenes utiliza Streamlit y Pillow.
Fue creada como un ejemplo básico de cómo manejar imágenes en una aplicación web sencilla.
""")
st.sidebar.warning("""
Nota: Las imágenes se procesan localmente y no se almacenan permanentemente.
""")
