import streamlit as st
import pandas as pd
import numpy as np

import numpyscript
import pandasscript
import streamlitscript

st.set_page_config(
     page_title='Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)
def main():
    st.title("Welcome to NumPy Pandas and Streamlit CheatSheet")
    option = st.sidebar.radio("Select one of the Options:",('NumPy','Pandas','Streamlit'))
    st.text("")
    st.text("")
    st.sidebar.text(" Basic Install Commands")
    st.sidebar.code("""
>>> pip install pandas
>>> pip install numpy
>>> pip install streamlit
                    """)
    st.sidebar.text("Import Convention")
    st.sidebar.code("""
>>> import pandas as pd
>>> import numpy as np
>>> import streamlit as st
                    """)
    if option:
        if option == 'NumPy':
            pass
            numpyscript.main()
        elif(option=='Pandas'):
            pass
            pandasscript.main()
        else:
            pass
            streamlitscript.main()           
if __name__=='__main__':
    main()