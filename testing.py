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
  'AgvNumber': 'UInt8',
  'AgvType': 'UInt8',
  'SequenceNumber': 'UInt32',
  'CurrentNodeNumber': 'UInt16',
  'NextNodeNumber': 'UInt16',
  'TaskTable': 'UInt16',
  'TableCommand': 'UInt16',
  'RunStateStatus': 'category',
  'DistanceValue': 'Int16',
  'BatteryCharge': 'UInt8',
  'Mode': 'category',
  'ErrorCode': 'UInt16',
  'ErrorDescription': 'category',
  'AgvZone': 'UInt8',
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
