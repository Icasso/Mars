import requests
import streamlit as st

BASE_URL = "https://www.okx.com"


@st.cache(ttl=5, suppress_st_warning=True)
def get_status():
    status_list = []
    request = BASE_URL + '/api/v5/system/status'
    st.code(request)
    response = requests.get(request)
    data = response.json()
    st.json(data)
    if data['code'] != "0":
        print(f"Error: {data['code']}")
        return None
    else:
        res = data['data']
        for s in res:
            status_list.append(s)
        return status_list
