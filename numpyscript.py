import streamlit as st
import pandas as pd
import numpy as np


## Main body

def cs_body():
    # Import/Export

    col1, col2, col3 = st.columns(3)
    st.text('')
    col1.subheader('Importing/Exploring')
    col1.code('''
>>> np.loadtxt('file.txt')
#From a text file
>>> np.genfromtxt('fille.csv',delimiter=',') 
# from a CSV file
>>> np.savetxt('file.txt',arr,delimiter=' ') 
# Writes to a text
>>> np.savetxt('file.csv',arr,delimiter=',') 
# Write to CSV file
    ''')
    #Creating arrays
    st.text('')
    col1.subheader('Creating Array')
    col1.code('''
>>> np.array([1,2,3])
# One dimention Array
>>> np.array([(1,2,3),(4,5,6)])
# Two Dimentttion Array
>>> np.zeros(3)
# 1D array with lenght 3.All values 0
>>> np.ones((3,4))
# 3x4 array with all values 1.
>>> np.eye(5)
# 5x5 array of 0 with 1 on diagonal(identity matrix)
>>> np.linespace(0,100,6)
# Arrray of 6 evenly divided values from 0 to 100
>>> np.arrange(0,10,3)
# Array of values from 0 to less than 10 with step 3
#Eg:- [0,3,6,9]
>>> np.full((2,3),8)
# 2x3 array  with all values 8
>>> np.random.rand(4,5)
# 4x5 Array of random floats between 0-1
>>> np.random.rand(6,7)*100
# 6x7 Array of random floats between 0-100
>>> np.random.randint(5,size=(2,3))
# 2x3 array with random ints between 0-4
     ''')
    st.text('')
    col1.subheader('Inspecting Properties')
    col1.code('''
>>> arr.size
# Returns number of elements in arr
>>> arr.shape
# Returns dimensions of arr(Rows,Columns)
>>> arr.dtype 
# Returns type f elements in  the arr
>>> arr.astype(dtype)
# Convert arr element to type dtype
>>> arr.tolist()
# Convert arr to a python list
>>> np.info(np.eye)
# View documentation for np.eye
     ''')
    st.text('')
    col1.subheader('Copying/Sorting/Reshaping')
    col1.code('''
>>> np.copy(arr)
# Copies arr to new memory
>>> arr.view(dtype)
# Creates view of arr elements with type dtype
>>> arr.sort()
# Sort arr
>>> arr.sort(axis=0)
# Sorts specific axis of arr
    ''')
    st.text('')
    col2.subheader('Copying/Sorting/Reshaping-II')
    col2.subheader(' ')
    col2.code('''
>>> two_d_arr.flatten()
# Flatten 2D array two_d_arr to 1D
>>> arr.T
# Transposes arr(Rows become Columns and Vise Versa)
>>> arr.reshape(3,4)
# Reshapes arr to 3 roe=ws and 4 columns without changing the data
>>> arr.resize((5,6))
#Changes arr shape to 5x6 and fills new values with 0
    ''')

    # Adding/Removing Elements
    st.text('')
    col2.subheader('Adding/Removing Elements')
    col2.code('''
>>> np.append(arr,values)
# Appends values to end of arr
>>> np.insert(arr,2,value)
# Insert values into arr before index 2
>>> np.delete(arr,3,axis=0)
# Delete row on index 3 of arr
>>> np.delete(arr,4,axis=1)
# Delete column on index 4 of the arr
     ''')

    # Combining/Splitting
    st.text('')
    col2.subheader('Combining/Splitting')
    col2.code('''
>>> np.concatenate((arr1,arr2),axis=0)
# Adds arr2 as rows to the end of arr1
>>> np.concatenate((arr1,arr2),axis=1)
# Adds arr2 as columns to the end of arr1
>>> np.split(arr,3)
# Split arr into 3 sub-arrays
>>> np.hsplit(arr,5)
# Split arr horizontally on the 5th index
    ''')

    # Indexing/Slising/Subsetting
    st.text('')
    col2.subheader('Indexing/Slising/Subsetting')
    col2.code('''
>>> arr[5]
# Returns the element at index 5
>>> arr[2,5]
# Return the 2D array element on the index [2][5]
>>> arr[1]=4
# Assign array element on index 1 to the value 4
>>> arr[1,3]=10
# Assign array element on index [1][3] to the value 10
>>> arr[0:3]
# Returns the element at the indicces 0,1,2(On the 2D array: returns 0,1,2)
>>> arr[0:3,4]
# returns the elements on the rows 0,1,2 at column 4
>>> arr[:2]
# Returns the elements at the indices 0,1(On a 2D array:returns rows 0,1)
>>> arr[:,1]
# Returns the elements at the index 1 on all rows
>>> arr<5
# Returns an array of boolean values
>>> (arr1<3)&(arr2<5)
# Returns an array of boolean values
>>> ~arr
# Inverts a boolean array
>>> arr[arr<5]
# Returns array elements smaller than 5
    ''')

    # Scalar Math
    st.text('')
    col3.subheader(' ')
    col3.subheader('Scalar Math')
    col3.subheader(' ')
    col3.code('''
>>> np.add(arr,1)
# Add 1 to each array element
>>> np.subtract(arr,2)
# Substract 2 from each array element
>>> np.multiply(arr,3)
# Multiply each array element by 3
>>> np.divide(arr,4)
# Divide each array element by 4
>>> np.power(arr,5)
# Raise each array element to the 5th power
    ''')

    # Vector Math
    st.text('')
    col3.subheader('Vector Math')
    col3.subheader(' ')
    col3.code('''
>>> np.add(arr1,arr2)
# Elementwise add arr2 to arr1
>>> np.subtract(arr1,arr2)
# Elementwise substract arr2 fromm arr1
>>> np.multiply(arr1,arr2)
# Elementwise multiply arr1 by arr2
>>> np.divide(arr1,arr2)
# Elementwise divide arr1 by arr2
>>> np.power(arr1,arr2)
# Elementwise Raise arr1 raised to the power of arr2
>>> np.array_equal(arr1,arr2)
# Returns TRUE if the arrays have the same elements and shape
>>> np.sqrt(arr)
# Squareroot of each element on the array
>>> np.sin(arr)
# Sine of each element in the array
>>> np.log(arr)
# Natural log of each element in the array
>>> np.abs(arr)
# Absolute values of each element in the array
>>> np.ceil(arr)
# Round up to the nearest int
>>> np.floor(arr)
# Round down to the nearest int
>>> np.round(arr)
# Round to the nearest int
    ''')
    # Statistics
    st.text('')
    col3.subheader('Statistics')
    col3.code('''
>>> np.mean(arr,axis=0)
# Returns mean along spesific axis
>>> arr.sum()
# Reaturns sum of the arr
>>> arr.min()
# Returns minimum value of arr
>>> arr.max(axis=0)
# Returns maximum value of spesific axis
>>> np.std(arr,axis=1)
# Returns the Standerd deviation of spesific axis
>>> arr.corrcoef()
# Returns correlation coefficient of arrar
    ''')
    

def main():
    st.title("Numpy Cheat sheet : ")
    st.header('')
    cs_body()
