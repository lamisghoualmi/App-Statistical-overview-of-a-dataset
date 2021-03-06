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
st.sidebar.image("AppStatOverView.png", use_column_width=True)
st.sidebar.write("""
        Making informed decisions requires a meticulous, step-by-step process of data analysis. Before beginning the analysis,
        it is crucial to look at the dataset's descriptive statistical overview. This app helps you get the general statistical 
        description of a dataset, a clear idea of the measures you need to take to clean your data, and helps you ask the right 
        questions. It has the following functionalities: First, the size of the data. Second, the dataset column names. Using this
        might correct some misspelled columns' names or rename your variables to meaningful expressions that clearly express their purpose.
        Third,  the data column types. Identifying the different data types helps you define which variables need to be formatted. 
        Fourth, missing values are a common problem in data cleaning. Analyzing the percentage of missing values gives you a better 
        notion of the method to use to process them. For example, removing missing values, applying an imputation technique
        (replacing by zero, constant, mean, median, most frequent value, etc.). Fifth, the descriptive statistics summary of the 
        numerical  data gives you an idea of the potential outliers that can have a disproportionate effect on your data. It also 
        helps you get the variables with low variance. These kinds of variables add little to no information to your analysis and, 
        therefore, are irrelevant and have to be removed. Sixth, descriptive statistics summary of the categorical data. This can be 
        used to determine whether the population is biased or to possibly fix the category's error if any. For instance, if a user entered 
        "SINGLE" and another one entered "ALONE," the information would fall under the same category, "SINGLE." So, this kind of error has
        to be addressed before starting the analysis. If you are interested to check my code, check my github using 
        the following link: [Github](https://github.com/lamisghoualmi/-App-Statistical-overview-of-a-dataset).
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
        st.caption(' The number of missing values per column helps decide which technique you need to get rid of missing values. Example: removing missing values or applying an amputation technique to replace those missing values.')
                   
        st.write(df.isnull().sum())
     except:
       st.write( 'There are no missing values in this dataset.')
    
    if option=='Percentages of missing values': 
     try:
        st.caption('Percentages of missing values helps decide which technique you need to get rid of missing values. Example: removing missing values or applying an amputation technique to replace those missing values.')
                   
        for col in df.columns:
            PercentageMissing = np.mean(df[col].isnull())
            # print('{} - {}%'.format(col, round(PercentageMissing *100)))
            st.write('{} : {}%'.format(col, round(PercentageMissing *100)))
     except:
       st.write( 'There are no missing values in this dataset.')
    
    if option=='Zeros values per column':
     try:
        st.caption('Zeros values per column')
        zero_val = (df == 0.00).astype(int).sum(axis=0)
        st.write(zero_val)
     except:
        st.write( 'There are no zero values in this dataset.')
        
    if option=='Summarization of the data (Numerical variables)': 
        try:
         st.caption('Summarization of the data (Numerical variables). By examining each variable  minimum, maximum, and average values, you can look for variables that potentially contain outliers.')
         st.write(df.describe())
        except:
         st.write( 'Numerical variables are not present in this dataset.')
        
         
    if option=='Summarization of the data (Categorical variables)': 
      try:
        st.caption('You can use this to determine whether the population is biased and to possibly fix the categories error if any. For instance, if a user entered SINGLE and another one entered  ALONE, the information would fall under the same category, SINGLE. So, this kind of error has to be addressed before starting the analysis.')
                   
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
         st.write( 'There are no categorical variables in this dataset.')
except:     
 st.write( 'Please, load a dataset as a CSV file')
