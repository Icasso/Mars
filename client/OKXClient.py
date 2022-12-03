import requests
import streamlit as st

BASE_URL = "https://www.okx.com"


@st.cache(ttl=5)
def get_status():
    status_list = []
    response = requests.get(BASE_URL + '/api/v5/system/status')
    data = response.json()
    print(data)
    if data['code'] != "0":
        print(f"Error: {data['code']}")
        return None
    else:
        res = data['data']
        for s in res:
            status_list.append(s)
        return status_list
