import streamlit as st
import pandas as pd
import plotly.express as px
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime, timedelta

# Configuración de la página
st.set_page_config(page_title="CEDEAR Cotizaciones", layout="wide")

# Título de la aplicación
st.title("CEDEAR Cotizaciones")

# Clave API de Alpha Vantage
API_KEY = st.secrets["ALPHA_VANTAGE_API_KEY"]

# Lista de CEDEARs
cedears = [
    "AAPL.BA", "MSFT.BA", "GOOGL.BA", "AMZN.BA", "META.BA",
    "TSLA.BA", "NFLX.BA", "NVDA.BA", "PYPL.BA", "INTC.BA"
]

# Función para obtener los precios actuales
@st.cache_data(ttl=300)
def get_prices():
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    data = {}
    for cedear in cedears:
        try:
            df, _ = ts.get_daily(symbol=cedear, outputsize='compact')
            if not df.empty:
                data[cedear] = df['4. close'].iloc[0]
            else:
                data[cedear] = None
        except Exception as e:
            st.error(f"Error al obtener datos para {cedear}: {str(e)}")
            data[cedear] = None
    return pd.DataFrame(list(data.items()), columns=['Símbolo', 'Precio'])

# Botón para actualizar precios
if st.button("Actualizar precios"):
    st.experimental_rerun()

# Mostrar tabla de precios
prices_df = get_prices()
st.dataframe(prices_df)

# Selección de CEDEAR para el gráfico
selected_cedear = st.selectbox("Selecciona un CEDEAR para ver el gráfico", cedears)

# Función para obtener datos históricos
@st.cache_data(ttl=3600)
def get_historical_data(symbol):
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    data = data.sort_index()  # Asegurarse de que los datos estén ordenados cronológicamente
    return data.tail(30)  # Devolver los últimos 30 días

# Mostrar gráfico
if selected_cedear:
    data = get_historical_data(selected_cedear)
    
    fig = px.line(data, x=data.index, y='4. close', title=f"Variación de precio - {selected_cedear}")
    fig.update_layout(
        xaxis_title="Fecha",
        yaxis_title="Precio",
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # Mostrar variaciones
    st.subheader("Variaciones")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        daily_change = (data['4. close'].iloc[-1] - data['4. close'].iloc[-2]) / data['4. close'].iloc[-2] * 100
        st.metric("Variación diaria", f"{daily_change:.2f}%")
    
    with col2:
        weekly_change = (data['4. close'].iloc[-1] - data['4. close'].iloc[-5]) / data['4. close'].iloc[-5] * 100
        st.metric("Variación semanal", f"{weekly_change:.2f}%")
    
    with col3:
        monthly_change = (data['4. close'].iloc[-1] - data['4. close'].iloc[0]) / data['4. close'].iloc[0] * 100
        st.metric("Variación mensual", f"{monthly_change:.2f}%")
