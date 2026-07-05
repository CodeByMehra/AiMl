# Entry point file for stramlit

import streamlit as st
 
def main():
    st.header("Hey")
    name = st.text_input("Enter Name")

    st.button("Submit" , type= "primary")

main()