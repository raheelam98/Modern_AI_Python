import streamlit as st
import pandas as pd
import os
from io import BytesIO

# set up app
st.set_page_config(page_title="Data sweeper", layout="wide")
st.title("Data sweeper")
st.write("Tranform your files between CSV and Excel; formats with built-in data cleaning and visualization!")

#custom css
st.markdown(
    """
    <style>
    .stApp{
        #background-color: #f5f5f5;
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# create button to upload files
uploaded_files = st.file_uploader("Upload your files (CSV or Excel) :", type=['csv', 'xlsx'], accept_multiple_files=True)

# build logic to transform files
if uploaded_files:
    for file in uploaded_files:
        # get file extension [-1] is last element of the list
        file_extension = os.path.splitext(file.name)[-1].lower()
        
        if file_extension == ".csv":
            df = pd.read_csv(file)
        elif file_extension == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_extension}")
            
        # Display info about the file
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size/1024:.2f} KB")
        # st.write(f"**File Size:** {file.size/1024}")
        
        # Show the 5 rows of the data
        st.write("Preview the Head of the Dataframe")
        st.write(df.head())
        
        # Option for data cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)
             
            # with is context manager
            # Button to remove duplicates
            with col1:
                if st.button(f"Remove Duplicates for {file.name}"):
                    df = df.drop_duplicates()
                    st.write("Duplicates Removed")
                    
            # Button to for missing values   
            with col2:
                if st.button(f"Remove Missing Values for {file.name}"):
                    # note it will only apply to numeric columns
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values have been Filled")
                    
                    
        # Choose Specific Columns to Keep or Convert
        st.subheader("Select Columns to Convert") 
        columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
        df = df[columns] 
        
        # creating chart for the data (check)
        # Create Some Data Visualizations befor exporting
        st.subheader("Data Visualizations")
        if st.checkbox(f"Show Data Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])
            # st.bar_chart(df.select_dtypes(include='number'.iloc[:,:2]))
            
         
        # Note :-  BytesIO converts the data into bytes and store it in memory for short time   
        # Convert the File -> CSV to Excel
        st.subheader("Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name )
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            
            # Convert to CSV
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_extension, ".csv")
                mime_type = "text/csv"
                    
            # Convert to Excel
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_extension, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                
            buffer.seek(0)    
            
            # Download the file
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            ) 
            
st.success("All Files processed!")               
            
            
            
                     
                
                
                
                
                
                
                 
        