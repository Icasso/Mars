import requests
import streamlit as st

BASE_URL = "https://api.kraken.com/0"


@st.cache(ttl=5, suppress_st_warning=True)
def get_status():
    request = BASE_URL + '/public/SystemStatus'
    st.code(request)
    response = requests.get(request).json()
    st.json(response)
    return response
