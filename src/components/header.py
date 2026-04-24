import streamlit as st
import base64

def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def header_home():
    img_base64 = get_base64_image("src/—Pngtree—cartoon graduation achievement happiness and_23348423.png")
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; margin-bottm:30px; margin-top:30px;">
            <img src="data:image/png;base64,{img_base64}" width="90" />
            <h1 style="text-align:center; color:#E0E3FF;">SNAP<br>CLASS</h1>
        </div>
    """, unsafe_allow_html=True)

def header_dashboard():
    img_base64 = get_base64_image("src/—Pngtree—cartoon graduation achievement happiness and_23348423.png")
    st.markdown(f"""
        <div class="dashboard-header" style="display:flex; align-items:center; gap:10px;">
            <img src="data:image/png;base64,{img_base64}" width="80" />
            <h1>SNAP<br>CLASS</h1>
        </div>
    """, unsafe_allow_html=True)