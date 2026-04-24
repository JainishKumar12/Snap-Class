import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout , style_background_home , style_background_dashboard

def home_screen():  
    header_home()
    style_base_layout()
    style_background_home()  

    col1 , col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Teacher")
        st.image("src/image_38f29397-removebg-preview.png", width=125)
        if st.button("Teacher portal", type='primary', icon=":material/arrow_outward:" , icon_position='right'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
    with col2:
        st.header("I'm Student")
        st.image("src\Download_this_free_vector_of_Ai_Generated_Student_Schoolboy_from_Pixabay_s_vast_library_of_royalty-free_stock_images__videos_and_music_-removebg-preview.png", width=90)
        if st.button("Student portal", type='primary' , icon=":material/arrow_outward:" ,icon_position='right'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    footer_home()