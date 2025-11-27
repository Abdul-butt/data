import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv('india.csv')
list_of_states = list(df.State.unique())
list_of_states.insert(0,'overall India')
list_of_parametrs = list(df.columns.drop(['State','District']))
st.sidebar.title('DATA VIZ')
selected_state=st.sidebar.selectbox('Select a state',list_of_states)
primary=st.sidebar.selectbox('Select a Primary Parameter',list_of_parametrs)
secondry=st.sidebar.selectbox('Select a Secondry Parameter',list_of_parametrs)
plot = st.sidebar.button('PLOT Graph')
if plot:
    if selected_state == 'overallIndia':
        fig = px.scatter_mapbox(df, lat='Latitude',lon='Longitude',zoom=3,size=primary,color=secondry,mapbox_style='open-street-map',width=1200,height=500)
        st.plotly_chart(fig, use_container_width=True)

    else:
        state_df=df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=3, size=primary, color=secondry,
                                mapbox_style='open-street-map', width=1500, height=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)