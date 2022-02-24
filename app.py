# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:34:26 2022

@author: Ricky D Cruze
Used dataset: Hans Rosling Gapminder Dataset
"""

import plotly_express as px
import pandas as pd 
import streamlit as st
import time
import numpy as np 

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Hans Rosling's Iconic Animated Motion Chart", page_icon=":purple_heart:", layout= "wide")

st.header('Data visualization of Gapminder dataset from Has Rosling:')

with st.expander("Who is Hans Rosling?"):
    col1, col2 = st.columns(2)

    with col1:
     st.write("""
        ***Hans Rosling*** (Swedish pronunciation: [ˈhɑːns ˈrûːslɪŋ]; 27 July 1948 – 7 February 2017) was a Swedish physician, 
        academic, and public speaker. He was a professor of international health at Karolinska Institute[4] and 
        was the co-founder and chairman of the Gapminder Foundation, which developed the Trendalyzer software system. 
        He held presentations around the world, including several TED Talks[5] in which he promoted the use of data 
        (and data visualization) to explore development issues.[6] His posthumously published book Factfulness, 
        coauthored with his daughter-in-law Anna Rosling Rönnlund and son Ola Rosling, became an international bestseller.[7]
     """)

    with col2:
        st.image("https://www.unhcr.org/neu/wp-content/uploads/sites/15/2016/10/rosling1_01.png")

### --- LOAD DATAFRAME
gapminder = px.data.gapminder()
##making variables for later use
country = gapminder['country'].unique().tolist()
year = gapminder['year'].unique().tolist()
continent = gapminder['continent'].unique().tolist()
################################################

st.subheader('Scatter plot animation using Gapminder dataset!')
st.markdown('''
---
''')

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)

## Scatter plot animation

animated_scatter= px.scatter(gapminder, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="country", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90],template= 'plotly_white', width=1000, height=800)
st.write(animated_scatter)

##################

## Sunburst
st.subheader('Sunburst for year 2007')
st.markdown('''
---
''')

gapminder_2007=gapminder.query("year == 2007")

sunburst_2007= px.sunburst(gapminder_2007,path=['continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(gapminder_2007['lifeExp'], weights=gapminder_2007['pop']))

st.write(sunburst_2007)







   



# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)




