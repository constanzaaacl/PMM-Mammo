import streamlit as st
from upload_section.upload import subir_mamografia
from stats_section.stats import mostrar_estadisticas

#st.title("Proyecto de Clasificación de Mamografías")
st.markdown(
    "<h1 style='color: #FCC0FF;'>Proyecto de Clasificación de Mamografías</h1>", 
    unsafe_allow_html=True
)


st.write('Integrantes: Constanza Corday, Julio Maturana y Nicolás Ruiz')

# Barra lateral para la navegación
st.sidebar.title(":)")
opcion = st.sidebar.radio("Selecciona:", ("Análisis de Mamografía", "Sobre el Modelo"))

# Mostrar contenido basado en la opción seleccionada
if opcion == "Análisis de Mamografía":
    subir_mamografia()
elif opcion == "Sobre el Modelo":
    mostrar_estadisticas()