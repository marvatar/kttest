import streamlit as st

from pathlib import Path
import pandas as pd
import numpy as np

import plotly.express as px

#------------------------------------------------
st.set_page_config(
    page_title="Markus' Demo",
    page_icon="chart_with_upwards_trend",
#    layout="wide",
)
#------------------------------------------------
@st.cache
def get_data():
    tmpDAT = pd.read_excel("tobeweighted.xlsx")  
    return tmpDAT

def make_hist_fig(tmp_df, tmp_var):
    xfig = px.histogram(tmp_df,
                        title='Histogram of ' + tmp_var,
                        x=tmp_var,
                        text_auto=True,
    )
    xfig.update_layout(bargap=0.2)
    st.balloons() 
    return xfig

st.title("Markus' DEMO")

data_load_state = st.text('Loading data...')
df = get_data()
data_load_state.text("Done! (using st.cache)")

with st.sidebar:
    option_x = st.selectbox(
        "Merkmalsauswahl",
        ("sex", "age", "state")
    )
    st.write("Auswahl: " + option_x)

fig = make_hist_fig(df, option_x)
st.plotly_chart(fig)

if st.checkbox('Daten anzeigen'):
    st.subheader('Rohdaten')
    st.write(df)


