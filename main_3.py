import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json

# if __name__ == '__main__':
scenario_data = pd.read_csv('scenario_data.csv')
all_sites = tuple(scenario_data['Site'].unique())

st.header('Hello World')
selected_site = st.selectbox('Site:', all_sites)
selected_scenario = st.selectbox('Scenario Code:', scenario_data[scenario_data['Site'] == selected_site]['Scenario Name'].unique())
st.dataframe(scenario_data[(scenario_data['Site'] == selected_site) & (scenario_data['Scenario Name'] == selected_scenario)])

selected_year = st.selectbox('Year:', scenario_data[(scenario_data['Site'] == selected_site) & (scenario_data['Scenario Name'] == selected_scenario)]['Year'].unique())
year_data = scenario_data[(scenario_data['Site'] == selected_site) & (scenario_data['Scenario Name'] == selected_scenario) & (scenario_data['Year'] == selected_year)].iloc[0]
without_trolley = json.loads(year_data['Without Trolley'].replace('(', '[').replace(')', ']'))
with_trolley = json.loads(year_data['With Trolley'].replace('(', '[').replace(')', ']'))
fig = go.Figure()
for group in without_trolley:
    fig.add_trace(go.Scatter(
        x=[x for (x,y) in group],
        y=[y for (x,y) in group],
        mode='lines',
        name='No Trolley',
    ))
for group in with_trolley:
    fig.add_trace(go.Scatter(
        x=[x for (x,y) in group],
        y=[y for (x,y) in group],
        mode='lines',
        name='Trolley',
    ))
st.plotly_chart(fig, use_container_width=True)