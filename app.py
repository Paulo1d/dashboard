import streamlit as st
import pandas as pd
import plotly.express as px


 # Configurar layout do Streamlit
st.set_page_config(layout="wide")

# Estilos CSS
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: white !important;
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Título do Dashboard
st.markdown("<h1 style='text-align: center; color: black;'>🚢 DP ASSURANCE</h1>", unsafe_allow_html=True)

# Dados para o KPI 1 - Gráfico de Barras com todas as barras do mesmo tamanho
df_kpi1 = pd.DataFrame({
    "Vessels": ["Amy Chouest", "Bram Buccaneer", "Bram Buck", "Bram Hero", "C- Atlas", "C- Sailor", "Campos Commander", "Mr. Chafic", "Campos Clipper", "Oryx", "Reedbuck"],
    "Quantidade": [1] * 11  # Todas as barras do mesmo tamanho
})
fig1 = px.bar(df_kpi1, x="Vessels", y="Quantidade", title="🛳 Embarcações Pendentes",
              color_discrete_sequence=["#0077b6"])

# Dados para o KPI 2 - Gráfico de Pizza
df_pizza = pd.DataFrame({
    "Status": ["Pendentes", "Concluídas"],
    "Quantidade": [11, 39]
})
fig2 = px.pie(df_pizza, names="Status", values="Quantidade", title="🛳 Embarcações Pendentes vs Concluídas",
              color_discrete_sequence=["#0077b6", "#00a8e8"])

# Dados para o KPI 3 - Embarcações por Quantidade de Pendências
df_pendencias = pd.DataFrame({
    "Vessels": ["Bram Atlas", "Bram Bahia", "Bram Boa Vista", "Bram Natal", "Bushbuck", "C- Warrior"],
    "Pendências": [4, 4, 4, 2, 3, 1]
})
fig3 = px.bar(df_pendencias, x="Vessels", y="Pendências", title="⚠️ Pendências por Embarcação",
              color_discrete_sequence=["#0077b6"])

# Dados para o KPI 4 - Gráfico de Dispersão
df_grafico4 = pd.DataFrame({
    "Vessels": ["Bram Force", "Bram Spirit", "Bruce Kay", "Campos Carrier", "Campos Challenger", "Corcovado"],
    "Ano": [2024, 2024, 2024, 2024, 2024, 2024]
})
fig4 = px.scatter(df_grafico4, x="Vessels", y="Ano", title="📅 Embarcações com Report Pendentes",
                  color_discrete_sequence=["#0077b6"])

# Layout Profissional - 2 KPIs em cima, 2 embaixo
st.markdown("<h3 style='text-align: center; color: black;'>KPIs Principais</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.plotly_chart(fig4, use_container_width=True)