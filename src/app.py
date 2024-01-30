"""

"""
import streamlit as st

st.image("image/neurona.jpg")
st.title('¡Hola neurona!')
tab1, tab2, tab3 = st.tabs(["Una entrada",
                            "Dos entradas",
                            "Tres entradas y sesgo"])

with tab1:
    if tab1:
        w0 = st.slider(label='Peso', min_value=0.0, max_value=5.0, key='t1w0')
        x0 = st.number_input(label='Entrada', min_value=0.0, max_value=5.0, key='t1x0',)
        if st.button(label='Calcular la salida', key='t1_button'):
            y = x0*w0
            st.write('La salida de la neurona es ', str(y))

with tab2:
    col1, col2 = st.columns(2)
    if tab2:
        with col1:
            st.markdown("Peso w<sub>0</sub>", unsafe_allow_html=True)
            w0 = st.slider(label='t2_w0', label_visibility='collapsed', min_value=0.0, max_value=5.0, key='t2_w0')
            st.markdown("Entrada x<sub>0</sub>", unsafe_allow_html=True)
            x0 = st.number_input(label='t2_x0', label_visibility='collapsed', min_value=0.0, max_value=5.0, key='t2_x0')
        with col2:
            st.markdown("Peso w<sub>1</sub>", unsafe_allow_html=True)
            w1 = st.slider(label='t2_w1', label_visibility='collapsed', min_value=0.0, max_value=5.0, key='t2_w1')
            st.markdown("Entrada x<sub>1</sub>", unsafe_allow_html=True)
            x1 = st.number_input(label='t2x1', label_visibility='collapsed', min_value=0.0, max_value=5.0, key='t2_x1')

        
        if st.button(label='Calcular la salida', key='t2_button'):
            y = x0*w0 + x1*w1
            st.write('La salida de la neurona es ', str(y))

with tab3:
    col1, col2, col3 = st.columns(3)
    if tab3:
        with col1:
            st.markdown("Peso w<sub>0</sub>", unsafe_allow_html=True)
            w0 = st.slider(label='t3_w0', label_visibility='collapsed', min_value=0.0, max_value=5.0, key='t3_w0')
            st.markdown("Entrada x<sub>0</sub>", unsafe_allow_html=True)
            x0 = st.number_input(label='t3_x0', label_visibility='collapsed', min_value=0.0, max_value=5.0, key='t3_x0')
        with col2:
            st.markdown("Peso w<sub>1</sub>", unsafe_allow_html=True)
            w1 = st.slider(label='t3_w1', label_visibility='collapsed', min_value=0.0, max_value=5.0, key='t3_w1')
            st.markdown("Entrada x<sub>1</sub>", unsafe_allow_html=True)
            x1 = st.number_input(label='t3_x1', label_visibility='collapsed', min_value=0.0, max_value=5.0, key='t3_x1')
        with col3:
            st.markdown("Peso w<sub>1</sub>", unsafe_allow_html=True)
            w2 = st.slider(label='t3_w2', label_visibility='collapsed', min_value=0.0, max_value=5.0, key='t3_w2')
            st.markdown("Entrada x<sub>2</sub>", unsafe_allow_html=True)
            x2 = st.number_input(label='t3_x2', label_visibility='collapsed', min_value=0.0, max_value=5.0, key='t3_x2')

        bias = st.number_input("Introduzca el valor del sesgo", 0.0, 5.0, key='bias')

        if st.button(label='Calcular la salida'):
            y = x0*w0 + x1*w1 + x2*w2 + bias
            st.write('La salida de la neurona es ', str(y))
