import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Función para cargar imágenes desde URL
def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# Configuración de la página
st.set_page_config(page_title="Aplicaciones Rio Limay Oil Field Services", layout="wide")

# Estilo CSS personalizado
st.markdown("""
    <style>
    .stApp {
        max-width: 1000px;
        margin: 0 auto;
        font-family: Arial, sans-serif;
    }
    .app-card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        padding: 15px;
        margin-bottom: 20px;
    }
    .app-card img {
        width: 100%;
        object-fit: cover;
    }
    .app-card h3 {
        color: #2c3e50;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
logo_url = "https://i.ibb.co/r0gxVDP/logo-RL2-1.jpg"
st.image(logo_url, width=300)
st.title("Aplicaciones de Cálculo")

# Contenedor de aplicaciones
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.image("https://i.ibb.co/FDsd5sf/Calendario-2023-Rio-Limay-18-15-cm-4.png", use_column_width=True)
    st.header("Calculadora Volumen de Tanques")
    st.write("Calcula el volumen de tanques australianos para almacenamiento de agua de fractura de 5000m³.")
    st.markdown('[Abrir Calculadora](https://tinyurl.com/volumentanques)')
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.image("https://i.ibb.co/wdsgDd9/Elementos-que-complementan-a-las-gruas-de-izaje.jpg", use_column_width=True)
    st.header("Plan de Izaje")
    st.write("Herramienta para planificar operaciones de izaje con hidrogrúas.")
    st.markdown('[Abrir Plan de Izaje](https://tinyurl.com/PlanIzajerl)')
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="app-card">', unsafe_allow_html=True)
    st.image("https://i.imgur.com/example3.jpg", use_column_width=True)
    st.header("Calculadora Volumen Mangueras")
    st.write("Calcula el volumen de mangueras layflat de 12 pulgadas en una tirada en Vaca Muerta.")
    st.markdown('[Abrir Calculadora](https://tinyurl.com/Mangueras)')
    st.markdown('</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("Creado por Lic. Victor PAREDES")
