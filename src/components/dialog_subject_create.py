import streamlit as st
from src.database.db import create_subject

@st.dialog("Create Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new subject")
    sub_id = st.text_input("Enter the subject code", placeholder="CS01")
    sub_name = st.text_input("Enter the subject name", placeholder="Introduction to Computer Science")
    sub_sem = st.text_input("Semester" , placeholder="Semester 1")

    if st.button("Create Subject" , type='primary', width='stretch'):
        if sub_id and sub_name and sub_sem:
            try:
                create_subject(sub_id , sub_name , sub_sem , teacher_id)
                st.toast("Subject Created Succesfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error : {str(e)}")
        else:
            st.warning("Please fill aLL the details")