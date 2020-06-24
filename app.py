#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


# Analysis packages
import pandas as pd
import numpy as np
import pickle
import joblib
import sklearn
from sklearn.preprocessing import StandardScaler


# In[3]:


# Geo Pkgs
import geopandas as gpd 
import json
import geoplot
# Configure matplotlib.
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
import matplotlib.colors as colors


# In[4]:


#__________main page_________________

st.title("Age-Wise")
st.subheader("Estimating local care home need for seniors")

st.text("Age-Wise estimates the number of care home demand/over-supply for seniors (age 65+) in county level")

#city = st.selectbox("select a state", ("Washington", "New York"))


# In[5]:


if st.button("New York State"):
	# get geo data
	NY = gpd.read_file("New York.geojson", driver='geoJSON')
	NY = NY.drop(['GEO_ID', 'STATE', 'COUNTY', 'LSAD'],axis=1)
	NY.rename(columns = {'NAME':'County'}, inplace = True) 
	# loading state data
	NY_care = pd.read_csv('New York.csv')
	NY_merged = NY.set_index('County').join(NY_care.set_index('County'))
	# set a variable that will call whatever column we want to visualise on the map
	variable = 'demand'
	ax = plt.subplots(1, figsize=(10, 6))
	ax = NY_merged.plot(column=variable, cmap = 'YlGnBu' , figsize=(20,10), scheme='quantiles',edgecolor='1', k=10, legend = True)
	ax.annotate('Tool: Age Wise',xy=(0.15, 0.25),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
	# mapping the choropleth
	ax.set_axis_off()
	ax.get_figure()


# In[ ]:


if st.button("Washington State"):
	# get geo data
	WA = gpd.read_file("Washington.geojson", driver='geoJSON')
	WA = WA.drop(['GEO_ID', 'STATE', 'COUNTY', 'LSAD'],axis=1)
	NY.rename(columns = {'NAME':'County'}, inplace = True) 
	# loading state data
	WA_care = pd.read_csv('Washington.csv')
	WA_merged = WA.set_index('County').join(WA_care.set_index('County'))
	# set a variable that will call whatever column we want to visualise on the map
	variable = 'demand'
	ax = plt.subplots(1, figsize=(10, 6))
	ax = NY_merged.plot(column=variable, cmap = 'YlGnBu' , figsize=(20,10), scheme='quantiles',edgecolor='1', k=25, legend = True)
	ax.annotate('Tool: Age Wise',xy=(0.8, 0.15),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
	# mapping the choropleth
	ax.set_axis_off()
	ay.get_legend().set_bbox_to_anchor((.18,.2))
	ax.get_figure()

