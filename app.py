import streamlit as st
import base64

# Configuração da página
st.set_page_config(layout="wide")

# Função para definir a imagem de fundo
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background: url("data:image/png;base64,{encoded_image}") no-repeat center center fixed;
        background-size: cover;
    }}
    .block-container {{
        padding: 3rem;
    }}
    .stButton>button {{
        width: 100%;  /* Tamanho ajustado dos botões */
        height: 120px;  
        background-color: rgba(0,0,0,0); /* Totalmente transparente */
        border: none;  /* Sem bordas brancas */
        cursor: pointer;
    }}
    .button-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 160px;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Aplicar imagem de fundo no dashboard principal
set_background("Frame 1.png")

# Esconder menu e rodapé do Streamlit
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Criar espaçamento para alinhar corretamente os botões
st.markdown("<br>", unsafe_allow_html=True)

# Criar os botões invisíveis que levam para outros dashboards
col1, col2, col3 = st.columns([1, 1, 1], gap="large")  

with col1:
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("", key="btn1"):  # Botão invisível
        st.switch_page("pages/dashboard_1.py")  # Vai para dashboard_1.py
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="button-container">', unsafe_allow_html=True)  
    if st.button("", key="btn2"):
        st.switch_page("pages/dashboard_2.py")  
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("", key="btn3"):
        st.switch_page("pages/dashboard_3.py")  
    st.markdown('</div>', unsafe_allow_html=True)

# Ajustar espaçamento entre os botões
st.markdown("<br>", unsafe_allow_html=True)

col4, col5, col6 = st.columns([1, 1, 1], gap="large")  

with col4:
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("", key="btn4"):
        st.switch_page("pages/dashboard_4.py")  
    st.markdown('</div>', unsafe_allow_html=True)

with col5:
    st.markdown('<div class="button-container">', unsafe_allow_html=True)  
    if st.button("", key="btn5"):
        st.switch_page("pages/dashboard_5.py")  
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("", key="btn6"):
        st.switch_page("pages/dashboard_6.py")  
    st.markdown('</div>', unsafe_allow_html=True)
