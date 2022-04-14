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
         [4,7,10],
         [5,8,11],
         [6,9,12]],
        index=[1,2,3],
        columns=['a','b','c'])
    col1, col2, col3 = st.columns(3)
    col11,col12=st.columns(2)
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
    col1.col11.st.dataframe(df)
    col1.col12.st.dataframe(df1)
    








def main():
    st.title("Pandas Cheat sheet : ")
    st.header('')
    cs_body()