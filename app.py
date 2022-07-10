import streamlit as st
import pandas as pd
import numpy as np

import numpyscript
import pandasscript
import streamlitscript
import gitscript

st.set_page_config(
     page_title='Open cheat sheets',
     layout="wide",
     initial_sidebar_state="expanded",
)
def main():
    st.title("Welcome to Open CheatSheets")
    option = st.sidebar.radio("Select one of the Options:",('NumPy','Pandas','Streamlit','Git'))
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
            numpyscript.main()
        elif(option=='Pandas'):
            pandasscript.main()
        elif(option=='Streamlit'):
            streamlitscript.main()
        elif(option=='Git'):
            gitscript.main()

if __name__=='__main__':
    main()