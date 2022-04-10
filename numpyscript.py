import streamlit as st
import pandas as pd
import numpy as np

# Initial page config

st.set_page_config(
     page_title='Numpy cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)


def main():
    # cs_sidebar()
    cs_body()

    st.header("XYZZ")

    return None

    # Thanks to streamlitopedia for the following code snippet

# def img_to_bytes(img_path):
#     img_bytes = Path(img_path).read_bytes()
#     encoded = base64.b64encode(img_bytes).decode()
#     return encoded


#     # sidebar

# def cs_sidebar():

#     st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
#     st.sidebar.header('Numpy cheat sheet')



#     return None
## Main body

def cs_body():
    # Magic commands

    col1, col2, col3 = st.columns(3)

    col1.subheader('Importing/Exploring')
    col1.code('''For a text file
     np.loadtxt("file.txt") #From a text file
     np.genfromtxt('fille.csv',delimiter=',') # from a CSV file
     np.savetxt('file.txt',arr,delimiter=' ') # Writes to a text
     np.
     ''')
