import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json


scenario_data = pd.read_csv('scenario_data.csv')
all_sites = tuple(scenario_data['Site'].unique())

st.header('Hello World')
selected_site = st.selectbox('Site:', all_sites)

comparison_tab, detail_tab = st.tabs(['Scenario Comparison', 'Scenario Details'])
with comparison_tab:
    selected_scenarios = st.multiselect('Scenarios', scenario_data[scenario_data['Site'] == selected_site]['Scenario Name'].unique())
    fig = go.Figure()
    for scenario in selected_scenarios:
        scenario_rows = scenario_data[(scenario_data['Site'] == selected_site) & (scenario_data['Scenario Name'] == scenario)]
        max_peak_power = scenario_rows['Peak Power'].max()
        productive_time = scenario_rows['% Productive Hours'].mean()
        nonproductive_time = scenario_rows['% Non-productive Hours'].mean()
        fig.add_trace(go.Bar(
            x=['Peak Power', '% Productive', '% Non-productive'],
            y=[max_peak_power, productive_time, nonproductive_time],
            name=scenario,
        ))
    st.plotly_chart(fig, use_container_width=True)
    selected_param = st.selectbox('View parameter by year', ['Peak Power', '% Productive Hours', '% Non-productive Hours'])
    fig2 = go.Figure()
    for scenario in selected_scenarios:
        df_sorted = scenario_data[(scenario_data['Site'] == selected_site) & (scenario_data['Scenario Name'] == scenario)].sort_values(['Year'])
        fig2.add_trace(go.Scatter(
            x=df_sorted['Year'],
            y=df_sorted[selected_param],
            name=scenario,
        ))
    st.plotly_chart(fig2, use_container_width=True)
    
with detail_tab:
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