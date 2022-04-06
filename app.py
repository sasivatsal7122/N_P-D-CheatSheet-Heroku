import streamlit as st
import pandas as pd
import numpy as np

import numpyscript
import pandasscript


def main():
    st.title("Welcome to NumPy And Pandas CheatSheet")
    option = st.sidebar.radio("Select one of the Options:",('NumPy','Panads'))
    st.text("")
    st.text("")
    st.sidebar.text(" Basic Install Commands")
    st.sidebar.code("""
>>> pip install pandas
>>> pip install numpy
                    """)
    st.sidebar.text("Import Convention")
    st.sidebar.code("""
>>> import pandas as pd
>>> import numpy as np
                    """)
    if option:
        if option == 'NumPy':
            pass
            numpyscript.main()
        else:
            pass
            pandasscript.main()
            
if __name__=='__main__':
    main()