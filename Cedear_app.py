import streamlit as st
import pandas_datareader as pdr
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuración de la página
st.set_page_config(page_title="CEDEAR Cotizaciones", layout="wide")

# Título de la aplicación
st.title("CEDEAR Cotizaciones")

# Lista de CEDEARs
cedears = [
    "AAPL.BA", "MSFT.BA", "GOOGL.BA", "AMZN.BA", "META.BA",
    "TSLA.BA", "NFLX.BA", "NVDA.BA", "PYPL.BA", "INTC.BA"
]

# Función para obtener los precios actuales
@st.cache_data(ttl=300)
def get_prices():
    data = {}
    end_date = datetime.now()
    start_date = end_date - timedelta(days=1)
    for cedear in cedears:
        try:
            df = pdr.get_data_yahoo(cedear, start=start_date, end=end_date)
            if not df.empty:
                data[cedear] = df['Close'].iloc[-1]
            else:
                data[cedear] = None
        except:
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
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    data = pdr.get_data_yahoo(symbol, start=start_date, end=end_date)
    return data

# Mostrar gráfico
if selected_cedear:
    data = get_historical_data(selected_cedear)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Precio de cierre'))
    
    fig.update_layout(
        title=f"Variación de precio - {selected_cedear}",
        xaxis_title="Fecha",
        yaxis_title="Precio",
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # Mostrar variaciones
    st.subheader("Variaciones")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        daily_change = (data['Close'][-1] - data['Close'][-2]) / data['Close'][-2] * 100
        st.metric("Variación diaria", f"{daily_change:.2f}%")
    
    with col2:
        weekly_change = (data['Close'][-1] - data['Close'][-5]) / data['Close'][-5] * 100
        st.metric("Variación semanal", f"{weekly_change:.2f}%")
    
    with col3:
        monthly_change = (data['Close'][-1] - data['Close'][0]) / data['Close'][0] * 100
        st.metric("Variación mensual", f"{monthly_change:.2f}%")
