import streamlit as st
from PIL import Image

def subir_mamografia():
    st.header("Análisis de Mamografías")
    st.write("Se busca hacer una clasificación en nivel de BI-RADS")
    uploaded_file = st.file_uploader("Sube tu mamografía", type=["dicom"])

    if uploaded_file is not None:
            # Mostrar el nombre del archivo
            st.write(f"Nombre del archivo: {uploaded_file.name}")
            
            # Abrir y mostrar la imagen
            image = Image.open(uploaded_file)
            st.image(image, caption='Mamografía Subida', use_column_width=True)
            
            # Mensaje de análisis
            st.success("¡Analizado correctamente!")