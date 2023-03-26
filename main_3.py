import streamlit as st
import pandas as pd
import pyarrow.vendored.version

# if __name__ == '__main__':
scenario_data = pd.read_csv('scenario_data.csv')
all_sites = tuple(scenario_data['Site'].unique())

st.header('Hello World')
selected_site = st.selectbox('Site:', all_sites)
selected_scenario = st.selectbox('Scenario Code:', scenario_data[scenario_data['Site'] == selected_site]['Scenario Name'].unique())
st.dataframe(scenario_data[(scenario_data['Site'] == selected_site) & (scenario_data['Scenario Name'] == selected_scenario)])
