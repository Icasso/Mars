import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo


def status(current):
    if current is None or len(current) == 0:
        st.success("All services are operational")
        st.balloons()
    else:
        st.header('Live OKX Status')
        count = 0
        for status in current:
            st.write('---')
            title = status['title']
            start = int(status['begin']) / 1000.0
            end = int(status['end']) / 1000.0
            start_date = datetime.fromtimestamp(start, tz=ZoneInfo("Asia/Hong_Kong"))
            end_date = datetime.fromtimestamp(end, tz=ZoneInfo("Asia/Hong_Kong"))
            st.warning(title)
            col1, col2 = st.columns(2)
            col1.time_input("HKT: From", start_date, disabled=True, key="From" + str(count))
            col2.time_input("To", end_date, disabled=True, key="To" + str(count))
            count += 1
