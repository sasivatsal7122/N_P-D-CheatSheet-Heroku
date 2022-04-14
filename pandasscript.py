import streamlit as st
import pandas as pd
import numpy as np


## Main body

def cs_body():
    # Import/Export
    df=pd.DataFrame({
        "a" : [4,5,6],
        "b": [7,8,9],
        "c": [10,11,12]},
        index=[1,2,3])
    df1=pd.DataFrame([
         [4,5,6],
         [7,8,9],
         [10,11,12]],
        index=[1,2,3],
        columns=['a','b','c'])
    col1, col2, col3 = st.columns(3)
    st.text('')
    col1.subheader('Creating DataFrames')
    col1.code('''
        # Spesify values for each column
        df=pd.DataFrame({
        "a" : [4,5,6],
        "b": [7,8,9],
        "c": [10,11,12]},
        index=[1,2,3])

        # Specify values for each row
        df1=pd.DataFrame([
         [4,7,10],
         [5,8,11],
         [6,9,12]],
        index=[1,2,3],
        columns=['a','b','c'])
        

    ''')
    st.text('Output')
    col1.code(st.write(df),st.write(df1)
    )








def main():
    st.title("Pandas Cheat sheet : ")
    st.header('')
    cs_body()