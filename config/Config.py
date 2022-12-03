import streamlit as st


def load_config():
    st.set_page_config(
        page_title="Project - Mars",
        page_icon="🌌",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    hide_menu_style = """
            <style>
            header {visibility: hidden;}
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
