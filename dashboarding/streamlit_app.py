import streamlit as st
import os
import subprocess
import pandas as pd
import numpy as np
import itertools
import seaborn as sns
import matplotlib.pyplot as plt

import geopandas as gpd
import rasterio
import plotly

st.set_page_config(layout="wide")

with st.sidebar:
    st.write("Does this sidebar work?")
    st.write("How do I add pages here now?")
    st.title("Guessing title is just a way to format")

st.title('Test====================================')
st.title('Hello, World!')
st.write('This is a simple Streamlit app.')
st.write('This is a simple Streamlit app. (2)')

# print("what??")

arr = np.arange(1, 50, 2)
arr = itertools.repeat(arr, 5)
df = pd.DataFrame(arr)
df.columns = [f"column_{str(c)}" for c in df.columns]

# print(df.shape)
# print(df.head())

col1, col2 = st.columns(2)

with col1:
    st.title("Left title")
    st.write("Left text")
    st.dataframe(df)

with col2:
    st.title("Right title")
    st.write("Right text")
    fig = plt.figure()
    plt.hist(df)
    st.pyplot(fig)

# with st.

# pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])
# pg.run()