import streamlit as st

import client.OKXClient as OKXClient
import client.BinanceClient as BinanceClient
import client.KrakenClient as KrakenClient
import client.KucoinClient as KucoinClient
import config.Config as Config
import service.StatusService as StatusService

Config.load_config()

st.title("Live Crypto Exchange Status")
st.info(
    "Check the status of Crypto Exchanges upgrades, system maintenance, potential service outages, and crypto deposits "
    "and withdrawals")

exchange = st.selectbox("Select Crypto Exchange",
                        ("OKX", "Kucoin", "Kraken", "Binance - International"))

match exchange:
    case "OKX":
        StatusService.okx_status(OKXClient.get_status())
    case "Kucoin":
        StatusService.kucoin_status(KucoinClient.get_status())
    case "Kraken":
        StatusService.kraken_status(KrakenClient.get_status())
    case "Binance - International":
        StatusService.binance_status(BinanceClient.get_status("INTERNATIONAL"))
    case _:
        st.empty()
