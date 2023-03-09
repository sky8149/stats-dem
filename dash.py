import streamlit as st  
import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt
import numpy as np


st.title("Iris Dashbord")
df = pd.read_csv('iris.csv')
st.dataframe(df)

col1, col2 = st.columns(2)
with col1:
    
    st.dataframe(df[['sepal_length','sepal_width']])
with col2:
    st.header('Sepal lenth and sepal width')
    fig, ax = plt.subplots()
    ax.scatter(df.iloc[:,0],df.iloc[:,1])
    st.pyplot(fig)
st.write("*****************************************************************")
col1, col2 = st.columns(2)
with col1:
    
    st.dataframe(df[['petal_length','petal_width']])
with col2:
    st.header('Petal lenth and Petal width')
    fig, ax = plt.subplots()
    ax.scatter(df.iloc[:,2],df.iloc[:,3])
    st.pyplot(fig)


st.write("***********************************************************************")
st.header('Line plot ')
st.line_chart(df.iloc[:,:-1])

st.write("***********************************************************************")
st.header('Box Plot')
col1,col2,col3,col4 =st.columns(4)
with col1:
    fig, ax = plt.subplots()
    ax.boxplot(df.iloc[:,0])
    st.pyplot(fig)
with col2:
        fig, ax = plt.subplots()
        ax.boxplot(df.iloc[:,1])
        st.pyplot(fig)
with col3:
    fig, ax = plt.subplots()
    ax.boxplot(df.iloc[:,2])
    st.pyplot(fig)
with col4:
    fig, ax = plt.subplots()
    ax.boxplot(df.iloc[:,3])
    st.pyplot(fig)

st.bar_chart(df[['sepal_length','sepal_width','petal_length','petal_width']])