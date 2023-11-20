import streamlit as st
import pandas as pd

stats_df = pd.read_csv("Average_Daily_Traffic_Counts.csv")
st.dataframe(stats_df)