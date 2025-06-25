import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title = "Aerofit Treadmill Analysis",layout= "wide")
st.title("Aerofit Treadmill Analysis")

uploaded_file = st.file_uploader("please upload your Dataset",type = ["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    #Basic sub header
    st.subheader("Data Preview")
    st.dataframe(df.head())
    
    st.subheader("shape of the Dataset")
    st.write("Number of rows and columns in the dataset are:",df.shape)
    st.write("columns names of my Dataset:",df.columns.to_list())
    
    # Create few checkbox
    st.subheader("Statistics of the Dataset")
    data_info = st.checkbox("Show data types")
    missing_value = st.checkbox("Show missing values")
    statistics =st.checkbox("Show the statistical summary of the dataset") 
    
    if data_info:
        st.write("Data types of the Dataset:",df.info())  # returns the none for stramlit shows none 
    if missing_value:
        st.write("Missing values of the Dataset",df.isna().sum(axis = 0))
    if statistics:
        st.write("Dataset statistics are:",df.describe())        
    
    # Create radio button
    st.subheader("Dataset Information")
    option = st.radio(
        "Select the type of dataset information you want to view:",
        ("Show data types", "Show missing values", "Show statistical summary")
    )

    if option == "Show data types":
        st.write("Data types of the Dataset:")
        st.write(df.dtypes)
    elif option == "Show missing values":
        st.write("Missing values in the Dataset:")
        st.write(df.isna().sum())
    elif option == "Show statistical summary":
        st.write("Statistical Summary:")
        st.write(df.describe())
        
    # visnual Analysis of our Dataset
    # column selector
    
    numeric_cols = df.select_dtypes(include = ["int64","float"]).columns.tolist()    
    categorical_cols = df.select = df.select_dtypes(include = ["object"]).columns.tolist()   
    st.write(numeric_cols)
    st.write(categorical_cols)
    
    # Uni- variate Analysis
    # count plot
    st.subheader("count plot ")
    selected_cols = st.selectbox("select a nueric column ",numeric_cols)  
    fig,ax = plt.subplots()
    sns.countplot(x = df[selected_cols],ax =ax) 
    st.pyplot(fig)   
    
    st.subheader("count plot")
    cat_cols = st.selectbox("select a nueric column ",categorical_cols)  
    fig,ax = plt.subplots()
    sns.countplot(x = df[cat_cols],ax =ax) 
    st.pyplot(fig)
    
    #Box plot for Numerical Columns
    st.subheader("Box plot for checking the outliers")
    box_cols = st.selectbox("Select a numeric column", numeric_cols, key="box_cols_unique_1")
    fig,ax = plt.subplots()
    sns.countplot(x = df[box_cols],ax =ax) 
    st.pyplot(fig)
    
    # Histogram plot for Numerical Columns
    st.subheader("Histogram for checking the distribution of numeric columns")
    hist_cols = st.selectbox("Select a numeric column", numeric_cols, key="hist_cols_unique_1")
    fig, ax = plt.subplots()
    sns.histplot(df[hist_cols], kde=True, ax=ax, bins=30)  # kde adds a density curve, optional
    ax.set_title(f"Histogram of {box_cols}")
    st.pyplot(fig)


    # Bi - variate
    #box plot
    st.subheader("Bi-variate Analysis of our Dataset: Categorical Vs Numerical")  
    num_cols = st.selectbox("Select a numeric column", numeric_cols, key="num1")  
    category_cols = st.selectbox("select a nueric column ",categorical_cols,key = 'cat1')
    fig,ax = plt.subplots()
    sns.boxplot(x=df[num_cols],y = df[category_cols],ax = ax)
    st.pyplot(fig)
    
    # scatteplot
    st.subheader("scatter plot")  
    num_cols = st.selectbox("Select a numeric column", numeric_cols, key="scatter_num_col")  
    category_cols = st.selectbox("select a nueric column ",categorical_cols,key = 'scatter_cat_col')
    fig,ax = plt.subplots()
    sns.scatterplot(x=df[num_cols],y = df[category_cols],ax = ax)
    st.pyplot(fig)
    
    # Multi-variateAnalysis
    #Heatmap of our dataset to check the  corelation
    st.subheader("co-relation Heatmap")
    fig,ax = plt.subplots(figsize =(10,6))
    sns.heatmap(df[numeric_cols].corr(),annot =True,cmap ="magma",ax =ax)
    ax.set_title("Correlation between Numerical Features")
    st.pyplot(fig)
    
    #pair plot
    st.subheader("Pair plot")
    fig = sns.pairplot(df[numeric_cols])
    st.pyplot(fig)    
    
else:
    st.write("please upload the Dataset first for the EDA")    