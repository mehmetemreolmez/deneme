# app.py
import streamlit as st
import pandas as pd
from simulation import run_simulation

st.title("Simulation Web App")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

param1 = st.number_input("Parameter 1", value=1.0)
param2 = st.number_input("Parameter 2", value=2.0)
param3 = st.number_input("Parameter 3", value=3.0)
param4 = st.number_input("Parameter 4", value=4.0)
param5 = st.number_input("Parameter 5", value=5.0)

if st.button("Run Simulation"):
    if uploaded_file is not None:
        result_df = run_simulation(uploaded_file, param1, param2, param3, param4, param5)
        st.success("Simulation complete!")
        st.dataframe(result_df)

        # Download link
        output_filename = "simulation_results.xlsx"
        result_df.to_excel(output_filename, index=False)
        with open(output_filename, "rb") as f:
            st.download_button("Download Results", f, file_name=output_filename)
    else:
        st.warning("Please upload a file before running the simulation.")
