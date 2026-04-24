import streamlit as st
from supabase import create_client , Client
import httpx

custom_client = httpx.Client(transport=httpx.HTTPTransport(local_address="0.0.0.0"))

supabase : Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)