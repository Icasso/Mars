import requests
import streamlit as st

BASE_URL = "https://api.kucoin.com"


@st.cache(ttl=5, suppress_st_warning=True)
def get_status():
    request = BASE_URL + '/api/v1/status'
    st.code(request)
    response = requests.get(request).json()
    st.json(response)
    return response
