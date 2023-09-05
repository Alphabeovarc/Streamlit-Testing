import streamlit as st
import pandas as pd
import numpy as np
import plotly as pt

df = pd.DataFrame()

st.write('testing app')
st.write('syncing')
st.file_uploader('upload', 'csv', True, 'uploaded_files')

#st.write(st.session_state.uploaded_files)

dtypes = {
  'MessageCode': 'category',
  'MessageSeverity': 'category',
  'AgvNumber': 'uint8',
  'AgvType': 'uint8',
  'SequenceNumber': 'uint32',
  'CurrentNodeNumber': 'uint16',
  'NextNodeNumber': 'uint16',
  'TaskTable': 'uint16',
  'TableCommand': 'uint16',
  'RunStateStatus': 'category',
  'DistanceValue': 'int16',
  'BatteryCharge': 'uint8',
  'Mode': 'category',
  'ErrorCode': 'uint16',
  'ErrorDescription': 'category',
  'AgvZone': 'uint8',
  'CurrentJobID': 'category',
  'CurrentPlantID': 'category',
}

df = pd.DataFrame()
for file in st.session_state.uploaded_files:
  _ = pd.read_csv(
    file,
    on_bad_lines = 'skip',
    dtype = dtypes,
  )
  df = pd.concat([df,_], ignore_index = True)

st.dataframe(df)
st.write(f'{df.memory_usage(deep=True).sum()/1000/1000} MB')
