# Age-Wise
Estimating local care home need for seniors 

Estiamted Washingting State care home demand distribution
![Image of Yaktocat](https://github.com/mxynapoleon/Age-Wise/blob/master/WA.png)

# Motivation
COVID-19 started in the US from a senior care home in Seattle. It reveals serious problems under the surface and the vulnerability of the senior population. Something must be done and Age Wise is a small attempt to solve the problems. 

Ageing population is global issue. United States ranked 61 in 2019 by comparing the median age of the nation across the world. But it is climbing fast. Building care home is critical to protect the growing senior population and United States has a lot to catch. Even within the under suppleid US care home makert, the resources are heavily unbalanced. Determining the right location to build new care home or relocate limited resources to those of high demand area is crutial to care home providers. 

# Problem Statement
Given limited resources, how care home provides efficiently manage their current facilities and smartly determine where to build the next care home?

# Data Sources
Data.gov, US Census, Office of Financial Management, Washington State Department of Social and Health Services, New York State Department of Health

# Results and Insights
In this project, 176 features are collected to construct the dataset. They can be categorized into three buckets: demographic including race, gender and age segments, healthcare including number of local phisician, hospital, hospital bed, disable population, and economic including median income and household numbers. Washington and New York States are selected as the training targets. An Lasso regulization is performed and the 21 highly correlated features are selected. A random forest model is trained and then used to predict local county care home demand. 

Insights:
* Age 85+ population has high demand of care home (which is not suprising). 
* Healthcare infrastructures (number of physician, hospital, hospital bed) have strong correlation to care home demand. 

# Tools and Skills
* AWS EC2
* Streamlit
* Python
* GeoPandas
* Random Forest
* Lasso
* ETL
* Feature Engineering
