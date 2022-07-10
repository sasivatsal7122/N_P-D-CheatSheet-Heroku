import streamlit as st

# Write your imports here if required


## Main body
# donot CHNAGE the function name

def cs_body():

    st.title(" Write your cheat sheet title here ")
    st.markdown("<p><TT>Designed and Developed by <a style='text-decoration:none;color:red' target='_blank' href='Place Your Github Link'>WRITE YOUR NAME HERE></TT></p>", unsafe_allow_html=True)
    
# create as many as columns you would like to have , but make sure to make it look clean and good

    col1, col2, col3 = st.columns(3)
    st.text('')
    col1.subheader('SAMPLE HEADER-1')
    col1.code('''
>>> YOUR CONTENT GOES HERE
# MAKE SURE TO WRITE A LOT OF COMMENTS

    ''')
    #Creating arrays
    st.text('')
    col1.subheader('SAMPLE HEADER-2')
    col1.code('''
>>> YOUR CONTENT GOES HERE
# MAKE SURE TO WRITE A LOT OF COMMENTS

     ''')
    st.text('')
    col1.subheader('SAMPLE HEADER-3')
    col1.code('''
>>> YOUR CONTENT GOES HERE
# MAKE SURE TO WRITE A LOT OF COMMENTS

     ''')
    st.text('')
    col1.subheader('SAMPLE HEADER-4')
    col1.code('''
>>> YOUR CONTENT GOES HERE
# MAKE SURE TO WRITE A LOT OF COMMENTS

    ''')
    st.text('')
    col2.subheader('SAMPLE HEADER-4')
    col2.subheader(' ')
    col2.code('''
>>> YOUR CONTENT GOES HERE
# MAKE SURE TO WRITE A LOT OF COMMENTS

    ''')

    # Adding/Removing Elements
    st.text('')
    col2.subheader('SAMPLE HEADER-5')
    col2.code('''
>>> YOUR CONTENT GOES HERE
# MAKE SURE TO WRITE A LOT OF COMMENTS

     ''')

    # Combining/Splitting
    st.text('')
    col2.subheader('SAMPLE HEADER-6')
    col2.code('''
>>> YOUR CONTENT GOES HERE
# MAKE SURE TO WRITE A LOT OF COMMENTS

    ''')

    # Indexing/Slising/Subsetting
    st.text('')
    col2.subheader('SAMPLE HEADER-7')
    col2.code('''
>>> YOUR CONTENT GOES HERE
# MAKE SURE TO WRITE A LOT OF COMMENTS

    ''')

    # Scalar Math
    st.text('')
    col3.subheader(' ')
    col3.subheader('SAMPLE HEADER-7')
    col3.subheader(' ')
    col3.code('''
>>> YOUR CONTENT GOES HERE
# MAKE SURE TO WRITE A LOT OF COMMENTS

    ''')

    # Vector Math
    st.text('')
    col3.subheader('SAMPLE HEADER-8')
    col3.subheader(' ')
    col3.code('''
>>> YOUR CONTENT GOES HERE
# MAKE SURE TO WRITE A LOT OF COMMENTS

    ''')
    # Statistics
    st.text('')
    col3.subheader('SAMPLE HEADER-9')
    col3.code('''
>>> YOUR CONTENT GOES HERE
# MAKE SURE TO WRITE A LOT OF COMMENTS

    ''')
    
"""

AFTER COMPLETING YOUR CHEATSHEET TEST IT LOCALLY IF EVERYTHING LOOKS GOOD CREATE A IF-ELSE IN
APP.PY AND ADD YOUR FUNCTION THERE, MAKE SURE TO UPDATE THE RADIO BUTTON OPTIONS AS WELL

CHECK AGAIN IF THERE ARE NO ERRORS PUSH YOUR CODE TO THE REPO


"""

def main():
    st.header('')
    cs_body()
