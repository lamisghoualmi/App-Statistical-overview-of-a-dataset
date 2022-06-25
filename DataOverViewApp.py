# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:33:59 2022

@author: Benk
"""
import streamlit as st
import numpy as np
import pandas  as pd



# streamlit run "C:\Users\Benk\Desktop\Kaggle, Maven dataset\MarketingData-Maven\DataOverViewApp.py"

st.header('Statistical description of a dataset')
st.sidebar.image("StatisticOverView.png", use_column_width=True)
st.sidebar.write("""
        Data analysis follows a rigorous step-by-step process in order to make
        informed decisions. It is very important to have a descriptive statistics overview
        of the data before starting the analysis. This app helps you get
        a clear vision of what steps should you take to clean your data. 
        Such as the necessity of removing duplicates, missing values, outliers, 
        etc. If you are interested to check my code, check my github using 
        the following link: [Github](https://github.com/lamisghoualmi/App-Statistics-overview-of-a-dataset).
         """)

# uploaded_file = st.file_uploader("Choose a dataset (csv file)")
uploaded_file=st.file_uploader("Choose a dataset (CSV file)", type=['csv'] , accept_multiple_files=False, key=None, 
                               help=None ,
                               on_change=None, args=None, kwargs=None, disabled=False)
option=st.selectbox('Select an option:',
     ('View of the data','Data size', 'Columns name', 'Data columns types', 'Duplicates',
      'Missing values', 'Percentages of missing values', 'Zeros values per column', 
      'Summarization of the data (Numerical variables)', 
      'Summarization of the data (Categorical variables)' ))
st.write("""
             #### Results:
             """)   
try:
    if uploaded_file is not None:
         df = pd.read_csv(uploaded_file)
              
    
    
                
    if option=='View of the data' and uploaded_file is not None: 
     st.caption('View of the data.')
     st.write(df)
    
    
    if option=='Data size': 
     st.caption('Size of the data.')
     st.write('Size of the data', df.shape)
    
    if option=='Columns name': 
     st.caption('Columns name.')
     st.write( df.columns)
     
    if option=='Data columns types': 
      st.caption('Data columns types.')
      f=df.dtypes
      st.write(f.astype(str) )
      
    if option=='Duplicates': 
     st.caption('Number of duplicates.')
     duplicateObser = df[df.duplicated()]
     LabelsDupObser=duplicateObser.axes[0].tolist()
     st.write( duplicateObser.shape[0])
     
    if option=='Missing values': 
     try:
        st.caption('Missing values. Depending on the number of missing values,',
                   'you can decide which technique you need to get rid of missing values. Example: removing missing values or applying an amputation technique')
        st.write(df.isnull().sum())
     except:
       st.write( 'This dataset does not missing values')
    
    if option=='Percentages of missing values': 
     try:
        st.caption('Percentages of missing valuesDepending on the number of missing values,',
                   'you can decide which technique you need to get rid of missing values. Example: removing missing values or applying an amputation technique')
        for col in df.columns:
            PercentageMissing = np.mean(df[col].isnull())
            # print('{} - {}%'.format(col, round(PercentageMissing *100)))
            st.write('{} : {}%'.format(col, round(PercentageMissing *100)))
     except:
       st.write( 'This dataset does not missing values')
    
    if option=='Zeros values per column':
     try:
        st.caption('Zeros values per column')
        zero_val = (df == 0.00).astype(int).sum(axis=0)
        st.write(zero_val)
     except:
        st.write( 'This dataset does not zero values')
        
    if option=='Summarization of the data (Numerical variables)': 
        try:
         st.caption('Summarization of the data (Numerical variables). You can check for the variables that might have outliers by analyzing the min, mean and max of each variable')
         st.write(df.describe())
        except:
         st.write( 'This dataset does not contain numerical variables')
        
         
    if option=='Summarization of the data (Categorical variables)': 
      try:
        st.caption('Summarization of the data (Categorical variables). This can helps you know if there is a bias in the population and also might help you correct the categories.', 
                   'Example: user who entered SINGLE or ALONE, the information belong to the same category wich is SINGLE')
        cols = df.columns
        num_cols = df._get_numeric_data().columns
        Categ_cols=list(set(cols) - set(num_cols))
        lenght=len(Categ_cols)
        for i in range (lenght):
         st.markdown("""<hr style="height:2px;border:none;color:#66CD00;background-color:#333;" /> """, unsafe_allow_html=True)
         st.write('Variable name:',Categ_cols[i])
         st.write('Unique values',df[Categ_cols[i]].unique())
         st.write('Number of unique values', df[Categ_cols[i]].nunique())
      except:
         st.write( 'This dataset does not contain categorical variables')
except:     
 st.write( 'Please, load a dataset as a CSV file')
