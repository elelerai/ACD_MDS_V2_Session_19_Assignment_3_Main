# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 06:11:30 2018

@author: Eliud Lelerai
"""

import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

# performing a F-test 
  #Null Hypothesis(Ho): means of group1 and group2 are equal
  #Alternative Hypothesis(Ha): means of group1 and 2 are NOT equal
  
# Data organization

    #*******The Raw Data*****
    # Calculate F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25.

    #Creating data frame
df= pd.DataFrame({'group1':[10, 20, 30, 40, 50], 'group2' :[5,10,15, 20, 25]})

#  ONE WAY ANOVA TEST


stats.f_oneway(df['group1'],df['group2'])

# Analysis of variance test output:
    # f-value value=3.6
    # p-value=0.09
    

# Conclusion
   # p-value is approximately 0.09  which is high 0.05 significant level
   #  There is  no significant difference between the groups means