import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
from st_aggrid import AgGrid
import ydata_profiling
from ydata_profiling import ProfileReport
from PIL import Image

st.set_page_config(layout="wide")
st.sidebar.title("Welcome to EDAverse")
with st.sidebar.expander("About the App💻"):
    st.write("""EDAverse is made using Streamlit and pandas_profiling package.You can use the app to quickly generate a comprehensive data profiling and EDA report
     without even writing a single line code.📊📊
    """)
st.title("EDAverse📊💹")
st.write("Explore. Discover. Analyze.")
