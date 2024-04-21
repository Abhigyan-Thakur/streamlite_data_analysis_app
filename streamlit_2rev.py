#imports
import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st

#headers and subheaders
st.header('Data Analysis')
st.subheader('data analysis tools pvt')

#Upload Data Set
upload=st.file_uploader("Upload your DataSet (In csv Format)")
if upload is not None:
    data=pd.read_csv(upload)
    
    
#Show DataSet    
if upload is not None:
    if st.checkbox('Preview DataSet'):
        if st.button('Head'):
            st.write(data.head())
        if st.button('Tail'):
            st.write(data.tail())
            
            
#Check DataType of each column            
if upload is not None:
    if st.checkbox('DataTypes'):
        st.write(data.dtypes)

#Find the shape of the Data Set
if upload is not None:
    data_shape=st.radio('What dimension Do u want to Check?',('Rows','Columns'))
    if data_shape=='Rows':
        st.text('Number of Rows: ')
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text('Number of columns: ')
        st.write(data.shape[1])
    
#Find Null values in the Dataset            
if upload is not None:
    if st.checkbox('Null values:'):
        test=data.isnull().values.any()
        if test==True:
                sns.heatmap(data.isnull())
                st.pyplot()
        else:
            st.success('Congrats your Dataset has no errors')
            
#Find Duplicate values in the dataset 
if upload is not None:           
    if st.checkbox('Duplicated check'):
        tst=data.duplicated().any()
        if tst==True:
            st.warning('Dataset contains Duplicates')
            dup=st.selectbox("Do u want to drop the Duplicated data",('Select One','Yes','No'))
            if(dup=='Yes'):
                data=data.drop_duplicates()
                st.success('wow! ur duplicates are droped')
            if(dup=='No'):
                st.warning('Data is the Same')
#Get overall Statistics                
if upload is not None:               
    if st.checkbox("Summary of the DataSet"):
        st.write(data.describe(include="all"))
        
#About app
if st.button('About App!'):
    st.text('Built with strimlit')
    st.text("Thanks")
    
#by    
st.text('By Abhigyan Thakur')    