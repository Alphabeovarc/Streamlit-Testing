import streamlit as st
import pandas as pd
import numpy as np
import plotly as pt

df = pd.DataFrame()

st.write('testing app')
st.file_uploader('upload', 'csv', False, 'uploaded_files')

st.write(st.session_state.uploaded_files)


df = pd.read_csv(st.session_state.uploaded_files)
st.dataframe(df)
  
