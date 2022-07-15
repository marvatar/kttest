import streamlit as st

from pathlib import Path
import pandas as pd
import numpy as np

#------------------------------------------------
st.set_page_config(
    page_title="Kantar Demo",
    page_icon="chart_with_upwards_trend",
#    layout="wide",
)
#------------------------------------------------
@st.cache
def get_data():
    tmpDAT = pd.read_excel(Path.cwd() / "tobeweighted.xlsx")
    
    return tmpDAT

st.title("KANTAR DEMO")

data_load_state = st.text('Loading data...')
df = get_data()
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Daten anzeigen'):
    st.subheader('Rohdaten')
    st.write(df)

