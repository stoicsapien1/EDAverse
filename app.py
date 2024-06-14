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
    st.write("""You can use the EDAverse to quickly generate a comprehensive data profiling and EDA report
     without even writing a single line code.📊📊
    """)
st.title("EDAverse📊💹")
st.write("Explore. Discover. Analyze.")
img="https://i.postimg.cc/sXJ8Rcrp/SQC-AND-OR-UNIT-1.png"
st.image(img,use_column_width=True)
upload_file=st.file_uploader("Upload Your CSV File:",type=["csv"])
if upload_file is not None:
    df=pd.read_csv(upload_file)
    option1=st.sidebar.radio("What do want to include in the report?",["All variable","A subset of Variable"])
    if option1=="All variable":
        df=df
    elif option1=="A subset of Variable":
        var_list=list(df.columns)
        option3=st.sidebar.multiselect("Select the variables(s) you want to include in the report",var_list)
        df=df[option3]
    option2=st.sidebar.selectbox("Chose Minimal Mode or Complete Mode",("Minimal Mode","Complete Mode"))
    if option2=="Complete Mode":
        mode="complete"
        st.sidebar.warning("Complete Mode takes time,PLEASE BE PATIENT!")
    elif option2=="Minimal Mode":
        mode="minimal"
    grid_response=AgGrid(df,editable=True,height=300,width="100%")
    updated=grid_response["data"]
    df1=pd.DataFrame(updated)

    #Now let's build the report
    if st.button("Generate Button"):
        if mode=="complete":
            profile=ProfileReport(df,progress_bar=True)
            st.write("⬇️Report is given below⬇️")
            st_profile_report(profile)
            profile.to_file("your_report.html")
            
        elif mode=="minimal":
            profile=ProfileReport(df1,minimal=True,progress_bar=True)
            st.write("⬇️Report is given below⬇️")
            st_profile_report(profile)
        if "profile" in locals():
            st.download_button("Download Report", data=profile.to_html(), file_name="your_report.html")