import requests
import streamlit as st

BASE_URL_INTERNATIONAL = "https://api.binance.com"
BASE_URL_US = "https://api.binance.us"


@st.cache(ttl=5, suppress_st_warning=True)
def get_status(region):
    request = BASE_URL_INTERNATIONAL + '/sapi/v1/system/status'
    if region == "US":
        request = BASE_URL_US + '/sapi/v1/system/status'
    st.code(request)
    response = requests.get(request).json()
    st.json(response)
    return response
