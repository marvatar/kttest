import streamlit as st
import streamlit.components.v1 as components

from pathlib import Path
import pandas as pd
import numpy as np

import plotly.express as px

#------------------------------------------------
st.set_page_config(
    page_title="Markus' Demo",
    page_icon=":shark:" #"chart_with_upwards_trend",
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
    return xfig

# ---------------------------------------------------------
# ---------------------------------------------------------

st.title("Markus' DEMO")

# ---------------------------------------------------------

#data_load_state = st.text('Loading data...')
df = get_data()
#data_load_state.text("Done! (using st.cache)")

# ---------------------------------------------------------
with st.sidebar:
    option_x = st.selectbox(
        "Merkmalsauswahl",
        ("sex", "age", "state")
    )
    st.write(f"Auswahl: {option_x}")


#
    components.html("""<hr style="height:2px;border:none;color:#cbcbcb;background-color:#cbcbcb;" /> """)

    values = st.slider(
        label='Altersgrenzen auswählen',
        min_value=14, 
        max_value=99, 
        value=(25, 75),
        step=1,
        )

    st.write(f"Alter von {values[0]} bis {values[1]}")

# ---------------------------------------------------------

tab1, tab2, tab3 = st.tabs(["KPI 1", "KPI 2", "KPI 3"])

# ---------------------------------------------------------

with tab1:

    fig = make_hist_fig(df, option_x)
    st.plotly_chart(fig)

# ---------------------------------------------------------

    if st.checkbox('Daten anzeigen'):
        st.subheader('Rohdaten')
        st.write(df)


with tab2:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)


with tab3:
    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)
