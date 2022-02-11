# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:34:26 2022

@author: Ricky D Cruze
Hans Rosling Gapminder
"""

import plotly_express as px
import pandas as pd 
import streamlit as st

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Hans Rosling's Iconic Animated Motion Chart", page_icon=":purple_heart:", layout= "wide")


### --- LOAD DATAFRAME
gapminder = px.data.gapminder()
##making variables for later use
country = gapminder['country'].unique().tolist()
year = gapminder['year'].unique().tolist()
continent = gapminder['continent'].unique().tolist()
################################################

st.header('Scatter plot animation using Gapminder dataset!')
## Scatter plot animation

animated_scatter= px.scatter(gapminder, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="country", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90],template= 'plotly_white', width=1000, height=800)
st.write(animated_scatter)

##################



st.header('Who is Hans Rosling?')

head_col1, head_col2 = st.columns(2)
with head_col1:
    st.subheader("From Wikipedia: ")  
    st.write("""Hans Rosling (Swedish pronunciation: [ˈhɑːns ˈrûːslɪŋ]; 27 July 1948 – 7 February 2017) was a Swedish physician, 
            academic, and public speaker. He was a professor of international health at Karolinska Institute[4] and 
            was the co-founder and chairman of the Gapminder Foundation, which developed the Trendalyzer software system. 
            He held presentations around the world, including several TED Talks[5] in which he promoted the use of data 
            (and data visualization) to explore development issues.[6] His posthumously published book Factfulness, 
            coauthored with his daughter-in-law Anna Rosling Rönnlund and son Ola Rosling, became an international bestseller.[7]""")
          
   
with head_col2:
    showpicture = st.checkbox('Like to see his picture: ')
    if showpicture: 
        st.image("hans.jpg")
   



# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)




