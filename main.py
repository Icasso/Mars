import streamlit as st
import requests
import datetime
from config import load_config

load_config()


@st.cache
def get_status():
    status_list = []
    data_json = requests.get('https://www.okx.com/api/v5/system/status').json()
    if data_json['code'] != "0":
        return None
    else:
        data = data_json['data']
        for s in data:
            status_list.append(s)
        return status_list


st.title("Project - Mars")

curr_status = get_status()
if curr_status is not None and len(curr_status) != 0:
    st.header('OKX Status')
    count = 0
    for status in curr_status:
        st.write('---')
        title = status['title']
        start = int(status['begin']) / 1000.0
        end = int(status['end']) / 1000.0
        start_date = datetime.datetime.fromtimestamp(start)
        end_date = datetime.datetime.fromtimestamp(end)
        st.warning(title)
        col1, col2 = st.columns(2)
        col1.time_input("From", start_date, disabled=True, key="From" + str(count))
        col2.time_input("To", end_date, disabled=True, key="To" + str(count))
        count += 1
