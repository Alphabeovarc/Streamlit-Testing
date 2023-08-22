import streamlit as st
import pandas as pd
import numpy as np
import plotly as pt

st.write('testing app')
st.file_uploader('upload', 'csv', True, 'uploaded_files')

st.write(st.session_state.uploaded_files
