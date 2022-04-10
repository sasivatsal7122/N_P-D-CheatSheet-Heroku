import streamlit as st
import pandas as pd
import numpy as np

# Initial page config

st.set_page_config(
     page_title='Numpy cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

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
    # Import/Export

    col1, col2, col3 = st.columns(3)

    col1.subheader('Importing/Exploring')
    col1.code('''
     np.loadtxt('file.txt')
     #From a text file
     np.genfromtxt('fille.csv',delimiter=',') 
     # from a CSV file
     np.savetxt('file.txt',arr,delimiter=' ') 
     # Writes to a text
     np.savetxt('file.csv',arr,delimiter=',') 
     # Write to CSV file
    ''')
    #Creating arrays
    col1.subheader('Creating Array')
    col1.code('''
     np.array([1,2,3])
     # One dimention Array
     np.array([(1,2,3),(4,5,6)])
     # Two Dimentttion Array
     np.zeros(3)
     # 1D array with lenght 3.All values 0
     np.ones((3,4))
     # 3x4 array with all values 1.
     np.eye(5)
     # 5x5 array of 0 with 1 on diagonal(identity matrix)
     np.linespace(0,100,6)
     # Arrray of 6 evenly divided values from 0 to 100
     ''')







def main():
    # cs_sidebar()
    cs_body()

    st.header("XYZZ")

    return None