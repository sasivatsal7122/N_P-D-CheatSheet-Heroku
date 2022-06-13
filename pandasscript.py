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
    df1=pd.DataFrame({
        "a" : [4,5,6],
        "b": [7,8,9],
        "c": [10,11,12]},
        index=pd.MultiIndex.from_tuples(
            [('d',1),('d',2),('e',2)],names=['n','v']
            ))
    col1, col2, col3 = st.columns(3)
    st.text('')
    col1.subheader('Creating DataFrames')
    col1.code('''
# Spesify values for each column
>>> df1=pd.DataFrame({
        "a" : [4,5,6],
        "b": [7,8,9],
        "c": [10,11,12]},
        index=pd.MultiIndex.from_tuples(
            [('d',1),('d',2),('e',2)],names=['n','v']
            ))


    ''')

    col1.code('''
# Spesify values for each column
>>> df=pd.DataFrame({
"a" : [4,5,6],
"b": [7,8,9],
"c": [10,11,12]},
index=[1,2,3])

# Specify values for each row
>>> df1=pd.DataFrame([
    [4,7,10],
    [5,8,11],
    [6,9,12]],
index=[1,2,3],
columns=['a','b','c'])


    ''')
    col1.text('Output : ')
    
    
    col1.dataframe(df)
    col1.dataframe(df1)

    col1.subheader('Method Chaining')
    df = (pd.melt(df)
        .rename(columns={
        'variable':'var',
        'value':'val'})
        .query('val >= 200')
        )

    col1.code('''
 #Most pandas methods return a DataFrame so that
 #another pandas method can be applied to the result.
 #This improves readability of code.
 >>> df = (pd.melt(df)
 .rename(columns={
 'variable':'var',
 'value':'val'})
 .query('val >= 200')
 )
    ''')
    col1.text('Output : ')    
    col1.dataframe(df)
    
    col1.subheader('Using Query')
    col1.code('''
 #query() allows Boolean 
 #expressions for filtering rows.
 >>> df.query('Length > 7')
 >>> df.query('Length > 7 and Width < 8')
 >>> df.query('Name.str.startswith("abc")',engine="python")
    ''')

    col1.subheader('Subset Variables')
    col1.text('-Columns')
    col1.code('''
 >>> df[['width', 'length', 'species']]
 #Select multiple columns with specific names.
 >>> df['width'] or df.width
 #Select single column with specific name.
 >>> df.filter(regex='regex')
 #Select columns whose name matches regular expression regex.
    ''')

    col1.subheader('Windows')
    col1.code('''
>>> df.expanding()
#Return an Expanding object allowing summary functions to be
#applied cumulatively.
>>> df.rolling(n)
#Return a Rolling object allowing summary functions to be
#applied to windows of length n.
    ''')

    col2.subheader('Reshaping Data')
    col2.text('- Change layout, sorting, reindexing, renaming')
    df=pd.DataFrame({
        "a" : [4,5,6],
        "b": [7,8,9],
        "c": [10,11,12]},
        index=[1,2,3])
    
    

    col2.code('''
 >>> pd.melt(df)
 #Gather columns into rows.
 >>> df.pivot(columns='var', values='val')
 # Spread rows into columns.
 >>> pd.concat([df1,df2])
 #Append rows of DataFrames
 >>> pd.concat([df1,df2], axis=1)
 #Append columns of DataFrames
 >>> df.sort_values('mpg')
 #Order rows by values of a column (low to high).
 >>> df.sort_values('mpg', ascending=False)
 #Order rows by values of a column (high to low).
 >>> df.rename(columns = {'y':'year'})
 #Rename the columns of a DataFrame
 >>> df.sort_index()
 #Sort the index of a DataFrame
 >>> df.reset_index()
 #Reset index of DataFrame to row numbers, moving
 #index to columns.
 >>> df.drop(columns=['Length', 'Height'])
 #Drop columns from DataFrame
    ''')
    
    col2.subheader('Subset Observations')
    col2.text('-Rows')
    col2.code('''
 >>> df[df.Length > 7]
 #Extract rows that meet logical criteria.
 >>> df.drop_duplicates()
 #Remove duplicate rows (only considers columns).
 >>> df.sample(frac=0.5)
 #Randomly select fraction of rows.
 >>> df.sample(n=10)
 #Randomly select n rows.
 >>> df.nlargest(n, 'value')
 #Select and order top n entries.
 >>> df.nsmallest(n, 'value')
 #Select and order bottom n entries.
 >>> df.head(n)
 #Select first n rows.
 >>> df.tail(n)
 #Select last n rows.
    ''')

    col2.subheader('Subsets')
    col2.text('- Rows and Columns')
    col2.code('''
 #Use df.loc[] and df.iloc[] to select only 
 #rows, only columns or both.

 #Use df.at[] and df.iat[] to access a single
 #value by row and column.
 #First index selects rows, second index columns.
 >>> df.iloc[10:20]
 #Select rows 10-20.
 >>> df.iloc[:, [1, 2, 5]]
 #Select columns in positions 1, 2 and 5 (first column is 0).
 >>> df.loc[:, 'x2':'x4']
 #Select all columns between x2 and x4 (inclusive).
 >>> df.loc[df['a'] > 10, ['a', 'c']]
 #Select rows meeting logical condition, and only the specific columns.
 >>> df.iat[1,2] #Access single value by index
 >>> df.at[4, 'A'] #Access single value by label
    ''')

    col2.subheader('Handling Missing Data')
    col2.code('''
 >>> df.dropna()
 #Drop rows with any column having NA/null data.
 >>> df.fillna(value)
 #Replace all NA/null data with value.
    ''')
    col2.subheader('Plotting')
    col2.code('''
 >>> df.plot.hist()
 #Histogram for each column
 >>> df.plot.scatter(x='w',y='h')
 #Scatter chart using pairs of points.
    ''')
    
    col3.subheader('Summarize Data')
    col3.code('''
 >>> df['w'].value_counts()
 #Count number of rows with each unique value of variable
 >>> len(df)
 #Number of rows in DataFrame.
 >>> df.shape
 #Tuple of no.of rows, no.of columns in DataFrame.
 >>> df['w'].nunique()
 #No.of distinct values in a column.
 >>> df.describe()
 #Basic descriptive and statistics for each column (or GroupBy).
    ''')
    col3.subheader('Summary Functions')
    col3.code('''
#Pandas provides a large set of summary functions that operate on
#different kinds of pandas objects (DataFrame columns, Series,
#GroupBy, Expanding and Rolling (see below)) and produce single
#values for each of the groups. When applied to a DataFrame, the
#result is returned as a pandas Series for each column.
sum() - #Sum values of each object. 
min() - #Minimum value in each object.
max() - #Maximum value in each object.
count() - #Count non-NA/null values of each object.
mean() - #Mean value of each object.
median() - #Median value of each object.
var() - #Variance of each object.
quantile([0.25,0.75]) - #Quantiles of each object.
std() - #Standard deviation of each object.
apply(function) - #Apply function to each object.
    ''')    
    col3.subheader('Make New Columns')
    col3.code('''
>>> df.assign(Area=lambda df: df.Length*df.Height)
#Compute and append one or more new columns.
>>> df['Volume'] = df.Length*df.Height*df.Depth
#Add single column.
>>> pd.qcut(df.col, n, labels=False)
#Bin column into n buckets.

#Pandas provides a large set of vector functions that operate on all
#columns of a DataFrame or a single selected column (a pandas
#Series). These functions produce vectors of values for each of the
#columns, or a single Series for the individual Series. Examples:
max(axis=1)
#Element-wise max.
min(axis=1)
#Element-wise min.
clip(lower=-10,upper=10)
#Trim values at input thresholds
abs()
    #Absolute value.
    ''')

    col3.subheader('Group Data')
    col3.code('''
>>> df.groupby(by="col")
#Return a GroupBy object, grouped
#by values in column named "col".
>>> df.groupby(level="ind")
#Return a GroupBy object, grouped
#by values in index level named
#"ind".

#The examples below can also be applied to groups. In this case, the
#function is applied on a per-group basis, and the returned vectors
#are of the length of the original DataFrame.
shift(1)
#Copy with values shifted by 1.
shift(-1)
#Copy with values lagged by 1.
rank(method='dense')
#Ranks with no gaps.
rank(method='min')
#Ranks. Ties get min rank.
rank(pct=True)
#Ranks rescaled to interval [0, 1].
rank(method='first')
#Ranks. Ties go to first value.
cumsum()
#Cumulative sum.
cummax()
#Cumulative max.
cummin()
#Cumulative min.
cumprod()
#Cumulative product.
    ''')






def main():
    st.title("Pandas Cheat sheet : ")
    st.header('')
    cs_body()