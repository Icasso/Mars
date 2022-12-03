import streamlit as st

import client.OKXClient as Client
import config.Config as Config
import service.StatusService as StatusService

Config.load_config()

st.title("Project - Mars")
st.info("Check the status of OKX upgrades, system maintenance, potential service outages, and crypto deposits and "
        "withdrawals")

StatusService.status(Client.get_status())
